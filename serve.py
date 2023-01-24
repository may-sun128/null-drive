#!/usr/bin/python

import os 
import sys
import logging

# Logging
logging.basicConfig(level=logging.DEBUG)
# logging.basicConfig(filename='null-drive.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def generate_html():
	# Files to be Served
	files: list[str] = os.listdir() 
	# HTML Components 
	head: str ="""
	<!DOCTYPE html>
	<html>
	<head>
	<title>Null Drive</title>
	
	<!-- Bootstrap Stuff -->
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
	<!-- End Bootstrap Stuff -->
	
	</head>
	"""

	jumbotron = """
	<!-- Jumbotron -->
	<div class="jumbotron text-center">
	<h1>Null Drive</h1>
	<a href="">GitHub</a>
	</div>"""

	body_open = """
	<body>
	"""

	links: str = ''

	body_close ="""
	</body>
	</html>"""

	for file in files:
		if '.mp4' in file:
			links +=f'\t<video width="640" height="480" src="{file}" controls>\n'
		else:
			links += f'\t<a href="{file}">{file}</a><br>\n'

	html: str = head + body_open + jumbotron + links + body_close

	return html

def write_html_to_file(html: str):
	with open('index.html', 'w') as html_file:
		html_file.write(html)

# TODO make this more sophisticated 
def get_env():
	if not sys.argv[1]:
		os.chdir(sys.argv[1])

def main():
	get_env()
	# logging.warning()

	# get html 
	html = generate_html()

	write_html_to_file(html)

	# Node.JS server command
	start_srvr_cmd: str = 'http-server -p 8000'

	# start server
	os.system(start_srvr_cmd)

	# remove html after server stops
	os.remove('index.html')

	logging.warning('is this working or not')
	logging.warning(html)

def debug():
	# get html 
	html = generate_html()
	logging.debug(html)

	# write_html_to_file(html)

	# Node.JS server command
	# start_srvr_cmd: str = 'http-server -p 8000'

	# start server
	# os.system(start_srvr_cmd)

	# remove html after server stops
	# os.remove('index.html')

main()
# debug()