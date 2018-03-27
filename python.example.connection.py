#Must run these 2 commands before executing python code
#ssh -L 9999:localhost:9999 username@134.74.126.104 -> this will prompt for a password, give it a moment to log you in
#then run ssh -L 9999:localhost:3306 username@134.74.146.21 -> this will prompt for a password again
#once you have run the last command, leave the window open, and run the python code.

#username is in this style: XXXX#### where XXXX = first 4 letters of last name, and #### = last 4 numbers of EMPLID
#password is your EMPLID

import mysql.connector
from mysql.connector import errorcode

def showCashiers(cursor):
    query = ("SELECT * FROM Cashier;")
    cursor.execute(query)
    result = cursor.fetchall()

    #Print number and name
    for row in result:
        print(row[0], row[1])

    #Print entire row
    for row in result:
        print(row)
    return cursor


#Does not work
'''def createManager(cursor):
    query = ("INSERT INTO Manager (employeeID, Name, Pin) VALUES (1, 'Andrew Truett', 1234);")
    cursor.execute(query)
    return cursor
'''

config = {
    "user": '***',
    "password": '***',
    "host": '127.0.0.1',
    "port": '9999',
    "database": 'JCS18336AFT'
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

cursor = showCashiers(cursor)
cursor.close()
cnx.close()


'''
def create_random_date():
    return datetime.date(
            random.randint(2000, 2017), # Year
            random.randint(1, 12),      # Month
            random.randint(1, 28))      # Day

def create_random_name():
    last = ("Turing", "Church", "Curry", "Hopper", "Lovelace", "Derp")
    first = ("Allan", "Haskell", "Alonzo", "Grace", "Ada", "Emily")
    return " ".join((random.choice(first), random.choice(last)))

def create_random_record(num):
    for i in range(num):
        name = create_random_name()
        date = create_random_date()
        yield (name, date)

def query(cursor):
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    query = ("SELECT Name, EmplId, HireDate FROM Test;")
    cursor.execute(query)
    print("*" * 80)
    for (name, emplid, date) in cursor:
        print(f"{emplid} : {name}, {date}")
    print("*" * 80)

def create(cursor):
    for info in create_random_record(10):
        query = "INSERT INTO Test (Name, HireDate) VALUES (%s, %s);"
        cursor.execute(query, info)

def main():
    if len(sys.argv) != 2 or sys.argv[1] not in {"create", "query"}:
        print(f"USAGE: {sys.argv[0]} (create|query)")
        sys.exit(-1)

    try:
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
        if sys.argv[1] == "create":
            create(cursor)
            # Make sure data is committed to the database
            cnx.commit()
        else:
            query(cursor)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()

if __name__ == '__main__':
    main()
'''
