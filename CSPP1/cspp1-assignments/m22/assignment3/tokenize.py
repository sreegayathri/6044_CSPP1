'''
Write a function to tokenize a given string and return a dictionary with the frequency of
each word
'''
def tokenize(string):
    """conditions for the program"""
    for i in line:
        frequency = [string.count(w) for w in string]
    return dict(zip(string, frequency))


def main():
    """main function of the program"""
    lines = int(input())
    string = input().split(" ")
    print(tokenize(string))
    # print("frequencies\n"+ str(string)+ "\n")

if __name__ == '__main__':
    main()
