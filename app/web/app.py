# encoding:utf-8
from flask import Flask, abort, request, jsonify 
from flask import render_template
from flask import make_response
from flask_cors import CORS, cross_origin
import pymysql
import requests
import json
import os
import subprocess

#SERVERFUL_DB_HOST = os.environ['SERVERFUL_DB_HOST']
#SERVERFUL_DB_USER = os.environ['SERVERFUL_DB_USER']
#SERVERFUL_DB_PASS = os.environ['SERVERFUL_DB_PASS']
#SERVERFUL_DB_NAME = os.environ['SERVERFUL_DB_NAME']
    
#db = pymysql.connect(SERVERFUL_DB_HOST, SERVERFUL_DB_USER, SERVERFUL_DB_PASS, SERVERFUL_DB_NAME, autocommit=True)

app = Flask(__name__,
            static_url_path='', 
            static_folder='static')

app.debug = True

cors = CORS(app)

@app.route('/health', methods=['GET'])
def health():
    return 'OK'

@app.route('/globe', methods=['GET'])
def fraudreport():
    return render_template('index.html')

@app.route('/version', methods=['GET'])
def version():
    return '2.4'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')