'''
Write a function to clean up a given string_clear by removing the special characters and retain
alphabets in both upper and lower case and numbers.
'''

def clean_string(string_clear):
    """conditions for the program"""
    z_empty = ""
    letter_clear = ""
    length_clear = len(string_clear)
    for i in enumerate(length_clear):
        if string_clear[i] == "(!@#$%^&*)>.,''" or string_clear[i] == ")" or string_clear[i] == "!" or string_clear[i] == "@" or string_clear[i] == "." or string_clear[i] == "#" or string_clear[i] == "$" or string_clear[i] == "%" or string_clear[i] == "^" or string_clear[i] == "&"or string_clear[i] == "*" or string_clear[i] == " ":
            letter_clear = letter_clear + z_empty
        else:
            letter_clear = letter_clear + string_clear[i]
    return letter_clear

def main():
    """main function of this program"""
    string_clear = input()
    print(clean_string(string_clear))

if __name__ == '__main__':
    main()
