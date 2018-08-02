'''#Assume s is a string of lower case characters.

#Write a program that counts up the number of vowels contained in the string s.
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.
For example, if s = 'azcbobobegghakl', your program should print:

#Number of vowels: 5'''
def main():
    """ to find the number of vowels in a string"""
    count_abc = 0
    char_abc = input()
    for chat_abc in char_abc:
        if chat_abc in ('a', 'e', 'i', 'o', 'u'):
            count_abc += 1
    print(count_abc)
if __name__ == "__main__":
    main()
