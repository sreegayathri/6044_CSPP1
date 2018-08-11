"""Exercise: Assignment-2
#Implement the updateHand function. Make sure
this function has no side effects: i.e., it must not
mutate the hand passed in. Before pasting your function
definition here, be sure you've passed the appropriate
tests in test_ps4a.py.
"""

def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.
    #Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    temp_dictionary = hand.copy()
    for character in word:
        temp_dictionary[character] -= 1
    return temp_dictionary

def main():
    n_a = input()
    adict_a = {}
    for _ in range(int(n_a)):
        data_a = input()
        list_a = data_a.split()
        adict_a[list_a[0]] = int(list_a[1])
    data1_a = input()
    print(update_hand(adict_a, data1_a))

if __name__ == "__main__":
    main()
