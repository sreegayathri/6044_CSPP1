num_a = int(input())
if num_a > 0:
    if num_a % 3 == 0:
        print("Fizz")
    elif num_a % 5 == 0:
        print("Buzz")
if num_a % 3 == 0 and num_a % 5 ==0:
        print("Fizz")
        print("Buzz")
else:
    print("not a multiple of 3 and 5")