"""
Tests for data structures (lists, dictionaries) and their operations.
"""
import pytest

def test_list_creation(run_code):
    code = '''
    सूची = [1, 2, 3, 4, 5]
    यच्छ सूची
    '''
    result = run_code(code)
    assert result.elements == [1, 2, 3, 4, 5]

def test_list_access(run_code):
    code = '''
    सूची = [10, 20, 30, 40]
    यच्छ सूची[2]
    '''
    result = run_code(code)
    assert result.value == 30

def test_list_append(run_code):
    code = '''
    सूची = [1, 2, 3]
    संकलः(सूची, 4)
    यच्छ सूची
    '''
    result = run_code(code)
    assert result.elements == [1, 2, 3, 4]

def test_list_pop(run_code):
    code = '''
    सूची = [1, 2, 3, 4]
    पोप(सूची)
    यच्छ सूची
    '''
    result = run_code(code)
    assert result.elements == [1, 2, 3]

def test_list_extend(run_code):
    code = '''
    सूची1 = [1, 2]
    सूची2 = [3, 4]
    अतिसृ(सूची1, सूची2)
    यच्छ सूची1
    '''
    result = run_code(code)
    assert result.elements == [1, 2, 3, 4]

def test_dictionary_creation(run_code):
    code = '''
    कोश = {"क": 1, "ख": 2}
    यच्छ कोश
    '''
    result = run_code(code)
    assert result.elements == {"क": 1, "ख": 2}

def test_dictionary_access(run_code):
    code = '''
    कोश = {"नाम": "राम", "आयु": 25}
    यच्छ कोश["नाम"]
    '''
    result = run_code(code)
    assert str(result.value) == "राम"
