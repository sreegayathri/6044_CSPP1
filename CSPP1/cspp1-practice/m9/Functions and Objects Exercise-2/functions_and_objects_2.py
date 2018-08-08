#Exercise : Function and Objects Exercise-2
#Implement a function that converts the given testList = [1, -4, 8, -9] into [2, -3, 9, -8]

def inc(L):
	#:param taking the L from apply_to_each
	return L+1
def apply_to_each(L, f):
	"""# :param L, is the list [] of element
	# :param f, is the increment function for the elements in L
	# :return the int type"""
    for i in range(len(L)):
        L[i] = f(L[i])
    return L

def main():
	"""the main function of the program,
	using the condition from above and input here 
    print"""
    data = input()
    data = data.split()
    list1 = []
    for j in data:
        list1.append(int(j))
    print(apply_to_each(list1, inc))

if __name__ == "__main__":
    main()
