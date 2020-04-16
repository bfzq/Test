#!/bin/python3
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

def test_insert(c, start, end):
    count = start
    while count < end:
        sql = "insert into test6(a) value('{}')".format(count)
        print(sql)
        try:
            c.execute(sql)
        except Exception as err:
            print(err)
            exit(1)
        count += 1

if __name__ == '__main__':
    cnx = open_mysql_connection("192.168.56.103", 3323, "root", "root", "test")
    cnx.autocommit(1)
    c = cnx.cursor()
    c.execute("truncate table test6")
    test_insert(c, 0, 100)
    c.execute("truncate table test6")
    test_insert(c, 11,150)
    c.close()
    close_mysql_connection(cnx)
