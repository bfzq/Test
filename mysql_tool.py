#!/usr/bin/python3

import mysql.connector
from mysql.connector import errorcode

def open_mysql_connection(host, port, user, passwd):
    try:
        cnx = mysql.connector.connect(host=host, user=user,
                                    password=passwd, port=port)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database dos not exist")
        else:
            print(err)
    else:
        cnx.close()
    return cnx

def close_mysql_connection(cnx):
    cnx.close()

def use_database(cnx, DB_NAME):
    cursor = cnx.cursor()
    try:
        cursor.execute("use {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Database {} does not exists.".format(DB_NAME))
    else:
        print(err)
        exit(1)

def execute(cnx, sql):
    cursor = cnx.cursor()
    try:
        cursor.execute(sql)
    except mysql.connector.Error as err:
        print(err)
    
if __name__ == '__main__':
    cnx = open_mysql_connection("192.168.56.103", 3323, "root", "root")
    use_database(cnx, "test")
    execute(cnx, "insert into test3(id) value(1111)")
    close_mysql_connection(cnx)
