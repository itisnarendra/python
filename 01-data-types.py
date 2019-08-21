##Python data type - None
a = None
type(a)

##Python data type - Numeric (int)
ftp = 0b10101		#binary number
ssh = 0o26		#octal number
sntp = 25		#decimal number
http = 0x50		#hexadecimal number
ftp
type(ftp)

##Python data type - Numeric (float)
earth = 5.972e24	#mass of earth in kg
proton = 1.6726e-27	#mass of a proton in kg
type(earth)

##Python data type - Numeric (Bool)
is_married = True	
is_fulltime = False
type(is_married)

##Python data type - String (you may use single, double or triple quotes for delimiters)
name = 'narendra pershad'
type(name)
#a string can be treated as an sequence of letters
name[2]
name[2:]
name[:2]
name[2:5]
name *= 2

##Python data type - String (byte)
note = f'ftp works on port {ftp}
pm = b'Justin Trudeau'	#another byte string
print(pm)
type(pm)
pm[1]
type(pm[1])
chr(117)		#converts the int argument to the ascii letter
ord('u')		#converts the string argument to a number
pm[3:]
type(pm[3:])

##Python data type - Sequence (list)
colors = list(('red','orange','yellow','green','blue'))	#using the list constructor
presidents = ['obama', 'bush', 'clinton', 'reagan', 'carter']
presidents
print(presidents)
type(presidents)
#provides help on the functions associated with presidents
help(presidents)
presidents[-1] = 'trump'	#replaces the last item
presidents.insert(0, 'biden')	#inserts at the begining of the list
presidents.pop()		#removes the first one

##Python data type - Sequence (dictionary)
services = {'ftp': 21, 'ssh': 22, 'smtp': 25, 'http': 80, 'pop3': 110, 'imap': 220, 'https': 443}
services
type(services)
#for loop
for key in services:
	print(key)

for key in services:
	print(key, services[key])

services['smtp'] = 336		#adds a new key-value pair to services
