""" Longest substring in alphabetical order """
string = "abcdbc"
s = 0
count = 0
count1 = 0
for i in range(len(string) - 1):# comparing the indices
    if string[i] <= string[i+1]:# comparing the characters in the indices
        count += 1
        if count > count1:
            count1 = count
            s = i + 1
    else:
        count = 0
str1 = s - count1
print(string[str1:s+1])
