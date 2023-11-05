#Comprehensions offer an easy and compact way of creating lists, set and dictionaries
#A comprehension works by looping or iterating over items and assigning them to a container like
#list, set or dictionary
#This container can't be tuple as tuple being immutable is unable to receive assignments
a = [n for n in range(20)]
print(a)
b = [{x, x**2, x**3} for x in range(10)]
print(b)
c = [n for n in range(10,30) if n%2 == 0]
print(c)