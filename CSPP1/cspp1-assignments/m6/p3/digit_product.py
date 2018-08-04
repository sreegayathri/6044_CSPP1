'''Given a  number int_input, find the product of all the digits
example:input: 123 and output: 6'''
def main():
    '''Read any number from the input, store it in variable int_input.'''
    n_a = int(input())
    product = 1
    r_a = 0
    if n_a > 0:
        if n_a % 10 != 0:
            r_a += 1
            product *= r_a
    print(product)
if __name__ == "__main__":
    main()
