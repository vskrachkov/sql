import pymysql as msql
from config import BankDatabase, TestDatabase


con_bank = msql.connect(host=BankDatabase.HOST,
						port=BankDatabase.PORT, 
						user=BankDatabase.USER, 
						password=BankDatabase.PASSWORD, 
						db=BankDatabase.DATABASE)
con_test = msql.connect(host=TestDatabase.HOST,
						port=TestDatabase.PORT, 
						user=TestDatabase.USER, 
						password=TestDatabase.PASSWORD, 
						db=TestDatabase.DATABASE)

def ex(sql, con_name=None, *sql_params):
	"""Executes sql expression.
	Params::
		:sql: sql expression;
		:sql_params: optional positional parameters that will 
			be passed to sql expression.
	"""
	if con_name == 'bank':
		with con_bank.cursor() as cur:
			cur.execute(sql, sql_params)
			return cur.fetchall()
	else:
		with con_test.cursor() as cur:
			cur.execute(sql, sql_params)
			return cur.fetchall()


def exl(sql, *sql_params):
	"""Executes sql expresion and print results in userfriendly form."""
	for doc in ex(sql, *sql_params):
		print(doc)
