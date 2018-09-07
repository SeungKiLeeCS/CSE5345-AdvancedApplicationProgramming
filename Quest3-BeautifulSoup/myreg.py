import re

def validEmail(address):
    # If None, return false -> no match
    return re.match(r'^[A-Za-z0-9][A-Za-z0-9\.]*[A-Za-z0-9]@{1}[a-zA-Z]{1}[A-Za-z\_]*[a-zA-Z]\.{1}[edu|org|com]', address) is not None