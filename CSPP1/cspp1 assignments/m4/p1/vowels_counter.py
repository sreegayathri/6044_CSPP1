#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5

def main():
	""" to find the number of vowels in a string"""
COUNT = 0
CHAR = input("enter a string")
for char_ in CHAR:
    if char_ in ('a', 'e', 'i', 'o', 'u'):
        COUNT += 1
print(COUNT)

if __name__ == "__main__":
	main()
