#!/usr/bin/python

import os
import logging

logging.basicConfig(level=logging.DEBUG)

class nulltml:
	def __init__(self):
		# Files to be Served
		self.files: list[str] = os.listdir() 
		# HTML Components 
		self.head: str ="""
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

		self.body_open = """
		<body>
		"""

		self.jumbotron = """
		<!-- Jumbotron -->
		<div class="jumbotron text-center">
		<h1>Not Google Drive</h1>
		<a href="">GitHub</a>
		</div>\n"""

		self.links: str = ''

		self.body_close ="""
		</body>
		</html>"""

	def generate_html(self):
		for file in self.files:
			if any(s in file for s in ('.mp4', '.aif')):
				self.links += f'<h2>{file}</h2><br>'
				self.links += f'\t\t<video width="640" height="480" src="{file}" controls></video><br>\n'
			# elif '.jpg' in file:
			elif any(s in file for s in ('.jpg', '.png')):
				self.links += f'<h2>{file}</h2><br>'
				self.links += f' <img class="img-responsive" src="{file}" alt="Chania"> <br>'
			self.links += f'\t\t<a href="{file}">{file}</a><br>\n'

	def get_html(self):
		html: str = self.head + self.body_open + self.jumbotron + self.links + self.body_close
		return html

	def write_html_to_file(self):
		with open('index.html', 'w') as html_file:
			html_file.write(self.get_html())

	def remove_html(self):
		os.system('rm index.html')