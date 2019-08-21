def hello():
	'''This function does not take any arguments
	and it does not return any value.
	It prints Hello World'''
	print("Hello World!")

help(hello)


def hello_world(name):
	'''This function take a single string argument
	and it does not return any value.
	It prints Hello World from {argument}'''
	print(f'Hello World from {name}')


def add(a, b):
	'''This function take two argument and
	returns the sum of them'''
	return a + b

sum = add(10, 5)
sum			#displays 15


def add_minus(a, b):
	'''This function take two argument and
	returns the sum and difference of them'''
	return a + b, a - b

sum, diff = add_minus(5, 2)
sum			#display2 7
diff			#displays 2
