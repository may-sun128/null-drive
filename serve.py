#!/usr/bin/python

import os 
import sys
import logging
import getpass
import getopt

import nulltml
import nullss
import command_builder

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
	conn = command_builder.serve_command()
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
	set_working_directory()

	# get null html object 
	nhtml = nulltml.nulltml()
	# get null css object 
	nss = nullss.nullss()

	# programatically get html from director
	# TODO do this in an html initialize function 
	nhtml.generate_html()

	# write html to temporary index file 
	nhtml.write_html_to_file() 
	nss.write_css_to_file()

	# domain = 'midnight.home'
	# port = '8000'
	conn = get_server_command()
	username, password = get_credentials()
	c = conn.get_connection_string(username, password)

	# Node.JS server command
	# start_srvr_cmd: str = f'http-server -p {port} --username={username} --password={password}'

	# start server
	os.system(c)

	# remove html after server stops
	nhtml.remove_html()
	nss.remove_css()

def debug():
	conn = get_server_command()
	username, password = get_credentials()
	s = conn.get_connection_string(username, password)
	print(s)

# debug()
main()
