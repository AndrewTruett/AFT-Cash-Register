
import mysql.connector
from mysql.connector import errorcode
try:
    cnx = mysql.connector.connect(
    user= 'JCS18Al1052',
    password= '23421052',
    host= '127.0.0.1',
    port='9999',
    database= 'JCS18336AFT')

except mysql.connector.Error as e:
    if e.errno==errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with username and password")
    elif e.errno==errorcode.ER_BAD_DB_ERROR:
        print("Database doesn't exist")
    else:
        print(e)

        # Create a test query function just to connect to the database.

        # def query(cursor):
        #     cnx = mysql.connector.connect()
        #     cursor = cnx.cursor()
        #
        #     query = ("SELECT *FROM Cashier;")
        #     cursor.execute(query)
        #     data = cursor.fetchall()
        #     for row in data:
        #         print(row[0],row[1])
        #         cnx.commit()
        #     cursor.close()
        #     cnx.close()

        # Query every single table on the database with making functions.
        cnx = mysql.connector.connect()
        cursor = cnx.cursor()

        def showAgeRestrictedItem(cursor):
            query= ("SELECT * FROM AgeRestrictedItem;")
            cursor.execute(query)
            return cursor

        def showCashier(cursor):
             query = ("SELECT * FROM Cashier;")
             cursor.execute(query)
             return cursor

        def showGeneralItem(cursor):
                query = ("SELECT * FROM GeneralItem;")
                cursor.execute(query)
                return cursor

        def showManager(cursor):
                query = ("SELECT * FROM Manager;")
                cursor.execute(query)
                return cursor
        def showMemeber(cursor):
            query=("SELECT * FROM Member;")
            cursor.execute(query)
            return cursor
        def showCategories(cursor):
             query= ("SELECT * FROM Categories;")
             cursor.excute(query)
             return cursor


