# Exercise: Is In
# Write a Python function, isIn(char, aStr), that takes in two arguments a character and String and returns the isIn(char, aStr) which retuns a boolean value.

# This function takes in two arguments character and String and returns one boolean value.

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    asm_a = ''
    if aStr =='':
        return False
    asm_a = sorted(aStr)
    m = asm_a[len(asm_a)//2]
    if char == m:
        return True
    if len(asm_a) == 1 and asm_a[0] != char:
        return False
    elif len(asm_a) == 0:
        return False
    elif char < m:
        return isitIn(char, asm_a[:len(asm_a)//2])
    else:
        return isitIn(char, asm_a[len(asm_a)//2:])
    return isitIn(char, aStr)
def main():
    data = input()
    data = data.split()
    print(isIn((data[0][0]), data[1]))


if __name__ == "__main__":
    main()