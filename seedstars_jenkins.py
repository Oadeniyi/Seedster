import jenkins
import sqlite3
import sys
from datetime import datetime,date


#url = sys.argv[1]
url = input('Please enter the JekinsURL here:')
#usr = sys.argv[2]
usr = input('Username:')
#pwd = sys.argv[3]
pwd = input('Password:')

def populate_target(jenkinsurl, user, pss):
	server = jenkins.Jenkins(jenkinsurl, username=user, password=pss)
	try:
		conn = sqlite3.connect('seedstars.db')
		c = conn.cursor()
		sql_cmd1 = '''create table Jobs_status_time (job text, status text, timestamp text)'''
		c.execute(sql_cmd1)
		jobs = server.get_jobs()
		for job in jobs:
			if "result" in job.keys():
				name = job['name']
				status = jobs['result']
				time = datetime.strftime(datetime.now(),"%Y%m%d %H:%M:%S") 
				print(name,status,time)
				c.execute("""insert into Jobs_status_time('job', 'status', 'timestamp') values(?,?,?)""",(name, status, time))
				conn.commit()
			else:
				name = job['name']
				time = datetime.strftime(datetime.now(),"%Y%m%d %H:%M:%S") 
				print(name,time)
				c.execute("""insert into Jobs_status_time('job', 'timestamp') values(?,?)""",(name, time))
				conn.commit()
				print('Job has no status')
	except sqlite3.Error:
		print('table already exist..')
		conn = sqlite3.connect('seedstars.db')
		c = conn.cursor()
		jobs = server.get_jobs()
		for job in jobs:
			if "result" in job.keys():
				name = job['name']
				status = jobs['result']
				time = datetime.strftime(datetime.now(),"%Y%m%d %H:%M:%S") 
				print(name,status,time)
				c.execute("""insert into Jobs_status_time('job', 'status', 'timestamp') values(?,?,?)""",(name, status, time))
				conn.commit()
			else:
				name = job['name']
				time = datetime.strftime(datetime.now(),"%Y%m%d %H:%M:%S") 
				print(name,time)
				c.execute("""insert into Jobs_status_time('job', 'timestamp') values(?,?)""",(name, time))
				conn.commit()
				print('Job has no status')
	
if __name__ == '__main__':
	populate_target(url, usr, pwd)
# connt = sqlite3.connect('seedstars.db')
# c = connt.cursor()
# c.execute('select * from Jobs_status_time')
# rows = c.fetchall()
# for i in rows:
# 	print(i)