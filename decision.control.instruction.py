## Decision Control Instruction
#   Three ways for taking decisions in program:
#       1) if condition:(=,<,>,>=,<=)
if False:
    print("hi there")
#       2) if condition:
#          else:
if 15 < 5:
    print("I am working")
else:
    print("I am free")
#       3) if condition:
#           elif:
#           else:
if "Raj" in "Ramachandran":
    print("Raj present")
elif "Ram" in "Ramakrishnan":
    print("Ram present")
else:
    print("Ram absent")
## Logical Operators
input = 19
output = input % 2
if output == 0:
    print("Given number is even")
elif output == 1:
    print("Given number is odd")
else:
    print("invalid input")