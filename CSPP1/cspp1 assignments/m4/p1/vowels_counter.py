'''#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5'''
def main():
    """ to find the number of vowels in a string"""
    count_a = 0
    char_a = input("enter a string")
    for char_a in char_a:
        if char_a in ('a', 'e', 'i', 'o', 'u'):
            count_a += 1
print(count_a)
if __name__ == "__main__":
    main()
