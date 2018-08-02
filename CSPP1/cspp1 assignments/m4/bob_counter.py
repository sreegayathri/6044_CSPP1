'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
    """ to count the number of times a substring occurs"""
S = 'azcbobobobegghakl'
SUB = 'bob'
RESULTS = 0
S_LEN = len(S)
SUB_LEN = len(SUB)
for i in range(len(S)):
    if S[i:i+SUB_LEN] == SUB:
        RESULTS += 1
print(RESULTS)
if __name__== "__main__":
    main()
