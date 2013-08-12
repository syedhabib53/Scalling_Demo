#!/usr/bin/env python

import pymysql as mdb
from params import *

def connect_db():
    conn = mdb.connect(MYSQL_HOST, MYSQL_USERNAME, MYSQL_PWD, MYSQL_DB,
                       connect_timeout=10)
    return conn

def execute_query(query):
    conn = connect_db()
    with conn:
        cur = conn.cursor()
        cur.execute(query)
        return cur

def create_database():
    query = "create database testdb;"
    return execute_query(query)

def create_contact_table():
    query = "create table contact(id int primary key AUTO_INCREMENT,\
            Name varchar(25), EmailID varchar(25), Ph varchar(13),\
            Query varchar(50));"
    return execute_query(query)
