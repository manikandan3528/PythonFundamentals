# Python string is a collection of Unicode characters
# Python strings can be enclosed in single, double and triple quotes
#e.g.
#   'Hello world'
#   "Hello world"
#   ''' This is the correct
#                sentence'''
name = 'Pychram IDE'
message = "Hi, This is a hello message from me"
description = '''I am entering some random message in 
                two lines'''
print(name)
print(message)
print(description)
## Accessing String Elements
#   String elements can be accessed using an index value, starting with 0.
#       Negative index value is allowed. The last character is considered to be at index -1.
a = 'helLo world'
print(a[3])
#   A substring can be sliced out of a string e.g. s[start:end]
print(a[6:9])
#   Using too large an index reports an error.
# print(a[100])
## String properties
#   All strings are objects of build-in type str. print(type(msg))
print(type(name))
# principle = 1000.00
# print(type(principle))
#   Python strings are immutable - they can't be changed
#   String can be concatenated using +
firstname = "Ram"
lastname = "siva"
fullname = firstname + ' ' + lastname
print(fullname)
#   String can be replicated during printing. print('-', 10)
print("*",' ',10)
#   whether one string is part of another can be found out using in. print('e' in 'Hello')
fullname2 = "Raj siva"
fullname3 = "Rock bounce"
print("siva" in fullname)
print("siva" in fullname2)
print("siva" in fullname3)
## String operations
#   Many built-in string functions are available.
a = (10000,4000,60000)
b = 12000
c = 15000
print(b)