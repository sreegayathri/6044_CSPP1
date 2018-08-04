"""Write a python program to find the square root of the given number
using approximation method"""
def main():
    ''' print if the given string is perfect square or not using n-r method'''
    num_val = int(input())
    guess = num_val/2.0
    epsilon = 0.01
    while (guess*guess-num_val) >= epsilon and guess <= num_val:
        guess = guess-(((guess**2)-num_val)/(2*guess))
    print(guess)

if __name__ == "__main__":
    main()
