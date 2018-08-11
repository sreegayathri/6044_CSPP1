"""#Exercise: Assignment-4
#We are now ready to begin writing the code that interact
with the player. We'll be implementing the playHand function.
This function allows the user to play out a single hand.
First, though, you'll need to implement the helper
calculateHandlen function, which can be done in under five lines of code.
"""

def calculate_hand_len(hand):
    """
    :parama hand= dictionary (string int)
    :returns: integer
    """
    temp_a = ""
    length_of_hand = 0
    for letter in hand.keys():
        for _ in range(hand[letter]):
            temp_a = temp_a + letter
    length_of_hand = len(temp_a)
    return length_of_hand


def main():
    """call calculate_hand_len into main function"""
    n_a = input()
    adict_a = {}
    for _ in range(int(n_a)):
        data_a = input()
        list_a = data_a.split()
        adict_a[list_a[0]] = int(list_a[1])
    print(calculate_hand_len(adict_a))



if __name__ == "__main__":
    main()
