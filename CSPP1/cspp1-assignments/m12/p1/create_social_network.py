'''
    Assignment-1 Create Social Network
'''

def create_social_network(data_):
    '''
        The data argument passed to the function is a data_
        It represents simple social network data
        In this social network data there are people following other people

        Here is an example social network data data_:
        John follows Bryant,Debra,Walter
        Bryant follows Olive,Ollie,Freda,Mercedes
        Mercedes follows Walter,Robin,Bryant
        Olive follows John,Ollie

        The data_ has multiple lines and each line represents one person
        The first word of each line is the name of the person
        The second word is follows that separates the person from the followers
        After the second word is a list of people separated by ,

        create_social_network function should split the data_ on lines
        then extract the person and the followers by splitting each line
        finally add the person and the followers to a data_onary and
        return the data_onary

        Caution: watch out for trailing spaces while splitting the data_.
        It may cause your test cases to fail although your output may be right

        Error handling case:
        Return a empty data_onary if the data_ format of the data is invalid
        Empty data_onary is not None, it is a data_onary with no keys
    '''
    b_a = input()
    data_ = {}
    keys, values = b_a.split()
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
    data_ = ''
    lines = int(input())
    for i in range(lines):
        i += 1
        data_ += input()
        data_ += '\n'

    print(create_social_network(data_))

if __name__ == "__main__":
    main()
