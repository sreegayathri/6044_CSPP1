'''Given a  number int_input, find the product of all the digits
example:input: 123 and output: 6'''
def main():
    '''Read any number from the input, store it in variable int_input.'''
    n_a = int(input())
    product = 1
    r_a = 0
    while n_a > 0:
        r_a = n_a % 10
        product *= r_a
        n_a = n_a//10
    print(product)
if __name__ == "__main__":
    main()
