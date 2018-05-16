import jenkins
import sqlite3
import sys
from datetime import datetime

url = sys.argv[1]
usr = sys.argv[2]
pwd = sys.argv[3]

def populate_target(jenkinsurl, user, pss):
	try:
		server = jenkins.Jenkins(jenkinsurl, username=user, password=pss)
		conn = sqlite3.connect('seedstars.db')
		c = conn.cursor()
		sql_cmd1 = '''create table Jobs_status_time (job text, status text, timestamp time)'''
		c.execute(sql_cmd1)
	except sqlite3.Error:
		print('Table already exixts...')
	jobs = server.get_jobs()
	for job in jobs:
		if "result" in job.keys():
			name = job['name']
			status = jobs['result']
			time = datetime.now()
			print(name,status,time)
			sql_cmd = '''insert into Job_status(job, status) /nvalues({},{})'''.format(name,status,time)
			c.execute(sql_cmd)
			conn.commit()
		else:
			name = job['name']
			time = datetime.now()
			print(name,time)
			print('Job has no status')

populate_target(url, usr, pwd)