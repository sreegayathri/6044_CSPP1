# Write a python program to find if the given number is a perfect cube or not
# using guess and check algorithm

# testcase 1
# Input: 24389
# Output: 24389 is a perfect cube

# testcase 2
# Input: 21950
# Output: 21950 is not a perfect cube

def _main_():
    num_va = int(input())
    guess = 0
    epsilon = 0.1
    inc = 0.1
    num_a = 0
    while guess < num_va:
        if abs(guess**3-num_va) < epsilon:
            break
        guess = guess+inc
        num_a += 1
    if abs(guess**3-num_va) >= epsilon:
        print(num_va, "is not a perfect cube")
    else:
        print(num_va, "is a perfect cube")

if __name__ == "__main__":
    main()
