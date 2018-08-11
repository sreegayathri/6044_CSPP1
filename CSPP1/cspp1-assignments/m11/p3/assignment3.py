# Assignment-3
'''At this point, we have written code to generate a random
hand and display that hand to the user. We can also ask the
user for a word (Python's input) and score the word (using
your getWordScore). However, at this point we have not written
any code to verify that a word given by a player obeys the rules
of the game. A valid word is in the word list; and it is composed
entirely of letters from the current hand. Implement the isValidWord function.
Testing: Make sure the test_isValidWord tests pass.
In addition, you will want to test your implementation
by calling it multiple times on the same hand - what
should the correct behavior be? Additionally, the
empty string ('') is not a valid word - if you code
this function correctly, you shouldn't need an additional
check for this condition.
Fill in the code for isValidWord in ps4a.py and be sure
you've passed the appropriate tests in test_ps4a.py before
pasting your function definition here.'''

def is_valid_word(word_a, hand_a, word_list):
    """
    :param word= is a string
    hand= dictionary (string -> int)
    wordList= list of lowercase strings
    :returm boolean type
    """
    character_number = 0
    new_dictionary = hand_a.copy()

    if word_a in word_list:
        for letter in word_a:
            if (not(letter in new_dictionary)):
                return False
            # else:
                character_number += 1
                new_dictionary[letter] -= 1
                if new_dictionary[letter] < 0:
                    return False
        if character_number == len(word_a):
            return True
    # else:
    #     return False



def main():
    """call is_valid_word into main"""
    word_a = input()
    n_a = int(input())
    adict_a = {}
    for _ in range(n_a):
        data_a = input()
        list_a = data_a.split()
        adict_a[list_a[0]] = int(list_a[1])
    list2_a = input().split()
    print(is_valid_word(word_a, adict_a, list2_a))

if __name__ == "__main__":
    main()
