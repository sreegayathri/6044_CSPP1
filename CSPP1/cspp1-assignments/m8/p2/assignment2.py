""" Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one
number and returns the sum of digits of given number.
# This function takes in one number and returns one number
"""
def sumofdigits(n_a):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    if input is 123 then output is 6
    if input is 45677698 then output is 58
    '''
    # Your code here
    sum_digit = 0
    if n_a == 0:
        return sum_digit
    rem_r = n_a % 10
    sum_digit += rem_r
    n_a = n_a//10
    return sum_digit + sumofdigits(n_a)

def main():
    """print the output we get from above function"""
    a_n = input()
    print(sumofdigits(int(a_n)))

if __name__ == "__main__":
    main()
