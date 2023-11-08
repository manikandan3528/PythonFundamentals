#Sets - Sets are like lists, with an exception that they don't contain duplicate entries
# Set is an unordered collection, hence order of insertion is not same as the order of access
# set() function can be used to convert list or tuple into a set
# Sets are like lists and their content can be mutable
s = {"who", "did", "invent"}
print(s)
s.add("automobile")
print(s)
# If we want an immutable set, we should use frozenset
# s = frozenset({"I", "know", "Python"})
# s.add("program")

#sets
managers = {'Adi', 'Raj', 'Gopal'}
engineers = {'Vijay', 'Ajay', 'Raj', 'Suresh'}

#union
print(engineers | managers)

#intersection
print(engineers & managers)

#difference
print(engineers - managers)

#symmetric
print(managers ^ engineers)