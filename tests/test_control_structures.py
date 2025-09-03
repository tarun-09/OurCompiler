"""
Tests for control structures (if, while, for).
"""
import pytest

def test_if_statement(run_code):
    code = '''
    क = 10
    यदि क > 5 {
        यच्छ 1
    } चेत् {
        यच्छ 0
    }
    '''
    result = run_code(code)
    assert result.value == 1

def test_if_else_statement(run_code):
    code = '''
    क = 3
    यदि क > 5 {
        यच्छ 1
    } चेत् {
        यच्छ 0
    }
    '''
    result = run_code(code)
    assert result.value == 0

def test_if_elif_else(run_code):
    code = '''
    क = 5
    यदि क > 10 {
        यच्छ "बृहत्"
    } नोचेत् क == 5 {
        यच्छ "समम्"
    } चेत् {
        यच्छ "लघु"
    }
    '''
    result = run_code(code)
    assert str(result.value) == "समम्"

def test_while_loop(run_code):
    code = '''
    क = 0
    योग = 0
    यावद् क < 5 {
        योग = योग + क
        क = क + 1
    }
    यच्छ योग
    '''
    result = run_code(code)
    assert result.value == 10

def test_while_with_break(run_code):
    code = '''
    क = 0
    योग = 0
    यावद् क < 10 {
        यदि क == 5 {
            विघ्नः
        }
        योग = योग + क
        क = क + 1
    }
    यच्छ योग
    '''
    result = run_code(code)
    assert result.value == 10

def test_while_with_continue(run_code):
    code = '''
    क = 0
    योग = 0
    यावद् क < 5 {
        क = क + 1
        यदि क == 3 {
            अनुवर्तते
        }
        योग = योग + क
    }
    यच्छ योग
    '''
    result = run_code(code)
    assert result.value == 12  # 1 + 2 + 4 + 5
