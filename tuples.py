# Tuples are typically used for handling heterogeneous data
# Heterogeneous data is enclosed within ()
# Tuples are immutable
t = ('God', "bless", 'you', 1, 2, 3, 4, 5, 'Happy', 'you')
print(t)
# t[4] = 10
print(min(t[3:8]))

result = divmod(10, 2)
print(result)

students = [("A101", "John", 23), ("A102", "Raj", 23), ("A103", "Matt", 24)]
student_ids = []
for student in students:
    student_ids = student_ids + [student[0]]
print(student_ids)

