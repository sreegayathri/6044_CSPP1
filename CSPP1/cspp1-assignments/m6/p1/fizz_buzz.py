'''# fe5142200c606f1f4e75620a559a577ab933e43c
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
def main():
    '''
    Read number from the input, store it in variable num.
    '''
    num_a = int(input())
    if num_a >= 0:
        for i in range(1, num_a+1):
            if i % 3 == 0 and i % 5 == 0:
                print("Fizz\nBuzz")
            elif i % 3 == 0:
                print("Fizz")
            elif i % 5 == 0:
                print("Buzz")
            else:
                print(i)
if __name__ == "__main__":
    main()
