import os

class CommandBuilder:
	def __init__(self):
		self.port = '8000'
		self.authentication = False 
		self.server = 'python'
		self.serving_directory = os.getcwd()
		self.domain = None
		self.serve_command = ''

	def get_server_command(self, username, password):
		command = ''
		if self.server == 'python':
			self.serve_command = 'python -m http.server'
			# If the server is python, no other arguments are applicable; exit 
			return self.serve_command
		elif self.server == 'node':
			self.serve_command = 'http-server'
		else:
			print('Invalid server command.')
		# directory
		self.serve_command += f' {self.serving_directory}'
		# port
		self.serve_command += f' -p {self.port}'
		# if there's authentication
		if self.authentication:
			self.serve_command += f' --username={username} --password={password}'
		# if there's a domain
		if self.domain:
			self.serve_command += f'-a {self.domain}'
		return self.serve_command


