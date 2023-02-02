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

def parse_args():
	argv = sys.argv[1:]
	opts, args = getopt.getopt(argv, "s:d:a:o:p", ["server=", "directory=", "authentication=", "domain=", "port="])
	cb = commandbuilder.CommandBuilder()
	for opt, arg in opts:
		if opt in ('-s', '--server'):
			cb.server = arg 
		elif opt in ("-d", "--directory"):
			cb.serving_directory = os.path.abspath(os.path.expanduser(arg))
		elif opt in ("-a", "--authentication"):
			cb.authentication = arg
		elif opt in ("-o", "--domain"):
			cb.domain = arg
		elif opt in ("-p", "--port"):
			cb.port= arg
	return cb 

# set credentials for access to server
def get_credentials():
	print('Enter the username and password you would like to use for access to server.')
	username = input('<Username> ')
	password = getpass.getpass('<Password:> ')
	return username, password

def main():
	command_builder = parse_args()
	os.chdir(command_builder.serving_directory)

	gen = htmlgenerator.HTMLGenerator()
	html = gen.render_output(os.getcwd())
	with open('index.html', 'w') as f:
		f.write(html)

	username, password = get_credentials()
	command = command_builder.get_server_command(username, password)

	# start server
	os.system(command)

	# remove html after server stops
	os.system('rm index.html')



# debug()
main()
