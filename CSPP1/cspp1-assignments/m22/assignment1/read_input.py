'''
Write a python program to read multiple lines of text input and store the input into a string.
'''
def sentences(lines):
    text = []
    for i in range(lines):
        text_input = input()
        k_text = text_input
        text.append(k_text)
    return text
    

def main():
    lines = int(input())
    sent_def =sentences(lines)
    # for i in range(lines):
    print(*sent_def, sep="\n")


if __name__ == '__main__':
    main()
