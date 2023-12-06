import mysql.connector
import dbconfig as cfg

class PlayerStatsDAO:
    
    #connect DB
    def __init__(self):
        self.db = mysql.connector.connect(
        host=cfg.mysql['host'],
        user=cfg.mysql['user'],
        password=cfg.mysql['password'],
        database=cfg.mysql['database']
        )

def getCursor(self): 
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor
    
def closeAll(self):
    self.connection.close()
    self.cursor.close()

# create PlayerStats entry
def create(self,values):
    cursor = self.getCursor()
    sql = "INSERT INTO playerstats (Full_Name, Prize_Money, Year) VALUES (%s, %s, %s)"      
    cursor.execute(sql, values)

    self.connection.commit()
    newid = cursor.lastrowid
    self.closeAll()
    return newid
    
# get all the data in the PlayerStats table
def getAll(self):
    cursor = self.getCursor()
    sql="select * from playerstats"
    cursor.execute(sql)
    result = cursor.fetchall()
    self.closeAll()
    return result

# find playerstats by id
def findByID(self, id):
    cursor = self.getCursor()
    sql="select * from playerstats where id = %s"
    values = (id,)

    cursor.execute(sql, values)
    result = cursor.fetchone()
    self.closeAll()
    return result

# find the data for a particular year
def findByYear(self, Year):
        cursor = self.db.cursor()
        sql = "SELECT * FROM playerstats WHERE Year = %s"
        values = (Year,)

        cursor.execute(sql, values)
        result = cursor.fetchone()
        self.closeAll()
        return result

# delete entry by id
def delete(self, id):
    cursor = self.getCursor()
    sql="delete from playerstats where id = %s"
    values = (id,)
    cursor.execute(sql, values)
    self.connection.commit()
    self.closeAll

playerstatsdao = PlayerStatsDAO()