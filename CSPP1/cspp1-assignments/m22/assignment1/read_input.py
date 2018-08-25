'''
Write a python program to read multiple lines of text input and store the input into a string.
'''
def sentences(lines):
    for i in range(lines):
        text_input = input()
        k_text = text_input*lines
    return k_text
    

def main():
    lines = int(input())
    # for i in range(lines):
    print("\n".join(sentences(lines))

if __name__ == '__main__':
    main()
