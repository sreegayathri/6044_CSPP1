'''
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
    res_a = 0
    if num_a >= 0:
        for i in range(num_a+1):
            if num_a % 3 == 0:
                print(num_a + "Fizz")
            elif num_a % 5 == 0:
                print(num_a + "Buzz")
                break
        else:
            print(num_a)
            if num_a % 3 == 0 and num_a % 5 == 0:
                print(num_a + "Fizz")
                print(num_a + "Buzz")
            else:
                print(num_a)
if __name__ == "__main__":
    main()
