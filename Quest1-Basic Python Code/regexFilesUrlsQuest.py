#Quest: Regex, Files, Urls

import re, pytest

__STUDENT_ID__  = "00006666"        # replace with your 8 digit student id
__CODING_NAME__ = "Zondo"           # replace with your coding name - max 15 characters

def count_vowels(mystr):
    """return the number of vowels, upper and lowercase a,e,i,o,u in the string
    >>> count_vowels('aaacvemmikkOOzzuU')  -> 9
    """
    return 2

def is_valid_python_hex(mystr):
    """is string a valid hex: begins with 0x and contains only 0-9 and A-F (lower or upper)
     >>> is_valid_python_hex('0x1A2f') -> True
     >>> is_valid_python_hex('x1A2f')  -> False
     >>> is_valid_python_hex('0x1A2G') -> False
    """
    return True

def has_vowel(mystr):
    """   return True if a vowel upper or lowercase in string
    >>> has_vowel("zcxvsd")     -> False
    >>> has_vowel("vcbxvefjk")  -> True
    """
    return True

def is_integer(mystr):
    """ returns True if integer with optional minus sign
    >>> is_integer("2345")     -> True
    >>> is_integer("-192345")  -> True
    >>> is_integer("234x5")    -> False
    """
    return True

def get_extension(mystr):
    """ returns the extension for a filename or 'NONE' if no extension
    >>> get_extension('foo.zip')     -> 'zip'
    >>> get_extension('foo.doc.txt') -> 'txt'
    >>> get_extension('foozip')      -> 'NONE'
    """
    return 'NONE'

def is_number(mystr):
    """ floating point number with optional - sign and optional decimal point
    >>> is_number('234')        -> True
    >>> is_number('-234')       -> True
    >>> is_number('234.')       -> True
    >>> is_number('234.999')    -> True
    >>> is_number('234.99.77')  -> False
    >>> is_number('234a.88')    -> False
    """
    return True

def convert_date_format(mystr):
    """ convert date format YYYY-MO-DAY  TO MO-DAY-YYYY. If not in date format
        return "NONE" . Check only 4 digits for year and 2 digits for MO and DAY
    >>> convert_date_format('2018-03-04')  -> '03-04-2018'
    >>> convert_date_format('2018.03-04')  -> 'NONE'
    >>> convert_date_format('2018-03-054') -> 'NONE'
    """
    return 'NONE'



#File functions
def readFileCountLines(filename):
    """use download file from Canvas: pytestFile1.txt - return number of lines
    >>> readFileCountLines('pytestFile1.txt')  -> 4
    """

    return 4

def readFileCountStringOccurrences(filename, stringval):
    """read file: pyTestFile1.txt  - return number of times  stringval appears
    >>> readFileCountStringOccurrences('pytestFile1.txt','rollo')  -> 3
    """
    return 100

def readFileSumDigitsGreaterThanNumber(filename, number):
    """e.g. file = "hello22world2100and18and 1000", number =999 -> 3100
     >>> readFileSumDigitsGreaterThanNumber('pytestFile1.txt',15)  -> 88
    """

    return 100

def remove_all_but_alpha(mystr):
    """ remove all characters that are not alpha a-z A-Z
    >>> remove_all_but_alpha('hey-99-where8isthe**big_table**') -> 'heywhereisthebigtable'
    """
    return 'xyz'

#URL functions
def readurlCountStringOccurrences(urlname, stringval):
    """return number of times  stringval appears in text of url - ignore case
     >>> readurlCountStringOccurrences('http://s2.smu.edu/~coyle/testurls/foo.txt','rollo')  -> 3
    """
    return 100

def readurlCountValidPhoneNumbers(urlname):
    """return count of valid phone number formats: no separator, dash separator, period separator:
    valid: 2126663333, 212-666-3333, 212.666.3333
    invalid: 212-444.5555, 212.333-4444, 212, 6363636363636
    >>> readurlCountValidPhoneNumbers('http://s2.smu.edu/~coyle/testurls/foo.txt')  -> 3
    """
    return 100



if __name__  == '__main__':
    print ("To test your code execute: python test_QuestFilesUrls.py  or on command line execute: pytest ")



