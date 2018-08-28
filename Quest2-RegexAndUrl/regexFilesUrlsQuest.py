#Quest: Regex, Files, Urls

import re, pytest, requests


__STUDENT_ID__  = "35460312"        # replace with your 8 digit student id
__QUEST_NAME__ = "QUEST2"           # QUEST NAME
__CODING_NAME__ = "MonsterPeach"           # replace with your coding name - max 15 characters

def count_vowels(mystr):
    """return the number of vowels, upper and lowercase a,e,i,o,u in the string
    >>> count_vowels('aaacvemmikkOOzzuU')  -> 9
    """
    
    mystr = mystr.lower()
    vowel_list = re.findall(r'[aiueo]', mystr)    
    return len(vowel_list)

def is_valid_python_hex(mystr):
    """is string a valid hex: begins with 0x and contains only 0-9 and A-F (lower or upper)
     >>> is_valid_python_hex('0x1A2f') -> True
     >>> is_valid_python_hex('x1A2f')  -> False
     >>> is_valid_python_hex('0x1A2G') -> False
    """
    mystr = mystr.lower()
    if re.match(r'^[0x]{2}[a-f0-9]{4}$', mystr) is None:
        return False
    return True

def has_vowel(mystr):
    """   return True if a vowel upper or lowercase in string
    >>> has_vowel("zcxvsd")     -> False
    >>> has_vowel("vcbxvefjk")  -> True
    """
    mystr = mystr.lower()
    if re.search(r'[aiueo]', mystr) is None:
        return False
    return True

def is_integer(mystr):
    """ returns True if integer with optional minus sign
    >>> is_integer("2345")     -> True
    >>> is_integer("-192345")  -> True
    >>> is_integer("234x5")    -> False
    """
    if re.search(r'^[\-]?[0-9]*$', mystr) is not None:
        return True
    return False

def get_extension(mystr):
    """ returns the extension for a filename or 'NONE' if no extension
    >>> get_extension('foo.zip')     -> 'zip'
    >>> get_extension('foo.doc.txt') -> 'txt'
    >>> get_extension('foozip')      -> 'NONE'
    """
    
    extension_type = re.search(r'[\.]{1}.\w*$', mystr)
    if extension_type is not None:
        return extension_type.group(0)[1:]
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

    if re.search(r'^[\-]?[0-9]*[\.]?[0-9]*[\.]?$', mystr) is not None:
        return True
    return False
    
def convert_date_format(mystr):
    """ convert date format YYYY-MO-DAY  TO MO-DAY-YYYY. If not in date format
        return "NONE" . Check only 4 digits for year and 2 digits for MO and DAY
    >>> convert_date_format('2018-03-04')  -> '03-04-2018'
    >>> convert_date_format('2018.03-04')  -> 'NONE'
    >>> convert_date_format('2018-03-054') -> 'NONE'
    """
    return_str = 'NONE'
    date_format = re.search(r'^\d{4}\-\d{2}\-\d{2}$',mystr)
    if date_format is not None:
        return_str = date_format.group(0)[5:7] + '-' + date_format.group(0)[8:10] + '-' + date_format.group(0)[0:4]
    return return_str


#File functions
def readFileCountLines(filename):
    """use download file from Canvas: pytestFile1.txt - return number of lines
    >>> readFileCountLines('pytestFile1.txt')  -> 4
    """
    with open(filename, 'r') as f:
        return_count = sum(1 for newline in f)
    f.close()
    return return_count
    
def readFileCountStringOccurrences(filename, stringval):
    """read file: pyTestFile1.txt  - return number of times  stringval appears
    >>> readFileCountStringOccurrences('pytestFile1.txt','rollo')  -> 3
    """
    word_count = 0
    with open(filename, 'r') as f:
        for word in f.read().split():
            if word.lower() == stringval:
                word_count += 1
        f.close()
        return word_count

def readFileSumDigitsGreaterThanNumber(filename, number):
    """e.g. file = "hello22world2100and18and 1000", number =999 -> 3100
     >>> readFileSumDigitsGreaterThanNumber('pytestFile1.txt',15)  -> 88
    """
    return_num = 0
    with open(filename, 'r') as f:
        text = f.read().lower()
        for num in text.split(): 
                if num.isdigit() and int(num) > number:
                    return_num += int(num)
        
        f.close()
        return return_num

def remove_all_but_alpha(mystr):
    """ remove all characters that are not alpha a-z A-Z
    >>> remove_all_but_alpha('hey-99-where8isthe**big_table**') -> 'heywhereisthebigtable'
    """
    mystr = re.sub(r'[^a-zA-Z]*','', mystr)
    return mystr


#URL functions
def readurlCountStringOccurrences(urlname, stringval):
    """return number of times  stringval appears in text of url - ignore case
     >>> readurlCountStringOccurrences('http://s2.smu.edu/~coyle/testurls/foo.txt','rollo')  -> 3
    """
    word_count = 0
    uf = requests.get(urlname).text.split()
    
    for word in uf:
        if word.lower() == stringval:
            word_count += 1
    
    return word_count

def readurlCountValidPhoneNumbers(urlname):
    """return count of valid phone number formats: no separator, dash separator, period separator:
    valid: 2126663333, 212-666-3333, 212.666.3333
    invalid: 212-444.5555, 212.333-4444, 212, 6363636363636
    >>> readurlCountValidPhoneNumbers('http://s2.smu.edu/~coyle/testurls/foo.txt')  -> 3
    """
    valid_count = 0
    uf = requests.get(urlname).text.split()
    for word in uf:
        if re.search(r'\d{3}(\-|\.)?\d{3}\1?\d{4}\1?', word) is not None:
            valid_count += 1
    return valid_count