'''# 10d9bbf28e4991a85c6978809e464abedede7449
Given a  number int_input, find the product of all the digits
example:input: 123 and output: 6'''
def main():
    '''Read any number from the input, store it in variable int_input.'''
    n_a = int(input())
    product = 1
    if n_a == 0:
        product = 0
    while n_a > 0:
        r_a = abs(n_a) % 10
        product *= r_a
        n_a = abs(n_a)//10
    print(product)
if __name__ == "__main__":
    main()
