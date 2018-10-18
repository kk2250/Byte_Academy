from pprint import pprint

def readcurrency(filename):
    currency_list = []
    currency_dictionary1 = []
    currency = []
    convert = []
    with open(filename, 'r') as f:
        for line in f:
            for word, word1 in line.split():
                print(word1)
                print(word)
                currency_list.append(word)
    a = len(currency_list)
    for i in range(0, a):
        if i%2 == 0:
            currency.append(currency_list[i])
        else:
            convert.append(currency_list[i])
    b = len(convert)
    for j in range(0,b):
        currency_dictionary = {'symbol' : currency[j],'rate' : float(convert[j])}
        currency_dictionary1.append(currency_dictionary)

    return currency_dictionary1
pprint(readcurrency('currency.txt'))


# x, y = line.split()
# dict = {'i' : x , 'j' : y}


# from pprint import pprint

# def readcurrency(filename):
#     currency_list = []
#     currency_dictionary = {}
#     currency = []
#     convert = []

#     with open(filename, 'r') as f:
#         for line in f:
#             for word in line.split():
#                 currency_list.append(word)
#     a = len(currency_list)
#     for i in range(0, a):
#         if i%2 == 0:
#             currency.append(currency_list[i])
#         else:
#             convert.append(currency_list[i])
#     b = len(convert)
    
#     """
#     This is creating a dictionary that contains two strings, separated by ':'
#     instead of a dictionary with two entries with key-value pairs:
#     currency_dictionary = {('symbol : ' + currency[j]):('rate : ' + convert[j])for j in range(0,b)}
#         --Greg
#     """
#     final_list_of_dicts = []

#     for _ in range(b):
#         # This creates a dictionary that has keys and values correctly
#         currency_dictionary = {'symbol':currency[_], 'rate':float(convert[_])}
#         final_list_of_dicts.append(currency_dictionary)


#     return final_list_of_dicts
# pprint(readcurrency('currency.txt'))