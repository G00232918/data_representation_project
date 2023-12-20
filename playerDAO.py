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
        sql = "INSERT INTO players (ID, Full_Name, Age, Nationality) VALUES (%s, %s, %s, %s)" 
        newid = cursor.lastrowid
        cursor.execute(sql,(newid, values[0], values[1], values[2]))
        self.connection.commit()
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
        sql = "SELECT * FROM players WHERE id = %s"
        values = (id,)
        cursor.execute(sql, values)
        result = cursor.fetchone()  
        self.closeAll()
        
        if result:
            print(f"No player found with ID: {id}")
            return self.convertToDictionary(result)
        
        else:
            return None


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
        cursor = self.getCursor()
        sql="update players set Full_Name= %s,Age=%s, Nationality=%s  where id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()

    
    # delete entry by id
    def delete(self, id):
        cursor = self.getCursor()
        sql="delete from players where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        print("delete done")

    
    def convertToDictionary(self, result):
        colnames=['ID', 'Full_Name', 'Age', 'Nationality']
        player = {colname: result[idx] for idx, colname in enumerate(colnames)}
        return player
    
playerDAO = PlayerDAO()
