# importing python packages
import threading # threading package
import requests # Open web pages
import sqlite3
from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import time

class ScrapeData: 

    def __init__(self): # Initialized with the self variable to access the attributes of the object

        # Create db file and establish connection
        conn = sqlite3.connect('global_radiative_forcing_data.db')
        # Cursor
        cur = conn.cursor()
        # Create table
        create_table = "CREATE TABLE IF NOT EXISTS radiative_forcing (Year VARCHARS(20), CO2 VARCHARS(20), CH4 VARCHARS(20), N2O VARCHARS(20), CFC12 VARCHARS(20), CFC11 VARCHARS(20), MINOR15 VARCHARS(20))"
        # Execute create new table query
        cur.execute(create_table)

    def get_data(self): 
        '''
            This method retrive data from URL and save it on the database.
        '''
        data_url = "https://www.esrl.noaa.gov/gmd/aggi/aggi.html"
        res = requests.get(data_url)  # Visit url and save the response

        # BS4 library to extract information
        soup = bs(res.text, 'html.parser')
        table_elements = soup.find("table",{"class":"table table-bordered table-condensed table-striped table-header"})

        data_rows = table_elements.findAll('tr')[2:]
        year = []
        CO2 = []
        CH4 = []
        N2O = []
        CFC12 = []
        CFC11 = []
        minor15 = []

        for i in data_rows:
            data = i.findAll("td")
            year.append(data[0].text)
            CO2.append(data[1].text)
            CH4.append(data[2].text)
            N2O.append(data[3].text)
            CFC12.append(data[4].text)
            CFC11.append(data[5].text)
            minor15.append(data[6].text)

        conn = sqlite3.connect('global_radiative_forcing_data.db') #Connects to the db file
        cur = conn.cursor()
        for i in range(len(year)):
            insert_into_table = "INSERT INTO radiative_forcing (Year, CO2, CH4, N2O, CFC12, CFC11, MINOR15) VALUES (?, ?, ?, ?, ?, ?, ?)"
            values_to_insert = (year[i], CO2[i], CH4[i], N2O[i], CFC12[i], CFC11[i], minor15[i])
            cur.execute(insert_into_table, values_to_insert)
            conn.commit()
        
        return 'Success'
    
    def linear_plot(file, agent):
        '''
            Linear plot method takes two args
            file : Database file
            agent: Agent variable 
        '''
        conn = sqlite3.connect(file) # Connects to the db file
        df = pd.read_sql_query(f"SELECT year, {agent} from radiative_forcing", con=conn)
        # Convert type of the result
        df["Year"] = df["Year"].astype(int)
        df[agent] = df[agent].astype(float)

        # Plot regression
        ax = sns.regplot(x="Year", y=agent, data=df,  truncate=False)
        # Label and title
        ax.set_ylabel(agent, fontsize = 15)
        ax.set_xlabel ('Year', fontsize = 15)
        ax.set_title(f"Year_vs_{agent}", fontsize = 18)
        # Save the figures
        fig = ax.get_figure()
        fig.savefig(f"plots/year_vs_{agent}")
        return 'saved'


if __name__ == "__main__":
    # Get the data from URL and save it
    ScrapeData().get_data()

    # Database file
    database_file = "global_radiative_forcing_data.db"

    agent_list = ["CO2", "CH4", "N2O", "CFC12", "CFC11", "MINOR15"]

    # Disable Plot GUI, we can't run thread and plot GUI at the same time
    plt.switch_backend('agg')
    for i in range(len(agent_list)):
        thread_function = threading.Thread(target = ScrapeData.linear_plot, args=(database_file, agent_list[i]))
        thread_function.start() #Starting the thread
        thread_function.join() #Joins the thread
        time.sleep(2) #Specifies the standby time