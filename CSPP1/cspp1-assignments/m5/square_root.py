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
