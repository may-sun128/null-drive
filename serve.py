#!/usr/bin/python
import os 
import sys
import logging
import getpass
import getopt
import jinja2 
import commandbuilder
import htmlgenerator


# Logging
logging.basicConfig(level=logging.DEBUG)

def set_working_directory():
	if len(sys.argv) == 2:
		os.chdir(sys.argv[1])
	else:
		print('Null Drive serving working directory.')

def get_server_command():
	argv = sys.argv[1:]
	opts, args = getopt.getopt(argv, "s:d:a:o:p", ["server=", "directory=", "authentication=", "domain=", "port="])
	conn = commandbuilder.serve_command()
	for opt, arg in opts:
		if opt in ('-s', '--server'):
			conn.server = arg 
		elif opt in ("-d", "--directory"):
			conn.serving_directory = arg
		elif opt in ("-a", "--authentication"):
			conn.authentication = arg
		elif opt in ("-o", "--domain"):
			conn.domain = arg
		elif opt in ("-p", "--port"):
			conn.port= arg
	return conn 


# set credentials for access to server
def get_credentials():
	print('Enter the username and password you would like to use for access to server.')
	username = input('<Username> ')
	password = getpass.getpass('<Password:> ')
	return username, password

def main():
	# set_working_directory()

	gen = htmlgenerator.HTMLGenerator()
	html = gen.render_output(os.getcwd())
	with open('index.html', 'w') as f:
		f.write(html)

	conn = get_server_command()
	username, password = get_credentials()
	c = conn.get_connection_string(username, password)
	logging.debug(c)
	# Node.JS server command
	# start_srvr_cmd: str = f'http-server -p {port} --username={username} --password={password}'

	# start server
	os.system(c)

	# remove html after server stops
	os.system('rm index.html')



# debug()
main()
