'''
Write a function to clean up a given string by removing
the special characters and retain
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    """to give conditions for a alpha-symobl word/sentence"""
    z_a = ""
    letter_clean = ""
    for i in enumerate(string):
        if (string[i] == "(" or string[i] == ")" or\
            string[i] == "!" or string[i] == "@" or\
            string[i] == "." or string[i] == "#" or\
            string[i] == "$" or string[i] == "%" or\
            string[i] == "^" or string[i] == "&" or\
            string[i] == "*" or string[i] == " "):
            letter_clean = letter_clean + z_a
        else:
            letter_clean = letter_clean + string[i]
    return letter_clean

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
