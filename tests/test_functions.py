"""
Tests for functions and function calls.
"""
import pytest

def test_simple_function(run_code):
    code = '''
    कार्य योगः(क, ख) {
        यच्छ क + ख
    }
    यच्छ योगः(5, 3)
    '''
    result = run_code(code)
    assert result.value == 8

def test_nested_function_calls(run_code):
    code = '''
    कार्य गुणनम्(क, ख) {
        यच्छ क * ख
    }
    कार्य वर्गः(क) {
        यच्छ गुणनम्(क, क)
    }
    यच्छ वर्गः(4)
    '''
    result = run_code(code)
    assert result.value == 16

def test_recursive_function(run_code):
    code = '''
    कार्य क्रमगुणनम्(क) {
        यदि क <= 1 {
            यच्छ 1
        }
        यच्छ क * क्रमगुणनम्(क - 1)
    }
    यच्छ क्रमगुणनम्(5)
    '''
    result = run_code(code)
    assert result.value == 120

def test_function_with_default_return(run_code):
    code = '''
    कार्य रिक्तम्() {
    }
    यच्छ रिक्तम्()
    '''
    result = run_code(code)
    assert result.value == None

def test_function_scope(run_code):
    code = '''
    क = 10
    कार्य परीक्षणम्() {
        क = 20
        यच्छ क
    }
    परीक्षणम्()
    यच्छ क
    '''
    result = run_code(code)
    assert result.value == 20  # Test if function can modify global variable
