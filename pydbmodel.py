"""
    PyDbModel: A class to manipulate SQL Databases.
    Copyright (C) 2016 Leandro Israel Pinto

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
	
	CONTACT:
	Email: leandro.israel.p@gmail.com
	Another Email: contato@leandroip.com
	Site: leandroip.com

"""
VERSION = '1.0'

#Can configure it in code, before instantiate any Model().
HOST=''
USER=''
PWD=''
DATABASE=''
DB_TYPE=''  #MYSQL, SQLITE3


def config_sqlite(db):
	global DATABASE, DB_TYPE
	DATABASE = db
	DB_TYPE = 'SQLITE3'
	
	
def config_mysql(host,user,pwd,database):
	global HOST,USER,PWD,DATABASE,DB_TYPE
	HOST = host
	USER = user
	PWD = pwd
	DATABASE = database
	DB_TYPE = 'MYSQL'
	
	

"""
if DB_TYPE == 'MYSQL':
	import MySQLdb as mysql
elif DB_TYPE == 'SQLITE3':
	import sqlite3 as mysql
else:
	print "Error on set database type."
	exit()
"""

import datetime
import random





con = None
dcur = None

class Model:
	_prop = {"id":None}
	name=''
	table=''
	def __init__(self,table,createid=False):
		global con,dcur		
		self._prop = {"id":None}		
		self.table = table
		self.createid = createid
		
		if DB_TYPE == 'MYSQL':
			import MySQLdb as mysql
		elif DB_TYPE == 'SQLITE3':
			import sqlite3 as mysql
		else:
			print "Error on set database type."
			exit()

		if DB_TYPE == 'MYSQL':
			if(con==None or not con.open):
				con = mysql.connect(HOST, USER, PWD)
				con.select_db(DATABASE)
				dcur = con.cursor(mysql.cursors.DictCursor)
		elif DB_TYPE == 'SQLITE3':
			if(con==None):
				con = mysql.connect(DATABASE)
				dcur = con.cursor()
		
	def set(self, att, val):
		self._prop[att] = val
		
	def get(self, att):
		return self._prop[att]
		
	def get2(self, att):
		if not att in self._prop:
			return ''
		return str(self._prop[att])
	

	def resToDict(self, r, names):
		ret = []
		for l in r:
			di = {}
			i = 0
			for n in names:
				di[n] = l[i]
				i = i + 1
			ret.append(di)
		return ret
				
	
	def load(self, id):
		global dcur
		l = dcur.execute('select * from %s where id="%s"' %(self.table,id))	
		if DB_TYPE == 'MYSQL':
			self._prop = dcur.fetchallDict()[0]
		elif DB_TYPE == 'SQLITE3':
			names = [d[0] for d in l.description]
			self._prop = self.resToDict([dcur.fetchall()[0]],names)[0]
		else:
			print "ERR DB  not set"
			exit()
		
	def query(self, sql):
		global dcur, con
		#con.begin()
		l = dcur.execute(sql)
		con.commit()
		if DB_TYPE == 'MYSQL':
			return dcur.fetchallDict()
		elif DB_TYPE == 'SQLITE3':
			if(l == None or l.description==None):
				return None
			names = [d[0] for d in l.description]
			return self.resToDict(dcur.fetchall(),names)
		else:
			print "ERR DB  not set"
			exit()
		return None
		
	def setAll(self, prop):
		self._prop = prop.copy()
	def getAll(self):
		return self._prop
	
	def persist(self, onlysql=False):
		cols = ''
		vals = ''
		sql = ''
		getid=False
		if(self._prop["id"] == None or self._prop["id"] == ''):
			d = datetime.datetime.now()
			dstr = d.strftime('%Y%m%d%H%M%S')
			if self.createid:
				self._prop["id"] = "%s%04d" % (dstr, random.randint(0,9999))
			else:
				del self._prop["id"]
			for p in self._prop:
				cols = cols + ',' + p
				vals = vals + ',\'' + str(self._prop[p])+'\''
				
			cols=cols[1:]
			vals = vals[1:]				
			
			sql = "insert into %s(%s) values(%s)" %(self.table, cols, vals)
			getid=True
			#import jnatui as tui
			#tui.dia_ok(sql)
		else:
			vals = ''
			for p in self._prop:
				vals = vals + ", %s = \"%s\"" % (p, self._prop[p])				
				
			vals = vals[1:]
			sql = "update %s set %s where id = '%s'" %(self.table, vals, self._prop["id"])
		
		#print sql
		r = self.query(sql)
		#if(getid):
		#	self._prop["id"] = self.query("select LAST_INSERT_ID() as id")[0]["id"]
		#if(onlysql):
		#	return sql
		
		return r
		#return sql
		
	def select(self, where=None, order=None, start=None, count=None):
		first = True
		table = self.table
		if(order != None):
			order = "order by "+order
			
		w = ''
		if(where !=None):
			for (k,v) in where:
				if(first):
					w = k + '=' + '\"' + v + '\"'
					first = false
				else:
					w = w + " AND "+k+'='+'\"'  + v + '\"'
					
		if(where == None):
			sql = "SELECT * FROM %s %s" % (table, order)
		else:
			sql = "select * from %s where %s %s" % (table, w, order)
		
		if(count !=None):
			sql = sql + " limit %d, %d" % (start,count)
			
		return self.query(sql)
	
	def search_match(self, terms, onCols, where= None, start = None, count = None):
		pass
	
	def search(self, terms, onCols, where= None, start = None, count = None):
		first = True
		table = self.table
		w = ''
		
		if(terms == None):
			return None
		term = terms.split(' ')
		if(where != None):
			for (k,v) in where:
				if(first):
					w = k + '=' + '\"' + v + '\"'
					first = False
				else:
					w = w + " AND " + k + "=" + "\"" + v + "\"";
		if(where == None):
			sql = "SELECT * FROM "+table
		else:
			sql = "SELECT *  FROM %s WHERE %s" % (table,w)
			
		s = ''
		first = True
		
		for v in onCols:
			for m in term:
				if(first):
					s = "%s %s LIKE '%%%s%%' " % (s,v,m)
					first = False
                else:
                    s = s+" OR %s LIKE '%%%s%%' " % (v,m)
					
		if(s != ''):	
			if(where == None):
				sql = sql + " WHERE "+s
			else:
				sql = sql + " AND(%s) " %(s)
				
		if(count != None):
			sql = sql + " limit %d, %d" % (start, count)
			
		#print sql
		#exit()
		return self.query(sql)			
					
	def delete(self, id=None):
		if(id == None):
			sql = "delete from " + self.table + " where id='" + str(self._prop["id"]) + "'"
		else:
			sql = "delete from " + self.table + " where id='" + str(id) + "'"
		return self.query(sql);
	
	
	
	
