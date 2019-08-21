colors = ['red', 'orange', 'yellow', 'green', 'blue']

for color in colors:
  print(color)
  

for color in reversed(colors):
  print(color)
  
for color in sorted(colors):
  print(color)
 
for i, color in enumerate(colors):
  print(f'{i} --> {color}')
  
numbers = [1, 2, 3, 4, 5]
for number, color in zip(numbers, colors):
  print(f'{number} --> {color}')

services = {'ftp': 21, 'ssh': 22, 'smtp': 25, 'http': 80, 'pop3': 110, 'imap': 220, 'https': 443}
#for loop
for key in services:
	print(key)

  
for key, value in services.items():
  print(key, value)
