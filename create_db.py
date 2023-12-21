import pandas as pd
import mysql.connector
from mysql.connector import Error
import dbconfig  

# Import CSV
players_data = pd.read_csv(r'C:\Users\james\College\data_representation_project\data\Top2022.csv')
player_stats_data = pd.read_csv(r'C:\Users\james\College\data_representation_project\data\Stats.csv')

# Connect to MySQL Server
try:
    connection = mysql.connector.connect(
        host=dbconfig.mysql['host'],
        user=dbconfig.mysql['user'],
        password=dbconfig.mysql['password'],
        database=dbconfig.mysql['database']
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Create Players Table
        cursor.execute('''
            CREATE TABLE Players (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                Full_Name VARCHAR(255),
                Age INT,
                Nationality VARCHAR(255),
                CONSTRAINT unique_name UNIQUE (Full_Name)
            )
        ''')

        print("Players table created successfully.")

        # Insert data into Players Table
        for row in players_data.itertuples():
            cursor.execute('''
                INSERT INTO Players (Full_Name, Age, Nationality)
                VALUES (%s, %s, %s)
            ''', (row.Full_Name, row.Age, row.Nationality))

        print("Data inserted into Players table.")

        # Create PlayerStats Table
        cursor.execute('''
            CREATE TABLE PlayerStats (
                ID INT AUTO_INCREMENT PRIMARY KEY,
                Full_Name VARCHAR(255),
                Prize_Money INT,
                Year INT
            )
        ''')
        print("PlayerStats table created successfully.")

        # Insert data into PlayerStats Table
        for row in player_stats_data.itertuples():
            cursor.execute('''
                INSERT INTO PlayerStats (Full_Name, Prize_Money, Year)
                VALUES (%s, %s, %s)
            ''', (row.Full_Name, row.Prize_Money, row.Year))

        print("Data inserted into PlayerStats table.")

        # Commit changes
        connection.commit()

except Error as e:
    print(f"Error: {str(e)}")

finally:
    # Close the connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection closed.")

# References
# Lecture Notes
# Read in csv - other module projects
