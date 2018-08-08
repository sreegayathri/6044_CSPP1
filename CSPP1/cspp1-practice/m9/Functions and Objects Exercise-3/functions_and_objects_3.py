"""#Exercise : Function and Objects Exercise-3
#Implement a function that converts the given testList = [1, -4, 8, -9]
 into [1, 16, 64, 81]"""


def apply_to_each(l_a, f_a):
    """:param l_a the list of elements
    #:param f_a is the function that takes L elements to give the required o/p
    #:return int type"""
    for i in enumerate(l_a):
        l_a[i] = f_a(l_a[i])
    return l_a
def square(l_a):
    """takes the return value from apply_to_each"""
    return l_a*l_a
def main():
    """using the condition from above and input here
    print"""
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, square))

if __name__ == "__main__":
    main()
