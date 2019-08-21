##Python data type - None
a = None
type(a)

##Python data type - Numeric (int)
ftp = 0b10101		#binary number
ssh = 0o26		#octal number
sntp = 25		#decimal number
http = 0x50		#hexadecimal number

##Python data type - Numeric (float)
earth = 5.972e24	#mass of earth in kg
proton = 1.6726e-27	#mass of a proton in kg

##Python data type - Numeric (Bool)
is_married = True	
proton = 1.6726e-27	



name = 'narendra pershad'
#a string can be treated as an array of letters
name[2]
name[2:]
name[:2]
name[2:5]
name *= 2

note = f'ftp workd on port {ftp}'
note


pm = b'Justin Trudeau'
print(pm)
type(pm)
pm[1]
type(pm[1])
chr(117)
ord('u')
pm[3:]
type(pm[3:])


friends = ['obama', 'bush', 'clinton', 'reagan', 'carter']
friends
print(friends)
type(friends)
friends[-1] = 'ford'
#provides help on the functions associated with friends
help(friends)
friends.insert(0, 'trump')
friends.pop()

services = {'ftp': 21, 'ssh': 22, 'smtp': 25, 'http': 80, 'pop3': 110, 'imap': 220, 'https': 443}

services
type(services)
#for loop
for key in services:
	print(key)

for key in services:
	print(key, services[key])

services['smtp'] = 336


def hello():
	'''prints hello world'''
	print("Hello World!")

def hello_world(name):
	'''prints hello world'''
	print('Hello World from', name)

def sum(a, b):
	'''a function to add two numbers'''
	return a + b
