'''
    Write a program to evaluate poker hands and determine the winner
    Read about poker hands here.
    https://en.wikipedia.org/wiki/List_of_poker_hands
'''
VAL_DICT = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8,\
    '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}



def is_four_of_akind(hand):
    '''
    to check if hand it is a four of a kind or not and sends the true or false
    '''

    check_hand = []
    freq_dict = []
    for card in hand:
        check_hand.append(card[0])
    for number_count in check_hand:
        freq_dict.append(check_hand.count(number_count))
    if max(freq_dict) >= 4:
        for key in freq_dict:
            if freq_dict[key] == 4:
                return key
    # return False

def is_full_house(hand):
    """to check any hand scored a full house"""
    check_full_house = []
    freq_dict_house = []
    for card in hand:
        check_full_house.append(card[0])
    for dani in check_full_house:
        freq_dict_house.append(check_full_house.count(dani))
    sorted(freq_dict_house)
    if freq_dict_house == [2, 3]:
        return True
    return False

def is_flush(hand):
    '''
        How do we find out if the given hand is a flush?
        The hand has a list of cards represented as strings.
        Do we need both the characters in the string? No.
        The second character is good enough to determine a flush
        Think of an algorithm: given the card suite how to check if it is a flush
        Write the code for it and return True if it is a flush else return False
    '''
    suit_list = []
    sum_ascii = 0
    for i in hand:
        suit_list.append(i[1])
    for i in suit_list:
        sum_ascii = sum_ascii + ord(i)
    if sum_ascii == 5*ord(i):
        return True
    return False

def is_straight(hand):
    '''
        How do we find out if the given hand is a straight?
        The hand has a list of cards represented as strings.
        There are multiple ways of checking if the hand is a straight.
        Do we need both the characters in the string? No.
        The first character is good enough to determine a straight
        Think of an algorithm: given the card face value how to check if it a straight
        Write the code for it and return True if it is a straight else return False
    '''
    face_values = []
    for i in hand:
        face_values.append(VAL_DICT[i[0]])
    sorted(face_values)
    for k in range(0, len(face_values)-1, 1):
        if face_values[k+1]-face_values[k] != 1:
            return False
    return True

def is_three_of_akind(hand):
    """ to check if atleast 3 cards are of a kind """
    check_hand = []
    freq_dict = []
    for card in hand:
        check_hand.append(card[0])
    for number_count3 in check_hand:
        freq_dict.append(check_hand.count(number_count3))
    if max(freq_dict) >= 3:
        for key in freq_dict:
            if freq_dict[key] == 3:
                return key

def is_two_pair(hand):
    """ to check if atleast 2 pair of cards are of a kind present or not"""
    check_hand = []
    freq_dict = []
    for card in hand:
        check_hand.append(card[0])
    for number_count2 in check_hand:
        freq_dict.append(check_hand.count(number_count2))
    if max(freq_dict) >= 2:
        if sorted(check_hand.values()) == [1, 2, 2]:
            for key in freq_dict:
                if freq_dict[key] == 2:
                    return True

def is_one_pair(hand):
    '''
    if input set of cards contains only pairs of cards
    with same facevalue
    output id true
    '''
    check_hand = []
    freq_dict = []
    for card in hand:
        check_hand.append(card[0])
    for num_freq in check_hand:
        if check_hand.count(num_freq) == 2:
            freq_dict.append(num_freq)
            print(freq_dict)
    if max(freq_dict) >= 1:
        for key in freq_dict:
            if freq_dict[key] == 1:
                return VAL_DICT[key]

def is_high_card(hand):
    '''
    returns the hand with high card value
    '''
    check_high = []
    for card in hand:
        if card[0] in ['J', 'K', 'Q', 'A', 'T']:
            check_high.append(VAL_DICT[card[0]]/int(10))
        else:
            check_high.append(int(card[0])/int(10))
    return max(check_high)/100

def hand_rank(hand):
    '''
        You will code this function. The goal of the function is to
        return a value that max can use to identify the best hand.
        As this function is complex we will progressively develop it.
        The first version should identify if the given hand is a straight
        or a flush or a straight flush.
    '''

    # By now you should have seen the way a card is represented.
    # If you haven't then go the main or poker function and print the hands
    # Each card is coded as a 2 character string. Example Kind of Hearts is KH
    # First character for face value 2,3,4,5,6,7,8,9,T,J,Q,K,A
    # Second character for the suit S (Spade), H (Heart), D (Diamond), C (Clubs)
    # What would be the logic to determine if a hand is a straight or flush?
    # Let's not think about the logic in the hand_rank function
    # Instead break it down into two sub functions is_straight and is_flush

    # check for straight, flush and straight flush
    # best hand of these 3 would be a straight flush with the return value 3
    # the second best would be a flush with the return value 2
    # third would be a straight with the return value 1
    # any other hand would be the fourth best with the return value 0
    # max in poker function uses these return values to select the best hand
    if is_flush(hand) and is_straight(hand):
        return 9
    elif is_four_of_akind(hand):
        return 8
    elif is_full_house(hand):
        return 7
    elif is_straight(hand):
        return 5
    elif is_flush(hand):
        return 6
    elif is_three_of_akind(hand):
        return 4
    elif is_two_pair(hand):
        return 3
    elif is_one_pair(hand):
        return 1
    return is_high_card(hand)

def poker(hands):
    '''
        This function is completed for you. Read it to learn the code.

        Input: List of 2 or more poker hands
               Each poker hand is represented as a list
               Print the hands to see the hand representation

        Output: Return the winning poker hand
    '''

    # the line below may be new to you
    # max function is provided by python library
    # learn how it works, in particular the key argument, from the link
    # https://www.programiz.com/python-programming/methods/built-in/max
    # hand_rank is a function passed to max
    # hand_rank takes a hand and returns its rank
    # max uses the rank returned by hand_rank and returns the best hand
    return max(hands, key=hand_rank)

if __name__ == "__main__":
    # read the number of test cases
    COUNT = int(input())
    # iterate through the test cases to set up hands list
    HANDS = []
    for x in range(COUNT):
        line = input()
        hand_a = line.split(" ")
        HANDS.append(hand_a)
    # test the poker function to see how it works
    print(' '.join(poker(HANDS)))
