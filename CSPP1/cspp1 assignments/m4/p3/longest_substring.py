'''Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in
which the letters occur in alphabetical order.
For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring.
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart.
If you've spent more than a few hours on this problem, we suggest that
you move on to a different part of the course.
If you have time, come back to this problem after you've had a break and
cleared your head.'''

def main():
	""" Longest substring in alphabetical order """
	STRING_A = "abcdbc"
	S_AB = 0
	COUNT_AB = 0
	COUNT1_AB = 0
	for i in range(len(STRING_AB) - 1):# comparing the indices
    	if STRING_AB[i] <= STRING_AB[i+1]:# comparing the characters in the indices
        	COUNT_AB += 1
        	if COUNT_AB > COUNT1_AB:
            	COUNT1_AB = COUNT_AB
            	S_AB = i + 1
    	else:
        COUNT_AB = 0
	STR_AB = S_AB - COUNT1_AB
print(string[STR_AB:S_AB + 1])
if __name__ == "__main__":
	main()
