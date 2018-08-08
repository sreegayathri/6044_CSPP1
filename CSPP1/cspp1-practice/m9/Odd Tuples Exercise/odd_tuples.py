"""Exercise : Odd Tuples
#Write a python function oddTuples(aTup) that takes a some numbers in the tuple as
input andreturns a tuple in which contains odd index values in the input tuple
"""
def odd_tuples(a_tup):
    '''
    aTup: a tuple
    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    b_tup = ()
    for i in range(0, len(a_tup)):
        if i % 2 == 0:
            b_tup += (a_tup[i], )
    return b_tup
def main():
    """ to get even index elements and swapping elements to a new tuple"""
    data = input()
    data = data.split()
    a_tup = ()
    for j in range(len(data)):
        a_tup += (int(data[j]),)
    print(odd_tuples(a_tup))
if __name__ == "__main__":
    main()
