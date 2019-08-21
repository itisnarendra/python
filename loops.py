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
