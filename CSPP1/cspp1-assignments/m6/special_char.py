str_ab=input()
z=" "
letter=""
for i in range(len(str_ab)):
    if str_ab[i] == "!" or str_ab[i] == "@" or str_ab[i] == "#" or str_ab[i] == "$" or str_ab[i] == "%" or str_ab[i] == "^" or str_ab[i] == "&"or str_ab[i] == "*":
        letter = letter + z
    else:
        letter = letter + str_ab[i]
print(letter)
