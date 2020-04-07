#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import pymysql as my

def open_mysql_connection(host, port, user, password, database):
    try:
        cnx = my.connect(host=host, port=port, user=user, password=password, db=database)
        return cnx
    except Exception as err:
        print(err)
        return -1

def close_mysql_connection(cnx):
    cnx.close()

def use_database(cnx, database):
    c = cnx.cursor()
    try:
        c.execute("use {}".format(database))
        return 0
    except Exception as err:
        print(err)
        c.close()
        return -1

if __name__ == '__main__':
    cnx = open_mysql_connection("192.168.56.103", 3323, "root", "root", "test")
    # execute(cnx, "create database test1")
    # use_database(cnx, "test")
    c = cnx.cursor()
    c.execute("select * from test1")
    data = c.fetchall()
    print(data)
    close_mysql_connection(cnx)
