#Exercise : Function and Objects Exercise-3
#Implement a function that converts the given testList = [1, -4, 8, -9] into [1, 16, 64, 81]


def apply_to_each(L, f):
    """:param L the list of elements
    #:param f is the function that takes L elements to give the required o/p
    #:return int type"""
    for i in range(len(L)):
        L[i] = f(L[i])
    return L
def square(L):
    """takes the return value from apply_to_each"""
    return L*L
def main():
    """using the condition from above and input here 
    print"""
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, square))

if __name__== "__main__":
    main()
