import mysql.connector
import dbconfig as cfg

class PlayerDAO:

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

    # create Players entry
    def create(self, values):
        cursor = self.getCursor()
        sql = "INSERT INTO players (Full_Name, Age, Nationality) VALUES (%s, %s, %s);"      
        cursor.execute(sql,(values["Full_Name"], values["Age"], values["Nationality"]))
        self.db.commit()
        newid = cursor.lastrowid
        self.closeAll()
        print("done")
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
        returnvalue = self.convertToDictionary(result)
        result = cursor.fetchone()
        self.closeAll()
        return returnvalue

    # find the data for a particular year
    def findByNationality(self, Nationality):
        cursor = self.db.cursor()
        sql = "SELECT * FROM player WHERE Nationality = %s"
        values = (Nationality,)
        cursor.execute(sql, values)
        returnvalue = self.convertToDictionary(result)
        result = cursor.fetchall()
        self.closeAll()
        return returnvalue
    
    def update(self, values):
        cursor = self.getcursor()
        sql="update player set Full_Name= %s,Age=%s, Nationality=%s  where id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

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
    
    # delete entry by id
    def delete(self, id):
        cursor = self.getCursor()
        sql="delete from player where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        print("delete done")


    
    def convertToDictionary(self, result):
        colnames=['Full_Name', 'Age', 'Nationality']
        player = {colname: result[idx] for idx, colname in enumerate(colnames)}
        return player

PlayerDao = PlayerDAO()
