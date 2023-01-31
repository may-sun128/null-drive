import os

class connection_string:
	def __init__(self):
		self.port = '8000'
		self.authentication = False 
		self.server = 'python'
		self.serving_directory = os.getcwd()
		self.domain = None
		self.serve_command = ''

	def get_connection_string(self, username, password):
		command = ''
		if self.server == 'python':
			self.serve_command = 'python3 -m http.server'
			# If the server is python, no other arguments are applicable; exit 
			return self.serve_command
		elif self.server == 'node':
			self.serve_command = 'http-server'
		else:
			print('Invalid server command.')
		# port if node 
		command += f'-p {self.port}'
		if self.authentication:
			command += f'--username {username} --password={password}'
		if self.domain:
			command += f'-a {self.domain}'


# start_srvr_cmd: str = f'http-server -p {port} --username={username} --password={password}'

# c = connection_string()
# print(c.get_connection_string('admin', 'password'))
