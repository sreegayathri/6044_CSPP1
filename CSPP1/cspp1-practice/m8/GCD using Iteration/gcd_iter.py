# Exercise: GCDIter
# Write a Python function, gcdIter(a, b), that takes in two numbers and returns the GCD(a,b) of given a and b.

# This function takes in two numbers and returns one number.


def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b
    '''
    # Your code here
    gcdIter = 1
    if a % b == 0:
        return b
    for k in range(int(b / 2), 0, -1):
        if a % k == 0 and b % k == 0:
            gcd = k
            break  
    return gcd
def main():
    data = input()
    data = data.split()
    print(gcdIter(int(data[0]), int(data[1])))

if __name__== "__main__":
    main()