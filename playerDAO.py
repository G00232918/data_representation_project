import mysql.connector
import dbconfig as cfg

class PlayerDAO:

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

    # create Players entry
    def create(self, values):
        cursor = self.getCursor()
        sql = "INSERT INTO players (Full_Name, Age, Nationality) VALUES (%s, %s, %s)"      
        cursor.execute(sql, values)
        self.db.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid
    
    # get all the data in the players table
    def getAll(self):
        cursor = self.getCursor()
        sql = "select * from players"
        cursor.execute(sql)
        result = cursor.fetchall()
        self.closeAll()
        return result

    def findByID(self, id):
        cursor = self.getCursor()
        sql = "select * from players where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return result

    # find the data for a particular year
    def findByYear(self, Nationality):
        cursor = self.db.cursor()
        sql = "SELECT * FROM player WHERE Nationality = %s"
        values = (Nationality,)
        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return result

    # Assuming your class has a database connection and a cursor (self.db and self.cursor)
    def find_cumulative_prize_by_year(self, nationality, year):
        cursor = self.db.cursor()

        # Modify the SQL query to join both tables and filter by nationality and year
        sql = """
            SELECT p.ID, p.Full_Name, p.Age, p.Nationality,
                   ps.Prize_Money, ps.Year,
                   SUM(ps.Prize_Money) OVER (PARTITION BY p.Nationality ORDER BY ps.Year) AS Cumulative_Total_Prize_Money
            FROM player p
            JOIN playerstats ps ON p.Full_Name = ps.Full_Name
            WHERE p.Nationality = %s AND ps.Year = %s
        """

        values = (nationality, year)
        cursor.execute(sql, values)
        result = cursor.fetchall()
        self.closeAll()
        return result

playerdao = PlayerDAO()
