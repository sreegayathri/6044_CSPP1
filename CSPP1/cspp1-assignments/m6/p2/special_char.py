'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str_ab=input()
    z=" "
    ltr=""
    for i in range(len(str_ab)):
        if str_ab[i] == "!" or str_ab[i] == "@" or str_ab[i] == "#" or str_ab[i] == "$" or str_ab[i] == "%" or str_ab[i] == "^" or str_ab[i] == "&"or str_ab[i] == "*":
            ltr = ltr + z
        else:
            ltr = ltr + str_ab[i]
    print(ltr)
if __name__ == "__main__":
    main()
