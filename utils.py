#!/usr/bin/env python

from dbapi import *
import logging

logging.getLogger(__name__)

class ContactData(object):
    
    def insert_contact(self, name, email, phno, summary):
        query = "insert into contact values\
                ('', '"+name+"', '"+email+"', '"+phno+"',\
                '"+summary+"');"
        return execute_query(query)
    
    def get_contacts(self, offset):
        query = "select * from contact limit "+str(DATA_LIMIT)+" offset "+str(offset)+";"
        return execute_query(query)
    
    def get_contacts_count(self):
        query = "select count(*) from contact;"
        return (execute_query(query)).fetchone()[0]
    
    
    
