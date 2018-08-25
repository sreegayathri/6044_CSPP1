'''
Write a function to clean up a given string by removing the special characters and retain 
alphabets in both upper and lower case and numbers.
'''

def clean_string(string):
    """to give conditions for a alpha-symobl word/sentence"""
    z=""
    letter=""
    for i in range(len(string)):
        if string[i] == "(" or string[i] == ")" or
            string[i] == "!" or string[i] == "@" or
            string[i] == "." or string[i] == "#" or
            string[i] == "$" or string[i] == "%" or
            string[i] == "^" or string[i] == "&" or
            string[i] == "*" or string[i] == " ":
            letter = letter + z
        else:
            letter = letter + string[i]
    return letter

def main():
    string = input()
    print(clean_string(string))

if __name__ == '__main__':
    main()
