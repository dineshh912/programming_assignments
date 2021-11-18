import sqlite3
import xml.etree.ElementTree as ET


'''
Create SQL Database from XML file
'''
class CreateDB:
    '''
        This class wiil Reads the UNdata.xml file,
        create database and it's table. then insert values into the table
    '''
    def __init__(self):
        self.create_table()
        

    def create_table(self):
        # create DB file if not existed, and establish connection
        conn = sqlite3.connect('undata.db')
        cur = conn.cursor()    
        # Create Table and it's column if not exists.
        cur.execute("CREATE TABLE IF NOT EXISTS cdata (country, year, value)")
        cur.close()
        conn.close()
                    
    def insert_data(self,country, year, value):
        conn = sqlite3.connect('undata.db')
        cur = conn.cursor()
        insert_query = """INSERT INTO cdata (country, year, value) 
                                    VALUES (?,?,?)"""
        data = (country, year, value)
        cur.execute(insert_query, data)
        conn.commit() # Execute insert command
        cur.close()
        conn.close()


if __name__ == "__main__":

    UNData = CreateDB()
    tree = ET.parse('undata.xml')            
    root = tree.getroot()
    
    country = []
    year = []
    value = [] 

    for child in root:
        for record in child:
            country = record.findall('Country')
            year = record.findall('Year')
            value = record.findall('Value') 
            UNData.insert_data(country[0].text, year[0].text,value[0].text)