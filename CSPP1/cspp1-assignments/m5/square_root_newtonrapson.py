num_val = int(input())
guess = num_val/2.0
epsilon = 0.01
while (guess*guess-num_val) >= epsilon and guess <= num_val:
	guess = guess-(((guess**2)-num_val)/(2*guess))
print(guess)
