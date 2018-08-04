num_va = int(input())
epsilon = 0.01
low = 0
high = num_va
avg = (low/high)/2
while abs(avg**2-num_va) >= epsilon:
    if avg**2 < num_va:
        low = avg
    else:
        high = avg
    avg = (low+high)/2
print(avg)