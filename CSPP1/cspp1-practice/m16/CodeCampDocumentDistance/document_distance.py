'''
    Document Distance - A detailed description is given in the PDF
'''
import math

def similarity(dict1, dict2, final_words):
    '''
        Compute the document distance as given in the PDF
    '''
    temp1 = 0
    temp2 = 0
    temp3 = 0
    dictionary = {}
    for i_ in final_words:
        dictionary[i_] = [dict1.count(i_),dict2.count(i_)]
    for j_ in dictionary:
        temp1 += dictionary[j_][0]*dictionary[j_][1]
    for j_ in dictionary:
        temp2 += dictionary[j_][0]**2
    for j_ in dictionary:
        temp3 += dictionary[j_][1]**2
    return temp1/math.sqrt(temp2*temp3)

def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = []
    with open(filename, 'r') as filename_:
        for line in filename_:
            stopwords.append(line.strip())
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    words1 = input1.lower()#string
    for i_ in words1:
        if i_ in "1234567890!@#$%^&*()?~/'":
            words1.replace(i_,'')
    words1 = words1.split()# converts into list after split
    input2 = input()
    words2 = input2.lower().strip()#string
    for i_ in words2:
        if i_ in "1234567890!@#$%^&*()?~/'":
            words2.replace(i_,'')
    words2 = words2.split()# converts into list after split

    stopwords = load_stopwords('stopwords.txt')
    words1 = [word for word in words1 if word not in stopwords]
    words2 = [word for word in words2 if word not in stopwords]    
    
    final_words = list(set(words1).union(set(words2)))
    print(similarity(words1, words2, final_words))

if __name__ == '__main__':
    main()
