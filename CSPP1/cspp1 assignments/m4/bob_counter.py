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
