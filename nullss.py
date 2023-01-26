#!/usr/bin/python

import os

class nullss:
	def __init__(self):
		self.all = """
		h2, a, code, video {
			padding-top: 10px;
  			padding-right: 10px;
  			padding-bottom: 10px;
  			padding-left: 10px;
		}
		"""

	def write_css_to_file(self):
		with open('style.css', 'w') as f:
			f.write(self.all)

	def remove_css(self):
		os.system('rm style.css')


"""
*Example* 

p {
	color: red, 
	text-align: center
}
"""