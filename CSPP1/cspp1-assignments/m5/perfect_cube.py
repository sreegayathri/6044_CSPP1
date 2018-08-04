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
