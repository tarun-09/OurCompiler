"""
Tests for basic arithmetic operations and variable assignments.
"""
import pytest

def test_simple_print(run_code, capture_output):
    """Test if printing a number works"""
    output, result = capture_output('मुद्रणः(5)')
    assert output == "5"

def test_simple_addition(run_code, capture_output):
    """Test basic addition with print"""
    output, result = capture_output('मुद्रणः(2 + 2)')
    assert output == "4"

def test_variable_assignment(run_code, capture_output):
    """Test variable assignment and printing"""
    code = '''
क = 5
मुद्रणः(क)
'''
    output, result = capture_output(code)
    assert output == "5"

def test_variable_addition(run_code, capture_output):
    """Test addition with variables and printing"""
    code = '''
क = 3
ख = 4
मुद्रणः(क + ख)
'''
    output, result = capture_output(code)
    assert output == "7"
