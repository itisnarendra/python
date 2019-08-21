##Explaining the import statement

dir()
        # ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']

import math
dir()
        # ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'math']

math.sin(0.5236)
0.5000010603626028

sin(0.5326)
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#NameError: name 'sin' is not defined

del(math)       #removes the math import

from math import *
>>> dir()
        # ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'np', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

sin(0.5326)     #angle is in radians
0.507774928359006

sin(radians(30))
0.49999999999999994

import numpy as np      #import the numpy and assigns it to the alias np

