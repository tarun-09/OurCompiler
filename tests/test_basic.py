import pytest
from Sansam.Run import run

def test_basic_arithmetic():
    code = '''
क = 5
ख = 3
योग = क + ख
'''
    result, error = run("<test>", code)
    assert error is None
    assert result.value == 8

def test_print_statement():
    code = 'मुद्रणः("test")'
    result, error = run("<test>", code)
    assert error is None

def test_if_statement():
    code = '''
क = 10
यदि क > 5 {
    यच्छ 1
} चेत् {
    यच्छ 0
}
'''
    result, error = run("<test>", code)
    assert error is None
    assert result.value == 1
