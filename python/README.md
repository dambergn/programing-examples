# Python

## Getting Started
which python
which python3
#!/usr/bin/python3

you can run a script via python3 name-of-script.py
or
put #!/usr/bin/python3 
at top of file and make exicutable by
sudo chmod +x name-of-script.py
then run script with ./name-of-script.py

## Console output
```py
print("Hello World")
print("Hello World's")
print('Hello "World\'s"')
```

## Variables
```py
VARIABLE_STRING = "string"
VARIABLE_BOOLIEN = False
VARIABLE_INTIGER = 
VARIABLE_DECIMAL = float('.01')
VARIABLE_LIST = ['one', 'two', 'three']
```

## Data types

## User input
```py
VARIABLE = input()
```

## Boolian Values
```py
== # Equal to
!= # Not Equal to
<  # Less Than
>  # Greater Than
<= # Less Than or Equal to
>= # Greater than or equal to
```

## if statements
```py
if something == true:
    # do something

if something == false:
    # do this
else:
    # do this instead

if something < 9000:
    # It's over 9000!!!
elif something > 9000 and something < 0:
    # Average power level
else
    # You are Yamcha
```

## for loops

## while loops
```py
counter = 0
while counter < 5:
    # do something
    counter = counter +1 # incriments counter
```

## functions
```py
def function_name()
    #do something

function_name()
```

## Math Examples
```py
# Simple addition
2 + 3
5

# Simple subtracton
9 - 8
1

# Simple mutiplication
4 * 6
24

# Simple division / returns float number
8  / 4
2.0

# Simple division with remainder
5 / 2
2.5

# Simple division without remainder
5 // 2
2

# Divison returning only remainder as whole int (modulus)
5 % 2
5

# Math order of operations
8 + 2 * 3
14

# Defining math order
(8 + 2) * 3
30

# To the power of long vs short hand
2 * 2 * 2
8

2 ** 3
8
```

## Built in functions
len() # will give the length of a string or array  
str() # Will convert a int into a string  
int() # Defines the use of an intiger  
float() # Defines the use of a floating point number .01  