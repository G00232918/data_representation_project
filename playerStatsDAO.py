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

    # create PlayerStats entry
    def create(self,values):
        cursor = self.getCursor()
        sql = "INSERT INTO playerstats (Full_Name, Prize_Money, Year) VALUES (%s, %s, %s)"      
        cursor.execute(sql,(values["Full_Name"], values["Prize_Money"], values["Year"]))
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
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue
    
    def update(self, values):
        cursor = self.getcursor()
        sql="update playerstats set Full_Name= %s,Prize_Monay=%s, price=%s  where id = %s"
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()


    # delete entry by id
    def delete(self, id):
        cursor = self.getCursor()
        sql="delete from playerstats where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        print("delete done")



    def convertToDictionary(self, result):
        colnames=['Full_Name', 'Prize_Money', 'Year']
        playerStat = {colname: result[idx] for idx, colname in enumerate(colnames)}
        return playerStat
       

PlayerStatsDao = PlayerStatsDAO()