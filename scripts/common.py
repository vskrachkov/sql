import pymysql as msql
from config import BankDatabase, TestDatabase


try:
	con_bank = msql.connect(host=BankDatabase.HOST,
				port=BankDatabase.PORT, 
				user='root', 
				password=BankDatabase.ROOT_PASSWORD, 
				db=BankDatabase.DATABASE)
	con_test = msql.connect(host=TestDatabase.HOST,
				port=TestDatabase.PORT, 
				user=TestDatabase.USER, 
				password=TestDatabase.PASSWORD, 
				db=TestDatabase.DATABASE)
except msql.err.OperationalError:
	pass


def ex_(sql, con):
	"""Execute sql expression.
	Parameters::
		:sql: sql expression;
		:con: mysql connector instance.
	"""
	try:
		with con.cursor() as cur:
			cur.execute(sql)
			return cur.fetchall()
	except Exception as err:
		return err


def ex(sql, con_name=None, *sql_params):
	"""Executes sql expression.
	Params::
	    :sql: sql expression;
	    :con_name: name of connection which will be used for 
	    	execution expresion;
	    :sql_params: optional positional parameters that will be 
	    	passed to sql expression.
	"""
	if con_name == 'bank':
		with con_bank.cursor() as cur:
			cur.execute(sql, sql_params)
			return cur.fetchall()
	else:
		with con_test.cursor() as cur:
			cur.execute(sql, sql_params)
			return cur.fetchall()


def exl(sql, con_name=None, *sql_params):
	"""Executes sql expresion and print results in userfriendly form.
	Parameters the same as in :ex: function.
	"""
	for doc in ex(sql, con_name=con_name, *sql_params):
		print(doc)


def exc(sql, con_name=None, *sql_params):
	"""Execute sql expression and commit changes. Use this function 
	for inserting or updating rows.
	"""
	exl(sql, con_name=con_name, *sql_params)
	if con_name == 'bank':
		con_bank.commit()
	else:
		con_test.commit()

if __name__ == '__main__':
	print('All tables for test database:')
	exl('show tables')
	print('All tables for bank database:')
	exl('show tables', con_name='bank')
