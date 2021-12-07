from socket import *
import os
import sys
import struct
import time
import select
import binascii

ICMP_ECHO_REQUEST = 8
MAX_HOPS = 30
TIMEOUT = 2.0
TRIES = 1

# The packet that we shall send to each router along the path is the ICMP echo
# request packet, which is exactly what we had used in the ICMP ping exercise.
# We shall use the same packet that we built in the Ping exercise


def checksum(string):
    csum = 0
    countTo = (len(string) // 2) * 2
    count = 0
    while count < countTo:
        thisVal = (string[count + 1]) * 256 + (string[count])
        csum += thisVal
        csum &= 0xffffffff
        count += 2

    if countTo < len(string):
        csum += (string[len(string) - 1])
        csum &= 0xffffffff

    csum = (csum >> 16) + (csum & 0xffff)
    csum = csum + (csum >> 16)
    answer = ~csum
    answer = answer & 0xffff
    answer = answer >> 8 | (answer << 8 & 0xff00)
    return answer


def build_packet():
    # Fill in start
    # In the sendOnePing() method of the ICMP Ping exercise ,firstly the header of our
    # packet to be sent was made, secondly the checksum was appended to the header and
    # then finally the complete packet was sent to the destination.
    processID = os.getpid() & 0xFFFF
    mychecksum = 0
    # header with 0 checksum
    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, mychecksum, processID, 1)
    data = struct.pack("d", time.time())
    # calculate the checksum on the data and the dummy header.
    mychecksum = checksum(header + data)

    if sys.platform == 'darwin':
        mychecksum = htons(mychecksum) & 0xffff
    else:
        mychecksum = htons(mychecksum)

    header = struct.pack("bbHHh", ICMP_ECHO_REQUEST, 0, mychecksum, processID, 1)

    # Make the header in a similar way to the ping exercise.
    # Append checksum to the header.
    # Don’t send the packet yet , just return the final packet in this function.
    # Fill in end
    # So the function ending should look like this
    packet = header + data
    return packet

def get_route(hostname):
    timeLeft = TIMEOUT
    tracelist1 = [] #This is your list to use when iterating through each trace
    tracelist2 = [] #This is your list to contain all traces

    for ttl in range(1, MAX_HOPS):
        for tries in range(TRIES):
            destAddr = gethostbyname(hostname)
            # Fill in start
            # Make a raw socket named mySocket
            mySocket = socket(AF_INET, SOCK_RAW, getprotobyname("icmp"))
            #Fill in end
            mySocket.setsockopt(IPPROTO_IP, IP_TTL, struct.pack('I', ttl))
            mySocket.settimeout(TIMEOUT)

            try:
                d = build_packet()
                mySocket.sendto(d, (hostname, 0))
                t= time.time()
                startedSelect = time.time()
                whatReady = select.select([mySocket], [], [], timeLeft)
                howLongInSelect = (time.time() - startedSelect)
                if whatReady[0] == []: # Timeout
                    tracelist1 = [str(ttl), '*', "Request timed out"]
                    #Fill in start
                    tracelist2.append(tracelist1)
                    #Fill in end
                recvPacket, addr = mySocket.recvfrom(1024)
                timeReceived = time.time()
                timeLeft = timeLeft - howLongInSelect
                if timeLeft <= 0:
                    tracelist1 = [str(ttl), '*', "Request timed out"]
                    #Fill in start
                    tracelist2.append(tracelist1)
                    #Fill in end
            except timeout:
                continue
            else:
                #Fill in start
                #Fetch the icmp type from the IP packet
                icmpHeader = recvPacket[20:28]
                types, code, checksum, packetID, sequence = struct.unpack("bbHHh", icmpHeader)
                #Fill in end
                try: #try to fetch the hostname
                #Fill in start
                    destAddr = gethostbyname(hostname)
                    destName = gethostbyaddr(destAddr)
                #Fill in end
                except herror as e: #if the host does not provide a hostname
                #Fill in start
                    tracelist1.append("unknown host : " + str(e))
                #Fill in end
                if types == 11:
                    bytes = struct.calcsize("d")
                    timeSent = struct.unpack("d", recvPacket[28:28 + bytes])[0]
                    ttk = int((timeReceived - t)*1000)
                    #Fill in start
                    #You should add your responses to your lists here
                    tracelist1 = [str(ttl), str(ttk)+'ms', str(addr[0]), str(destName[0])]
                    
                    tracelist2.append(tracelist1)
                    #Fill in end
                elif types == 3:
                    bytes = struct.calcsize("d")
                    timeSent = struct.unpack("d", recvPacket[28:28 + bytes])[0]
                    ttk = int((timeReceived - t)*1000)
                    #Fill in start
                    #You should add your responses to your lists here
                    tracelist1 = [str(ttl), str(ttk)+'ms', str(addr[0]), str(destName[0])]
                    tracelist2.append(tracelist1)
                    #Fill in end
                elif types == 0:
                    bytes = struct.calcsize("d")
                    timeSent = struct.unpack("d", recvPacket[28:28 + bytes])[0]
                    ttk = int((timeReceived - t)*1000)
                    #Fill in start
                    #You should add your responses to your lists here and return your list if your destination IP is met
                    tracelist1 = [str(ttl), str(ttk)+'ms', str(addr[0]), str(destName[0])]
                    tracelist2.append(tracelist1)
                    
                    if(str(addr[0]) == destAddr):
                        return tracelist2
                    #Fill in end
                else:
                    #Fill in start
                    #If there is an exception/error to your if statements, you should append that to your list here
                    #Fill in end
                    tracelist2.append("error")
            finally:
                mySocket.close()

# get_route("www.google.com")
# print(get_route("www.bing.com"))
get_route("www.bing.com")


# Output for bing.com
'''
[   ['1', '0ms', '192.168.0.252', 'a-0001.a-msedge.net'], 
    ['2', '5ms', '10.24.0.1', 'a-0001.a-msedge.net'],
    ['3', '4ms', '45.116.1.45', 'a-0001.a-msedge.net'], 
    ['4', '20ms', '45.116.0.137', 'a-0001.a-msedge.net'],
    ['5', '*', 'Request timed out'], 
    ['6', '*', 'Request timed out'],
    ['7', '21ms', '104.44.212.195', 'a-0001.a-msedge.net'], 
    ['8', '*', 'Request timed out'], 
    ['9', '*', 'Request timed out'],
    ['10', '*', 'Request timed out'], 
    ['11', '20ms', '204.79.197.200', 'a-0001.a-msedge.net']
]

'''