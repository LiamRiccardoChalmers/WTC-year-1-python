
def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    """
    converts a string into aa list of the words while removing the whitespace
    and punctution chracters
    """
    white_space_list = [' ','.',',',';','.','?']
    text_list = []
    for p in text:
        if p in white_space_list:
            text = text.replace(p, f" {p} ")
        else:
            pass
        text = text.replace("  ", " ")
        text = text.lower()
        text_list = text.split(" ")
    for i,x in enumerate(text_list):
        if x in white_space_list:
            del text_list[i]
        else:
            pass
    return list(filter(lambda x: x, text_list))


def words_longer_than(length, text):
    text_list = convert_to_word_list(text)
    new_list = list()
    for x in text_list:
        if len(x) > length:
            new_list.append(x)
        else:
            pass
    return new_list


def words_lengths_map(text):
    """
    takes a string and converts it into a map of word lenths and the 
    occurence of each starting from the words with the shortest length
    """
    text_list = convert_to_word_list(text)
    d = {}
    od = {}
    for i in text_list:           #Split by space
        l = len(i)
        if l not in d:            #Create len as key
            d[l] = 1
        else:
            d[l] +=1
        ordered = sorted(d.items(), key=lambda x: x[0], reverse = False)
        od = dict(ordered)
    return od


def letters_count_map(text):
    """
    creates a map with all the alphabet chracaters and then counts the 
    occurence of them in a given string
    """
    import string
    letter_dictionary = dict.fromkeys(string.ascii_lowercase, 0)
    text = text.lower()
    for letter in letter_dictionary:
        if letter_dictionary[letter] == 0:
            letter_dictionary[letter] = text.count(letter)
    return letter_dictionary


def most_used_character(text):
    """
    searches through a map of a letters occurence in a string and returbs the 
    first most used chracter
    """
    letterCounts = letters_count_map(text)
    maximum = 0
    max_key = None
    if text:
        for k in letterCounts:
            if letterCounts[k] > maximum:
                maximum = letterCounts[k]
                max_key = k
        return max_key
    else:
        return None
