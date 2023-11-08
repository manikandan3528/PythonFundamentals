# Write a program to collect leap years from 1900 to 2023

leap_years = [year for year in range(1900, 2023) if year % 4 == 0]
print(leap_years)

# Write a program to collect odd numbers from 1 to 100

odd_numbers = [odd for odd in range(1, 100, 2)]
print(odd_numbers)

#write a program to collect even numbers from 1 to 100
even_numbers = [even for even in range(2, 100) if even % 2 == 0]
print(even_numbers)
