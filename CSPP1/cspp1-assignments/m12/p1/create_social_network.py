'''
    Assignment-1 Create Social Network
'''

def create_social_network(data_):
    '''
        The data argument passed to the function is a string
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data string:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The string has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the string on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a data_onary and
        return the data_onary

        Caution: watch out for trailing spaces while splitting the string.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty data_onary if the string format of the data is invalid
        Empty data_onary is not None, it is a data_onary with no keys
    '''
    line = input()
    b_file = str(input())
    data_ = {}
    for i in range(line):
        keys, values = i.split()
        if keys in data_.keys():
            if values not in data_[keys]:
                data_[keys].append(values)
        else:
            data_[keys] = [values]
    return data_

def main():
    '''
        handling testcase input and printing output
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'

    print(create_social_network(string))

if __name__ == "__main__":
    main()

"""   my_dict = {}
    values = data.split()
    j = 2
    if values[1] != 'follows':
        return my_dict
    for iterate in range(0, lines):
        my_dict[values[iterate*3]] = values[j].split(',')
        j += 3
    return my_dict
def main():
    '''
        handling testcase input and printing output
        problem is to create a dictionary with given data
        params : number of lines and data
        output : will be in a dictionary form based on data given
    '''
    string = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        string += input()
        string += '\n'
    print(create_social_network(string, lines))
if __name__ == "__main__":
    main()"""