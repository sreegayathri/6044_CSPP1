'''Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s.
For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2'''

def main():
	""" to count the number of times a substring occurs"""
    s_abc = input()
    sub_abc = 'bob'
    result_abc = 0
    sub_len = len(sub_abc)
    for i in range(len(s_abc)):
        if s_abc[i:i+sub_len] == sub_abc:
            result_abc += 1
    print(result_abc)
if __name__== "__main__":
	main()
