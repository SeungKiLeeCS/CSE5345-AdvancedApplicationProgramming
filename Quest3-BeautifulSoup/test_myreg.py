# Testfile for basicPythonQuest.py
import pytest
import myreg


# TESTS   

# Test for Local

# Regular
def test_validlocal1():
    assert myreg.validEmail("abc@smu.edu") == True

# dots between
def test_validlocal2():
    assert myreg.validEmail("a.b.c@smu.edu") == True

# dot at start -> false
def test_validlocal3():
    assert myreg.validEmail(".abc@smu.edu") == False

# dot at end -> false
def test_validlocal4():
    assert myreg.validEmail("abc.@smu.edu") == False

# Captial Letters
def test_validlocal5():
    assert myreg.validEmail("a.Bc@smu.edu") == True

def test_validlocal6():
    assert myreg.validEmail("Ab.c@smu.edu") == True

# Start/end with underscore -> false
def test_validlocal7():
    assert myreg.validEmail("_b.c_@smu.edu") == False


# Test for @

def test_symbol0():
    assert myreg.validEmail("abc@@smu.edu") == False

def test_symbol1():
    assert myreg.validEmail("abc2smu.edu") == False

def test_symbol2():
    assert myreg.validEmail("abc!smu.edu") == False

def test_symbol3():
    assert myreg.validEmail("abcsmu.edu") == False

# Test for domain1

# _ in the middle
def test_fdomain1():
    assert myreg.validEmail("abc@s_m_u.edu") == True

# _ start -> false
def test_fdomain2():
    assert myreg.validEmail("abc@_smu.edu") == False

# _ end -> false
def test_fdomain3():
    assert myreg.validEmail("abc@s_m_u_.edu") == False

# number in domain -> false
def test_fdomain4():
    assert myreg.validEmail("abc@s8u.edu") == False

# special char in domain -> false
def test_fdomain5():
    assert myreg.validEmail("abc@s_m!u.edu") == False

# Test for domain2

def test_sdomain1():
    assert myreg.validEmail("abc@smu.org") == True

def test_sdomain2():
    assert myreg.validEmail("abc@smu.com") == True

def test_sdomain3():
    assert myreg.validEmail("abc@smu.kr") == False

# Final Test -> Something convoluted and wierd but fitting the email description
def test_final():
    assert myreg.validEmail("This.can.be.1@Email_that_wilL_Satisfy_the_requirements.com") == True

if __name__ == '__main__':
    print("Testing my_regex.py")
    pytest.main()
    

