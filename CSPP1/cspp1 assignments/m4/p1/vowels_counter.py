'''#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5'''
def main():
    """ to find the number of vowels in a string"""
    COUNT_A = 0
    CHAR_A = input("enter a string")
    for CHAR_A in CHAR_A:
        if CHAR_A in ('a', 'e', 'i', 'o', 'u'):
            COUNT_A += 1
print(COUNT_A)
if __name__ == "__main__":
    main()
