#!/usr/bin/python

import os 
import sys
import logging
import nulltml

# Logging
logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(filename='/home/mholmes/python/null-drive/null-drive.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# TODO make this more sophisticated 
def get_env():
	if not sys.argv[1]:
		os.chdir(sys.argv[1])
	else:
		print('Please pass path to program.')

def main():
	get_env()
	# logging.warning()

	# get nulltml object 
	nhtml = nulltml.nulltml()
	# programatically get html from director
	# TODO do this in an html initialize function 
	nhtml.generate_html()

	# write html to temporary index file 
	nhtml.write_html_to_file()

	# Node.JS server command
	start_srvr_cmd: str = 'http-server -p 8000'

	# start server
	os.system(start_srvr_cmd)

	# remove html after server stops
	nhtml.remove_html()

	logging.debug(nhtml.get_html())


main()
# debug()