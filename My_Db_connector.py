import mysql.connector
from db_config import host,user,password,database

class My_Db:

    def __init__ (self,query:str):
        self.my_db = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            port=3306,
            database=database
        )

        self.my_cursor = self.my_db.cursor()
        self.my_cursor.execute(query)
        self.result = self.my_cursor.fetchall()
        self.my_db.commit()
    def get_result(self):

        return self.result