""" Exercise: Assignment-2
# Write a Python function, sumofdigits, that takes in one
number and returns the sum of digits of given number.
# This function takes in one number and returns one number
"""
def sumofdigits(n_):
    '''
    n is positive Integer

    returns: a positive integer, the sum of digits of n.
    if input is 123 then output is 6
    if input is 45677698 then output is 58
    '''
    # Your code here
    sum_digit = 0
    if n_ == 0:
        return sum_digit
    else:
        rem_ = n_ % 10
        sum_digit += rem_
        n_ = n_//10
    return sum_digit + sumofdigits(n)

def main():
    a_ = input()
    print(sumofdigits(int(a_)))

if __name__== "__main__":
    main()
