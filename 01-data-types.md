
# Python has seven data types - none, numeric, sequences, mappings, classes, instances and exceptions.

## Data type - None
Similar to null in other langauges


```python
a = None
type(a)
```




    NoneType



## Python has four numeric types - bool, int, float and complex
Older implementation supported a byte data type

### Data type - bool
This is a sub-type of integer


```python
is_married = True
is_fulltime = False
print(f'Marital status: {is_married}')
type(is_married)
```

    Marital status: True





    bool



### Data type - Int
This is a number with unlimited precision


```python
ftp = 0b10101		#binary number
ssh = 0o26			#octal number
sntp = 25			#decimal number
http = 0x50			#hexadecimal number

print(f'ftp uses port {ftp}')
type(ftp)
#help(ftp)			#uncomments this line for more output

```

    ftp uses port 21





    int



### Data type - Float


```python
##Python data type - Numeric (float)
earth = 5.972e24	#mass of earth in kg
proton = 1.6726e-27	#mass of a proton in kg
print(f'Mass of the earth is {earth}kg')
type(earth)
```

    Mass of the earth 5.972e+24kg





    float



### Data type - Complex


```python
a = 3+1j
b = 5+2j

print(f'Sum is {a+b}')
print(f'Difference is {b-a}')
type(a)
```

    Sum is (8+3j)
    Difference is (2+1j)





    complex



## Data type - Sequences
There are three basic sequences - list,, tuple and range

### List are delimited by square brackets
List items does not have to be the same type


```python
#list using the constructor
services = list(('ftp', 'ssh', 'smtp', 'http'))
#list by assignment
ports = [ 21, 22, 25, 80 ]
foo = ['this', 0, 3.15, [4], "is", '''also a list''']

print(services)
print(ports)
print(foo)
type(foo)
```

    ['ftp', 'ssh', 'smtp', 'http']
    [21, 22, 25, 80]
    ['this', 0, 3.15, [4], 'is', 'also a list']





    list



#### Items are accessed via indices much like arrays




```python
ports.insert(4, 52)
services.insert(len(services), 'dns')
print(services)
print(ports)
```

    ['ftp', 'ssh', 'smtp', 'http', 'dns']
    [21, 22, 25, 80, 52]


### Tuple are delimited by normal brackets
Tuple items does not have to be the same type
Items are immutable


```python
#tuple using the constructor
planets = tuple(('mercury', 'venus', 'mars', 'earth'))
#tuple by assignment
moons = ('gannymege', 'europa', 'lo')

print(moons)

print(moons[0])

#moons[0] = 'earth'         #does not work, items are immutable

moons += ('callisto',)     #notice the trailing comma

print(moons)

```

    ('gannymege', 'europa', 'lo')
    gannymege
    ('gannymege', 'europa', 'lo', 'callisto')


### Range can only be obtain by invoking the range() function
It is used with for loops
More will be covered later



```python
a = range(6)
type(a)

b = range(3,7)

c = range(10, 25, 4)

```

# Mappings
More will be covered later

### Dictionary is a series of key-value pairs


```python
#dictionary from constructor
planets = dict()     #
services = {'ftp': 'no value', 'ssh': 22, 'smtp': 25, 'http': 80}
print(services)

services['ftp'] = 21          #mutate the value for key ftp
print(services)

services['dns'] = 53          #there is no key dns
print(services)


```

    {'ftp': 'no value', 'ssh': 22, 'smtp': 25, 'http': 80}
    {'ftp': 21, 'ssh': 22, 'smtp': 25, 'http': 80}
    {'ftp': 21, 'ssh': 22, 'smtp': 25, 'http': 80, 'dns': 53}



```python

```
