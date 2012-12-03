#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, g
from contextlib import closing
import os
import sqlite3
import database

#=======------ config ------=================
DATABASE     = os.path.join(os.path.dirname(__file__),'pinziyuan.db')
DEBUG        = True
SECRET_KEY   = 'development key'
MYSQL_HOST   = 'localhost'
MYSQL_DB     = 'pinziyuan'
MYSQL_USER   = 'root'
MYSQL_PASSWD = '5650268'
# USERNAME = 'admin'
# PASSWORD = 'default'

#============================================
app = Flask(__name__)
app.config.from_object(__name__)

#============数据库连接====================
def connect_db():
	return database.Connection(app.config['MYSQL_HOST'],app.config['MYSQL_DB'],app.config['MYSQL_USER'],app.config['MYSQL_PASSWD'])

def init_db():
	with closing(connect_db) as db:
		with app.open_resource('pinziyuan.sql') as f:
			db._execute(f.read())
@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
	g.db.close()
#==========================================

@app.route('/')
def index():
	# sql ="select * from ziyuan where `title` like '%s%' " %'python'
	like = '%' + '微软' + '%'
	sql = '''select * from ziyuan where `title` like `%s%%` '''%('python')
	import time
	t = time.time()
	cur = g.db.query('''select * from ziyuan where `title` like %s ''',('%音乐%'))
	# cur = None
	t2 = time.time()
	return render_template('index.html',cur = cur,t = t2-t,sql = sql,num = len(cur))

if __name__ == '__main__':
	app.run()