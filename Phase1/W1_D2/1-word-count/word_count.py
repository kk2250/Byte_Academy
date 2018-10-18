from operator import itemgetter
from collections import Counter

def word_counts(filename, n):
    counter = Counter()
    # use counter
    words = []
    repeating = []
# use dictionary - use counter in this case
    with open(filename, 'r') as input_file:
        for line in input_file:
            for word in line.split():
                lower_word = word.lower()
                if lower_word in words:
                    repeating.append(lower_word)
                else:
                    words.append(lower_word)

    # print(words)
    # print(repeating)
    a = len(words)
    c = len(repeating)
    arr_count = []
    for x in range(0, a):
        y = repeating.count(words[x])
        arr_count.append(y)
    


    print(arr_count)
    # b = len(arr_count)

    # print(a)
    # print(c)
    # print(b)
    # print(arr_count)


    # z = max(arr_count)
    # print(z)
    # b = len(arr_count)
    # for z in range(0, b):
    #     arr_count[z] 




if __name__ == "__main__":
    wcounts = word_counts('article.txt', 5)
    # now how do you display your data?
