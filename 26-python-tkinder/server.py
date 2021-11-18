import sqlite3
import socket
import json


class Server:
    '''
        This class will initiate server.
        and handles data request from the client. 
    '''

    def __init__(self):
        self.StartServer()
       
    def StartServer(self):    
        s = socket.socket() # Creating socket
        s.bind((socket.gethostname(),8080)) # opening connection on specific port
        print("socket_created") # print socket is created
        s.listen(1) # waiting for client connection

        connection, address = s.accept()
        print(f'connection establisted :{address}') # print once connection established
        # If client connected
        while True:
            recvMsg = connection.recv(1024).decode() # decode received message.

            data = {} # new dict to store retrived values
                  
            conn = sqlite3.connect('undata.db') # Establish connection with database
            cur = conn.cursor() # create cursor
            select_query = f"SELECT * FROM cdata WHERE country = '{recvMsg}' ORDER BY year"  # select query to get specific country data
            cur.execute(select_query)
            results = cur.fetchall() 
            
            for i in results:
                data[i[1]]=i[2] # push data into dict for client to access.
                    
            cur.close() # close the cursor
            conn.close()  # close database connection             
            
            data_json = json.dumps(data) # convert dict into json
            connection.send(data_json.encode()) # sending retrived data back to client.
            
        connection.close() 


if __name__ == "__main__":

    Server()