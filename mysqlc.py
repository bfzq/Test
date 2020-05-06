#!/usr/local/bin/python

import pymysql as mysql

def open_mysql_connection(host, port, user, passwd, database):
  try:
    cnx = mysql.connect(host=host, user=user, password=passwd, port=port, db=database)
    return cnx
  except Exception as err:
    print(err)
    exit(1)

def close_mysql_connection(cnx):
  cnx.close()

def use_database(cnx, DB_NAME):
  cursor = cnx.cursor()
  try:
    cursor.execute("use {}".format(DB_NAME))
  except Exception as err:
    print(err)
  cursor.close()

def execute(cnx, sql):
  cursor = cnx.cursor()
  try:
    cursor.execute(sql)
  except Exception as err:
    print(err)
  cursor.close()

def last_insert_id(cnx):
  cursor = cnx.cursor()
  try:
    cursor.execute("SELECT LAST_INSERT_ID()")
    for row in cursor:
      return row[0]
  except Exception as err:
    print(err)
  cursor.close()
  return -1

def query(cnx, sql):
  cursor = cnx.cursor()
  data = []
  try:
    cursor.execute(sql)
    for row in cursor:
      data.append(row)
  except Exception as err:
    print(err)
  cursor.close()
  return data

# if __name__ == '__main__':
#     cnx = open_mysql_connection("127.0.0.1", 3306, "root", "1qaz2wsx")
#     # execute(cnx, "create database test1");
#     use_database(cnx, "test1")
#     # execute(cnx, "create table test3(id int)")
#     execute(cnx, "insert into test3(id) value(1111)")
#     cnx.commit()
#     data = query(cnx, "select * from test3")
#     print(data)
#     close_mysql_connection(cnx)
