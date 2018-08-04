"""Write a python program to find the square root of the given number
using approximation method
"""
def main():
    ''' print if the given string is perfect square or not'''
    num_val = int(input())
    epsilon = 0.1
    guess = 0
    inc = 0.1
    nu_a = 0
    while guess < num_val:
        if abs((guess**2) - num_val) < epsilon:
            break
        guess = guess + inc
        nu_a += 1
    if abs(guess**2 - num_val) >= epsilon:
        print(guess)
    else:
        print(guess)
if __name__ == "__main__":
    main()
