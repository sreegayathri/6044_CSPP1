'''
Exercise: Assignment-1
The first step is to implement some code that allows us to calculate the score
for a single word. The function get_word_score should accept as input a string
of lowercase letters (a word) and return the integer score for that word, using
the game's scoring rules.
'''

def get_word_score(word_a, n_a):
    """
    "Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on"
    :param word = string (lowercase letters)
    :param n = integer (HAND_SIZE; i.e., hand size required for additional points)
    :returns: int >= 0
    """
    list_1 = []
    scrabble_letter_values = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
    sum_of = 0
    for key in word_a:
        if key in scrabble_letter_values:
            list_1.append(key)
            temp = scrabble_letter_values[key]
            sum_of = sum_of + temp
    length = len(word_a)
    temp_2a = sum_of * length

    if len(word_a) == 7:
        temp_2a = temp_2a + 50
    return temp_2a


def main():
    '''
    call get_word_score into main function for the given problem
    '''
    data = input()
    data = data.split()
    #print(data)
    print(get_word_score(data[0], int(data[1])))


if __name__ == "__main__":
    main()
