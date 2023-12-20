import mysql.connector
import dbconfig as cfg

class PlayerStatsDAO:

    connection=""
    cursor =''
    host=       ''
    user=       ''
    password=   ''
    database=   ''
    
    def __init__(self):
        self.db = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['user'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database']
        )

    def getCursor(self): 
        # Using the existing database connection details
        self.connection = mysql.connector.connect(
            host=cfg.mysql['host'],
            user=cfg.mysql['user'],
            password=cfg.mysql['password'],
            database=cfg.mysql['database']
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    def find_cumulative_prize_by_year(self,ID,Full_Name,Total_Prize_Money):
        cursor = self.db.cursor()
        print(str("James"))
        # Modify the SQL query to join both tables and filter by player's full name
        sql = """
            SELECT p.ID, p.Full_Name, p.Age, p.Nationality,
                SUM(ps.Prize_Money) AS Cumulative_Total_Prize_Money
            FROM players p
            JOIN playerstats ps ON p.Full_Name = ps.Full_Name
            WHERE p.Full_Name = %s
            GROUP BY p.ID, p.Full_Name, p.Age, p.Nationality
        """
        values = (ID,Full_Name,Total_Prize_Money)
        cursor.execute(sql,values)
        returnvalue = self.convertToDictionary1(result)
        print(result)
        result = cursor.fetchall()
        self.closeAll()
        return returnvalue


    def convertToDictionary(self, result):
        colnames=['Full_Name', 'Prize_Money', 'Year']
        playerStat = {colname: result[idx] for idx, colname in enumerate(colnames)}
        return playerStat
    
    
playerStatsDAO = PlayerStatsDAO()