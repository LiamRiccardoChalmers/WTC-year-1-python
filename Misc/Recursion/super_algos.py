
def find_min(element):
    """ Finds the smallest numeric value in an array
    if the array contains non numeric characters it returns -1
    """

    for x in (element):
        if type(x) != int:
            return(-1)
    if not(element):
        return(-1)
    else:
        if len(element)==2:
            if element[0] < element[1]:
                return element[0]
            else:
                return element[1]
        elif len(element)==1:
            return element[0]
        else:
            X = find_min(element[1:])
            if element[0]<X:
                return element[0]
            else:
                return X


def sum_all(element):
    """ 
adds all the numeric chracters in a list
if the array contains non numeric characters it returns -1
    """
    for x in (element):
        if type(x) != int:
            return(-1)
    if not(element):
        return(-1)
    else:
        theSum = 0
        for i in element:
            theSum = theSum + i
        return theSum



def find_possible_strings(character_set, n):
    """ Handles all the error checks for my permutaions fucntion
        * If the list is empty or the length of the permutaion is 0 return an empty list
        * if the permutaion lenght is 1 return the list of chracters
        * Other wise run the recursive program
    """
    list1 = list()

    for x in character_set:
        if type(x) != str:
            return list1
    if len(character_set) == 0 or n == 0:
        return list1
    else:
        possible_strings_recursive(character_set, "", len(character_set), n, list1)
        return list1

def possible_strings_recursive(character_set, prefix, size, n, list1):
    """ Recursively loop and find the permutations of a list of chracters to a set length
        requiries a new prefix which is just the chracter in the list at index i for i in the length of the list
    """

    if n == 0:
        list1.append(prefix)
        return
    for i in range(size):
        new_prefix = prefix + character_set[i]
        possible_strings_recursive(character_set, new_prefix, size, n - 1, list1)


   
#print(sum_all([1,-10,6,-80,100]))
#print(find_min([1.5,20,15,20,30]))
#print(find_possible_strings(['a','b'], 1))

