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
		
		<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
		
		</head>
		"""

		# Opening body tag 
		self.body_open = """
		<body>
		"""
		# Components to be dynamically 
		self.links: str = ''

		self.body_close ="""
		</body>
		</html>"""

	# Dynamically add HTML elements based on the files in the working directory 
	def generate_html(self):
		for file in self.files:
			# links
			# self.links += f'\t\t<a href="{file}">{file}</a><br>\n'
			# videos
			if any(s in file for s in ('.mp4', '.avi')):
				self.links += f'<h2>{file}</h2><br>'
				self.links += f'\t\t<video width="640" height="480" src="{file}" controls></video><br>\n'
			# images
			elif any(s in file for s in ('.jpg', '.png')):
				# self.links += f'<h2>{file}</h2><br>'
				# self.links += f' <img class="img-responsive" src="{file}" alt="Chania"> <br>'
				self.links += f"""
				<div class="w3-card-4" style="width:50%">
    				<img src="{file}" alt="{file}" style="width:100%">
    				<div class="w3-container w3-center">
      					<p>{file}</p>
    				</div>
  				</div>"""
			# text
			elif any(s in file for s in ('.txt', '.note')):
				with open(file) as f:
					text = f.read()
				self.links += f'<code>{text}</code><br>'

	# Get combined HTML elements
	def get_html(self):
		html: str = self.head + self.body_open + self.links + self.body_close
		return html

	# Write HTML to temporary index file
	def write_html_to_file(self):
		with open('index.html', 'w') as html_file:
			html_file.write(self.get_html())

	# Remove temporary index file 
	def remove_html(self):
		os.system('rm index.html')