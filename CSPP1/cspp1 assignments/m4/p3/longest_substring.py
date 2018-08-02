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
    string_ab = "abcdbc"
    s_ab = 0
    count_ab = 0
    count1_ab = 0
    for i in range(len(string_ab) - 1):# comparing the indices
        if string_ab[i] <= string_ab[i+1]:# comparing the characters in the indices
            count_ab += 1
            if count_ab > count1_ab:
                count1_ab = count_ab
                s_ab = i + 1
        else:
            count_ab = 0
    str_ab = s_ab - count1_ab
print(string_ab[str_ab:s_ab + 1])
if __name__ == "__main__":
    main()
