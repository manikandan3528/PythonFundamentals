#Dictionary is a collection of key-value pairs.
#Dictionaries are also known as maps or associative arrays
#Keys in a dictionary must be unique and immutable.
#e.g.
b = {'A101': 'Amol', 'A102': 'Anand', 'A103': 'Ravi'}
#Key value in dictionary are unique, but different key may have same values paired with them
print(b['A102'])
for k,v in b.items():
    print("key: " + k)
    print("value: " + v)
