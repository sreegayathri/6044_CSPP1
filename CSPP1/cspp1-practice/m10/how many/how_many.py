"""Exercise : how many
# write a procedure, called how_many, which returns the
#sum of the number of values associated with a dictionary.
"""

def how_many(a_dict):
    '''
    a_dict: A dictionary, where all the values are lists.
    returns: int, how many values are in the dictionary.
    '''
    sum_a = 0
    for i in a_dict:
        sum_a = sum_a + len(a_dict[i])
    return sum_a
def main():
    """this a main function that uses a_dict"""
    n_a = input()
    a_dict = {}
    for _ in range(int(n_a)):
        s_a = input()
        l_a = s_a.split()
        if l_a[0][0] not in a_dict:
            a_dict[l_a[0][0]] = [l_a[1]]
        else:
            a_dict[l_a[0][0]].append(l_a[1])
    print(how_many(a_dict))
if __name__ == "__main__":
    main()
