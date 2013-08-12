#!/usr/bin/env python

from flask import Flask, request, render_template, url_for, flash
from dbapi import *
from utils import ContactData
import os
import logging

app = Flask(__name__)
contact_data = ContactData()
path = os.path.dirname(os.path.abspath(__file__))
logging.basicConfig(filename=path+'/scalling.log', level=logging.DEBUG,
                    format='%(asctime)s %(message)s')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')
    elif request.method=='POST':
        name = str(request.form['name'])
        email = str(request.form['email'])
        phno = str(request.form['phno'])
        summary = str(request.form['query'])
        
        contact_data.insert_contact(name, email, phno, summary)
        logging.info("Data Inserted")
        flash('Information Sent Successfully', 'success')
        return render_template('index.html')


@app.route('/data/', methods=['GET'])
@app.route('/data/<page>', methods=['GET'])
def data(page=0):
    page = int(page)
    contact_count = contact_data.get_contacts_count()
    if page>=0:
        offset = ((contact_count - (contact_count%DATA_LIMIT))) - (page*DATA_LIMIT)
    else:
        page = contact_count/50
        offset = 0
    if offset<0:
        offset = 0
    result = contact_data.get_contacts(offset)
    result = list(result.fetchall())
    result.reverse()
    return render_template('data.html', data=result, page=page,
                           offset=offset)

app.secret_key = os.urandom(24)
