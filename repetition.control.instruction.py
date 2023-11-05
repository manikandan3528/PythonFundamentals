## Repetition Control Instruction
#   1. while 2. for
# Write a program that receives 3 sets of values p,n and r and calculate simple interest for each:
counter = 1
while counter <= 3:
    principle = float(input('Enter the value of principle: '))
    years = int(input('Enter the value of no of years: '))
    interest = float((input('Enter the value of rate of interest: ')))
    si = principle * years * interest/100
    print('Simple interest = Rs.' + str(si))
    counter = counter + 1

# for alpha in range(65, 91):
#     print(chr(alpha), end=",")

# i = 1
# j = 5
# # while not j == 80:
# #     print(i)
# #     i = i + 1
#
# for i in range(1, 10):
#     print(i)

