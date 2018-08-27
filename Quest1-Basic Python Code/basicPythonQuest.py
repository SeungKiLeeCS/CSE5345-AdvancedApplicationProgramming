# Basic Python Quest
# When returning lists of values, order is not important unless specified

__STUDENT_ID__  = "35460312"     # replace with your 8 digit student id
__CODING_NAME__ = "MonsterPeach"        # replace with your coding name -

def isSorted(list):
    """ return boolean depending on if list sorted
    >>> isSorted([2,4,7,7,99,122]) -> True
    >>> isSorted(['a','b','c'])  -> True
    >>> isSorted(['a','z','b','c'])  -> False
    constraint: MAY NOT USE: sorted( ) function or sort library
    """

    for i in range (len(list)-1):
        if list[i] > list[i+1]:
            return False
    return True

def isSortedAndUnique(list):
    """ return boolean depending on if list sorted
    >>> isSortedAndUnique([2,4,7,7,99,122]) -> False
    >>> isSortedAndUnique(['a','b','c'])  -> True
    >>> isSortedAndUnique(['a','z','b','b','c'])  -> False
    constraint: MAY NOT USE: set
    """
    return isSorted(list) and hasUniqueValues(list)

def hasUniqueValues(list):
    """ return boolean depending on if list has unique values
    >>> hasUniqueValues([2,4,7,99,122,7]) -> False
    >>> hasUniqueValues(['a','b','c'])  -> True
    >>> hasUniqueValues(['a','z','b','b','c'])  -> False
    constraint: MAY NOT USE: set
    """
    return len({}.fromkeys(list)) == len(list)

def genSortedArrayUniqueValues(list):
    """ return sorted version of list without duplicates
    >>> genSortedArrayUniqueValues([2,4,7,7,122,99]) -> [2,4,7,99,122]
    >>> genSortedArrayUniqueValues(['a','b','z','c', 'a'])  -> ['a','b','c','z']
    constraint: MAY NOT USE: set
    """

    return_list = []
    
    for key in {}.fromkeys(list):
        return_list.append(key)
    
    return sorted(return_list)

def listToMapTwoByTwo(list):
    """ return a map based on the order of list elements.
    >>> listToMapTwoByTwo(['foo','bar'])     ->  {"foo":"bar"}
    >>> listToMapTwoByTwo(['a',2, 3,'foo'])  ->  {"a":2,3:'foo'}
    >>> listToMapTwoByTwo([])  -> {}
    """

    return_dict = {}
    
    if len(list) > 1:
        for i in range (len(list)-1):
            if i%2 == 0:
                return_dict[list[i]] = list[i+1]
    
    return return_dict    

def wordsInStringToDictWordCount(str):
    """ return a dict of words in string and count
    >>> wordsInStringToDictWordCount('foo bar   bar') -> {'foo':1, 'bar':2}
    >>> wordsInStringToDictWordCount('') -> {}
    constraint: MAY NOT USE: Counter
    """

    return_dict = {}

    if len(str) > 1:        
        temp_list = str.split()
        
        for i in temp_list:
            if i in return_dict:
                return_dict[i] += 1
            else:
                return_dict[i] = 1
                
    return return_dict

def reverseWordsInString(str):
    """ return a string with words reversed with one space separators
    >>> reverseWordsInString('foo bar bar baz') -> 'baz bar bar foo'
    constraint: MAY NOT USE: list.reverse()
    """

    temp_list = str.split()
    temp_list = temp_list[::-1]
    
    return ' '.join(temp_list)


def genListOfOverlaps(list1, list2):
    """ return list of values appearing in both lists
    >>> genListOfOverlaps([2,4,6,8],[6,2,2,9,7]) -> [2,6]
    >>> genListOfOverlaps([2,4,6,8],[2,4,6,8]) -> [2,4,6,8]
    >>> genListOfOverlaps([2,4,6,8],[1,1,9,7]) -> []
    """

    return_list = []
    temp_dict = {}
    
    for i in list1:
        if i not in temp_dict:
            temp_dict[i] = 1
    for i in {}.fromkeys(list2):
        if i in temp_dict:
            temp_dict[i] += 1
        else:
            temp_dict[i] = 1

    for key in temp_dict:
        if temp_dict[key] == 2:
            return_list.append(key)
            
    return sorted(return_list)

def removeDupsNoSet(list):
    """ remove duplicates in the list without using Python Set
    >>> removeDupsNoSet([1,1,2,2,5,6]) -> [1,2,5,6]
    constraint: MAY NOT USE: set
    """

    return_list = []
    
    for i in {}.fromkeys(list):
        return_list.append(i)
    
    return return_list

def removeDupsUseSet(list1):
    """ remove duplicates in the list  using Python Set
    >>> removeDupsUseSet([1,1,2,2,5,6]) -> [1,2,5,6]
    constraint: MUST USE: set
    """

    return list(set(list1))

if __name__ == '__main__':
    #write your own test code here
    print ('ready to go')