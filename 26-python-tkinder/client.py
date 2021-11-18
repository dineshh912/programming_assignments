import sqlite3
from tkinter import *
import socket
import json
import matplotlib
matplotlib.use("TkAgg") # use matplotlib with tkinder
from matplotlib import pyplot as plt


class ClientUI:

    def __init__(self):

        self.start_connection() # establish socket connection with server
        self.get_country_name() # Retrive all countey name to show on dropdown
        self.start_UI() # start Tkinder UI

    def start_connection(self):
        self.c = socket.socket()
        self.c.connect((socket.gethostname(), 8080))
        
    def get_country_name(self):
        # After connection established get all country name from server
        # This is for the values in the dropdown
        res = self.c.recv(1024).decode()
        res = json.loads(res) 
        self.country_list = res
                    
    def start_UI(self):
        # create tkinder object
        root = Tk()
        # size of the window
        root.geometry("400x300")
        # datatype for menu text
        var = StringVar()
        # Create dropdown menuu
        menu = OptionMenu(root,
                          var, 
                          *self.country_list, 
                          command=self.get_country_data)
        menu.pack()

        # Create label
        label = Label( root , text = "Select Country:" )
        label.pack()

        root.mainloop()    


    def get_country_data(self, name):

        self.c.send(name.encode()) # encode country name and send to server

        res = self.c.recv(1024).decode()# Result from server
        res = json.loads(res) 
        # Get x and y from the result
        x = []
        y = []
        for k, v in res.items():
            x.append(int(k))
            y.append(float(v))

        plt.figure(figsize=(10,6))
        
        plt.title(name)
        plt.plot(x,y) 
        plt.show()


    def disconnect(self):
        # Disconnect from server
        self.c.close()


if __name__ == "__main__":

    Client = ClientUI()
    Client.disconnect()