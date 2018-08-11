#Exercise: Assignment-4
#We are now ready to begin writing the code that interacts with the player. We'll be implementing the playHand function. This function allows the user to play out a single hand. First, though, you'll need to implement the helper calculateHandlen function, which can be done in under five lines of code.


def calculateHandlen(hand):
    """ 
    :parama hand= dictionary (string int)
    :returns: integer
    """
    temp = ""
    lengthofhand = 0
    for letter in hand.keys():
        for count in range(hand[letter]):
            temp = temp + letter
    lengthofhand = len(temp)
    return lengthofhand 
    

def main():
    n_a = input()
    adict_a = {}
    for i in range(int(n_a)):
        data_a = input()
        list_a = data_a.split()
        adict_a[list_a[0]] = int(list_a[1])
    print(calculate_hand_len(adict_a))
        


if __name__== "__main__":
    main()