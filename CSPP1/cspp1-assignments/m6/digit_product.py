n_a = int(input())
product = 1
i = 0
r_a = 0
if n_a > 0:
    if n_a % 10 != 0:
        r_a += 1
        product *= r_a
print(product)