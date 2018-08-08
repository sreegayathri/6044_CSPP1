"""Exercise : Function and Objects Exercise-1
#Implement a function that converts the given
testList = [1, -4, 8, -9] into [1, 4, 8, 9]
"""

def apply_to_each(l_a, f_a):
    """if th input is [1, -8, 2], then output is [1, 8, 2]
    :param filename: L - array of int/char elements
    :param filename: f - function type used on the list elements
    :return: int"""
    for i in enumerate(l_a):
        l_a[i] = f_a(l_a[i])
    return l_a

def main():
    """using the condition from above and input here
    print """
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, abs))

if __name__ == "__main__":
    main()
