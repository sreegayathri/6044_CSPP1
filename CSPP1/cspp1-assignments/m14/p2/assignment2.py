''' Problem 2 - plaintext_message '''
# For this problem, the graders will use our implementation of the Message class,
# so don't worry if you did not get the previous parts correct.

# plaintext_message is a subclass of Message and has methods to encode a string
# using a specified shift value. Our class will always create an encoded version
# of the message, and will have methods for changing the encoding.

# Implement the methods in the class plaintext_message according to the specifications in ps6.py.
# The methods you should fill in are:
# __init__(self, text, shift): Use the parent class constructor to make your code more concise.
# The getter method get_shift(self)
# The getter method get_encrypting_dict(self): This should return a COPY of self.encrypting_dict.
# The getter method get_message_text_encrypted(self)
# change_shift(self, shift): Think about what other methods you can use to make this easier.

### Helper code

import string

def load_words(file_name):
    '''
    file_name (string): the name of the file containing
    the list of words to load

    Returns: a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    '''

    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    in_file.close()
    return word_list

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ''' Grader's Implementation of Message Object '''

    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object

        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words("words.txt")
        self.shift_dict = {}

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class

        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class

        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.

        shift (integer): the amount by which to shift every letter of the
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to
                 another letter (string).
        '''
        lower_keys = list(string.ascii_lowercase)
        lower_values = list(string.ascii_lowercase)
        shift_lower_values = lower_values[shift:] + lower_values[:shift]

        upper_keys = list(string.ascii_uppercase)
        upper_values = list(string.ascii_uppercase)
        upper_shift_values = upper_values[shift:] + upper_values[:shift]

        full_keys = lower_keys + upper_keys
        full_values = shift_lower_values + upper_shift_values

        self.shift_dict = dict(zip(full_keys, full_values))
        return self.shift_dict


    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift

        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        new_msg = []
        for i in self.message_text:
            if i not in self.build_shift_dict(shift).keys():
                new_msg.append(i)
                continue
            else:
                new_msg.append(self.build_shift_dict(shift)[i])
        return ''.join(new_msg)

### Helper code End



### Paste your implementation of the `plaintext_message` class here



def main():
    ''' Function to handle testcases '''
    inp = input()
    data = plaintext_message(inp, int(input()))
    print(data.get_shift())
    print(data.get_encrypting_dict())
    print(data.get_message_text_encrypted())
    data.change_shift(int(input()))
    print(data.get_shift())
    print(data.get_encrypting_dict())
    print(data.get_message_text_encrypted())

if __name__ == "__main__":
    main()
