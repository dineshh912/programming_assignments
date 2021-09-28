# importiong needed python packages
import sqlite3

def create_connection(db_file_location):
    """
        create a database connection to the sqlite database
        arg:
        -db_file_location : path to the database file
    """
    conn =  None
    try:
        conn = sqlite3.connect(db_file_location) # Establish connection to the DB
        return conn
    except Exception as e:
        print(str(e)) # Error


def create_table(dbconnction, sql_query):
    """
        create  a table fomr the sql query
        parameters:
        dbconnection -  Database connection object
        sql_query - sql query to create table
    """
    try:
        c = dbconnction.cursor() # Create cursor which helps to execute sql query
        c.execute(sql_query) # Executing SQL Query
    except Exception as e:
        print(str(e)) # Error


def main():
    # Intialize Database location
    database_file_location = "reviewData.db" 

    # Review table sql query
    sql_create_reviews_table = """CREATE TABLE IF NOT EXISTS reviews (
                                        username CHAR(40) NOT NULL,
                                        Restaurant CHAR(50) NOT NULL,
                                        ReviewTime datetime,
                                        Rating FLOAT NOT NULL,
                                        Review CHAR(500) NOT NULL
                                    )"""

    # Rating table sql query
    
    sql_create_ratings_table = """CREATE TABLE IF NOT EXISTS ratings (
                                    Restaurant CHAR(50) NOT NULL,
                                    Food FLOAT NOT NULL,
                                    Service FLOAT NOT NULL,
                                    Ambience FLOAT NOT NULL,
                                    Price FLOAT NOT NULL,
                                    Overall FLOAT NOT NULL
                                )"""

    # create a database connection
    conn = create_connection(database_file_location)

    if conn is not None:
        # create review table
        create_table(conn, sql_create_reviews_table)

        # create rating table
        create_table(conn, sql_create_ratings_table)

        # Confirmation Messgage
        print("Database and Table has been created!")
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()