# Write a python program to find the square root of the given number
# using approximation method

# testcase 1
# input: 25
# output: 4.999999999999998

# testcase 2
# input: 49
# output: 6.999999999999991

def main():
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
