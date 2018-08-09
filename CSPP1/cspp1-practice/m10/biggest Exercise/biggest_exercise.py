"""Exercise : Biggest Exercise
#Write a procedure, called biggest, which returns the
#key corresponding to the entry with the largest number
#of values associated with it. If there is more than one
#such entry, return any one of the matching keys."""
def biggest(a_dict):
    '''
    a_dict: A dictionary, where all the values are lists.
    returns: The key with the largest number of values associated with it
    '''
    let_key = 0
    key_val = []
    for key in a_dict.keys():
        length_okey =len(a_dict[key])
        if length_okey >= let_key:
            let_key = length_okey
            key_val += [key]
    return key_val
def main():
    n=input()
    a_dict={}
    for i in range(int(n)):
        s_input=input()
        element_a=s_input.split()
        if element_a[0][0] not in a_dict:
            a_dict[element_a[0][0]]=[element_a[1]]
        else:
            a_dict[element_a[0][0]].append(element_a[1])
    print(biggest(a_dict))
if __name__== "__main__":
    main()
