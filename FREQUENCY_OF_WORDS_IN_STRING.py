#Taking String Input
string = str(input('Enter the string: '))
#Defining empty dictionary
dictionary = {}
for word in string.split():
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1
#Printing the dictionary with frequecy of words in string
print(dictionary)
