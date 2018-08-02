""" to find the number of vowels in a string"""
COUNT = 0
CHAR = input("enter a string")
for char_ in CHAR:
    if char_ in ('a', 'e', 'i', 'o', 'u'):
        COUNT += 1
print(COUNT)
