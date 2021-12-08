from socket import*
import os
import sys
import struct
import time
import select
import binascii
import statistics  # For standard deviation
# Should use stdev

ICMP_ECHO_REQUEST =8

def checksum(string):
    csum =0
    countTo = (len(string) //2) * 2
    count = 0

    while count < countTo:
        thisVal = (string[count +1]) * 256+ (string[count])
        csum += thisVal
        csum &= 0xffffffff
        count += 2

    if countTo < len(string):
        csum += (string[len(string) -1])
        csum &= 0xffffffff
    
    csum = (csum >>16) + (csum & 0xffff)
    csum = csum + (csum >>16)
    answer = ~csum
    answer = answer & 0xffff
    answer = answer >> 8| (answer <<8&0xff00)
    return answer


def receiveOnePing(mySocket, ID, timeout, destAddr):

    timeLeft = timeout

    while 1:
        startedSelect = time.time()
        whatReady = select.select([mySocket], [], [], timeLeft)
        howLongInSelect = (time.time() - startedSelect)
        if whatReady[0] == []: # Timeout
            return "Request timed out."
        
        timeReceived= time.time()
        recPacket, addr = mySocket.recvfrom(1024)
        # Fill in start
        # Fetch the ICMP header from the IP packet
        icmpheader = recPacket[20:28]
        # unpack the header
        types, code, checksum, packetID, sequence = struct.unpack("bbHHh", icmpheader)

        if packetID == ID and types != 8:
            bytesInDouble = struct.calcsize("d")
            timeSent = struct.unpack("d", recPacket[28:28 + bytesInDouble])[0]
            ts =  timeReceived - timeSent
            return ts
        # Fill in end

        timeLeft = timeLeft - howLongInSelect
        if timeLeft <=0:
            return"Request timed out."


def sendOnePing(mySocket, destAddr, ID):
    # Header is type (8), code (8), checksum (16),id (16), sequence (16)
    myChecksum = 0 
    
    # Make a dummy header with a 0 checksum
    # struct -- Interpret strings as packed binary data
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    data = struct.pack("d",time.time())

    # Calculate the checksum on the data and the dummyheader.
    myChecksum = checksum(header + data)

    # Get the right checksum, and put in the header
    if sys.platform =='darwin':
        # Convert 16-bit integers from host to networkbyte order
        myChecksum = htons(myChecksum) & 0xffff
    else:
        myChecksum = htons(myChecksum)
        
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, myChecksum, ID, 1)
    packet = header + data
    mySocket.sendto(packet, (destAddr,1)) # AF_INETaddress must be tuple, notstr

    # Both LISTS and TUPLES consist of a number of objects
    # which can be referenced by their position number within the object.

def doOnePing(destAddr,timeout):

    icmp = getprotobyname("icmp")
    
    # SOCK_RAW is a powerful socket type. For moredetails:http://sockraw.org/papers/sock_raw
    mySocket = socket(AF_INET, SOCK_RAW, icmp)

    myID = os.getpid() & 0xFFFF # Return the currentprocess i

    sendOnePing(mySocket, destAddr, myID)
    delay = receiveOnePing(mySocket, myID, timeout, destAddr)
    mySocket.close()
    return delay
    
def ping(host,timeout=1):
    # timeout=1 means: If one second goes by withouta reply from the server,
    # the client assumes that either the client's ping or the server's pong is lost
    try:
        dest = gethostbyname(host)

        print("Pinging "+ dest +" using Python:")
        print("")
        
        res = []
        # Calculate vars values and return them
        # vars = [str(round(packet_min, 2)), str(round(packet_avg, 2)),str(round(packet_max, 2)),str(round(stdev(stdev_var), 2))]
        # Send ping requests to a server separated by approximately one second
        for i in range(0,4):
            delay = doOnePing(dest,timeout)
            print(delay)
            res.append(delay)
            time.sleep(1) # one second
        
        # calculate vars values and return them
        # multiplying wih 1000 because it needs to be in ms
        packet_min = min(res) * 1000
        packet_avg = statistics.mean(res) * 1000
        packet_max = max(res) * 1000
        stddev_var = statistics.stdev(res) * 1000
        vars = [str(round(packet_min, 2)), str(round(packet_avg, 2)),str(round(packet_max, 2)),str(round(stddev_var, 2))]
        return vars
    except Exception as e:
        vars = ['0','0.0', '0', '0.0']
        return vars

if __name__ == '__main__':
    # ping("No.no.e")
    # ping("127.0.0.1")
    ping("google.co.il")
    # print(ping("google.co.il")) # valid host
    # print(ping("no.no.e")) # invalid host