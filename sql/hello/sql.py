import mysql.connector
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user                    ='root',                                    
            password                ='password',
            database                ='mydb'
        )
        return connection
    except mysql.connector.Error as error:
        print("Error while connecting to MySQL", error)
        return None 
