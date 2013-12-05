calculator
==========

This is a just another calculator with console interface written in Python 2.7.
It supports basic arithmetical operations, subset of math functions built-in python,
works correctly with brackets.

installation
------------
```bash
# python setup.py install
```

usage
-----

1. as standalone script:
```bash
$ calc
``` 

2. as python class:
```python
import calculator as calc
c = calc.Calculator()
c.calculate("string with math expr")
```

It uses logging module, so you can change its
log level or define output log path.

You can add and/or change existing calculation
rules on the fly, for example:
```python
import calculator as calc
import calculator.definitions as defs

c = calc.Calculator()
c.calculate('sin(pi)') # == 0

defs._constants['pi'] = defs.Constant(value = 1.5707963) # pi/2
c.calculate('sin(pi)') # == 1
```

You can add/customize new functions, operators, constants defined
in calculator/definitions.py. 
