#define the gen_primes function here
def prime_num(a):
    for number in range(2, a):
        if a % number == 0:
            return False
    return True

def gen_primes():
    digit = 2
    while True:
        if prime_num(digit):
            yield digit
        digit += 1


def main():
    data = input()
    l = data.split()
    a = int(l[0])
    b = int(l[1])
    primeGenerator = gen_primes()
    for i in range(a):
        p = primeGenerator.__next__()
        if(i%b == 0):
            print(p)
    
if __name__== "__main__":
    main()
