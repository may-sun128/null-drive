#!/usr/bin/python

import os
import logging

logging.basicConfig(level=logging.DEBUG)

class nulltml:
	def __init__(self):
		# Files to be Served
		self.files: list[str] = os.listdir() 
		
		# HTML Components 
		
		# Head of HTML Document
		self.head: str ="""
		<!DOCTYPE html>
		<html>
		<head>
		<title>Null Drive</title>
		
		<!-- Bootstrap Stuff -->
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
		<link rel="stylesheet" href="style.css">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
		<!-- End Bootstrap Stuff -->
		
		</head>
		"""

		# Opening body tag 
		self.body_open = """
		<body>
		"""

		# Style for image thumbnails
		self.style = """<style>
		img {
		  border: 1px solid #ddd;
		  border-radius: 4px;
		  padding: 5px;
		  width: 150px;
		}

		img:hover {
		  box-shadow: 0 0 2px 1px rgba(0, 140, 186, 0.5);
		}
		</style>"""

		# Bootstrap Jumbotron
		self.jumbotron = """
		<!-- Jumbotron -->
		<div class="jumbotron text-center">
		<h1>Not Google Drive</h1>
		<a href="">GitHub</a>
		</div>\n"""

		# Components to be dynamically 
		self.links: str = ''

		self.body_close ="""
		</body>
		</html>"""

	# Dynamically add HTML elements based on the files in the working directory 
	def generate_html(self):
		for file in self.files:
			# links
			self.links += f'\t\t<a href="{file}">{file}</a><br>\n'
			# videos
			if any(s in file for s in ('.mp4', '.avi')):
				self.links += f'<h2>{file}</h2><br>'
				self.links += f'\t\t<video width="640" height="480" src="{file}" controls></video><br>\n'
			# images
			elif any(s in file for s in ('.jpg', '.png')):
				self.links += f'<h2>{file}</h2><br>'
				self.links += f' <img class="img-responsive" src="{file}" alt="Chania"> <br>'
			# text
			elif any(s in file for s in ('.txt', '.note')):
				with open(file) as f:
					text = f.read()
				self.links += f'<code>{text}</code><br>'

	# Get combined HTML elements
	def get_html(self):
		html: str = self.head + self.body_open + self.jumbotron + self.links + self.body_close
		return html

	# Write HTML to temporary index file
	def write_html_to_file(self):
		with open('index.html', 'w') as html_file:
			html_file.write(self.get_html())

	# Remove temporary index file 
	def remove_html(self):
		os.system('rm index.html')