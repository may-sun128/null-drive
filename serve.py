#!/usr/bin/python

import os 
import sys
import logging
import getpass

import nulltml
import nullss

# Logging
logging.basicConfig(level=logging.DEBUG)

def get_env():
	if len(sys.argv) == 2:
		os.chdir(sys.argv[1])
	else:
		print('Null Drive serving working directory.')

# set credentials for access to server
def get_credentials():
	print('Enter the username and password you would like to use for access to server.')
	username = input('<Username> ')
	password = getpass.getpass('<Password:> ')
	return username, password

def main():
	get_env()

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

	domain = 'midnight.home'
	port = '8000'
	username, password = get_credentials()

	# Node.JS server command
	start_srvr_cmd: str = f'http-server -p {port} --username={username} --password={password} -a {domain}'

	# start server
	os.system(start_srvr_cmd)

	# remove html after server stops
	nhtml.remove_html()
	nss.remove_css()

main()