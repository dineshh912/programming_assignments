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
        # After connection established get all country name and send to client
        country_list = self.get_country_name()
        connection.send(country_list.encode()) 
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

    def get_country_name(self):
        conn = sqlite3.connect('undata.db') # connect to database
        cur = conn.cursor()
        select_query = "SELECT DISTINCT country from cdata" # select query
        cur.execute(select_query)
        results = cur.fetchall() 
        country_list = [] # save only country into list
        for i in results:
            country_list.append(i[0])
        cur.close()
        conn.close() # closing sql connection

        country_json = json.dumps(country_list)
        return country_json


if __name__ == "__main__":

    Server()