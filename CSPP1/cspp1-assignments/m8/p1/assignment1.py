""" Exercise: Assignment-1
# Write a Python function, factorial(n), that takes in one
#number and returns the factorial of given number.

# This function takes in one number and returns one number."""
def factorial(n_a):
    '''
    n is positive Integer
    if input is 5 output is 120
    if input is 0 output is 1
    returns: a positive integer, the factorial of n.
    '''
    if n_a == 0:
        return 1
    return n_a*factorial(n_a-1)

def main():
    """print the factorial of given number"""
    a_n = input()
    print(factorial(int(a_n)))

if __name__ == "__main__":
    main()
