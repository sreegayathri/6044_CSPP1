#Exercise: Assignment-4
#We are now ready to begin writing the code that interacts with the player. We'll be implementing the playHand function. This function allows the user to play out a single hand. First, though, you'll need to implement the helper calculate_Hand_len function, which can be done in under five lines of code.


def calculate_hand_len(hand):
    """ 
    :param hand: dictionary (string int)
    :returns: integer type
    """
    temp_a = ""
    length_of_hand = 0
    for letter in hand.keys():
        for count in range(hand[letter]):
            temp_a = temp_a + letter
    length_of_hand = len(temp_a)
    return length_of_hand 
   

def main():
    """getting the required condition by calling calculate_hand_len into main"""
    n_input = input()
    adict = {}
    for i in range(int(n_input)):
        data = input()
        list_a = data.split()
        adict[list_a[0]] = int(list_a[1])
    print(calculate_hand_len(adict)

if __name__== "__main__":
    main()