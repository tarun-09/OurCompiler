"""
Tests for advanced language features and edge cases.
"""
import pytest

def test_nested_function_closure(run_code):
    code = '''
    कार्य बाह्य(क) {
        कार्य आन्तर(ख) {
            यच्छ क + ख
        }
        यच्छ आन्तर
    }
    फलन = बाह्य(5)
    यच्छ फलन(3)
    '''
    result = run_code(code)
    assert result.value == 8

def test_list_comprehension(run_code):
    code = '''
    सूची = [1, 2, 3, 4, 5]
    नवसूची = []
    प्रति अंक इन सूची {
        यदि अंक % 2 == 0 {
            संकलः(नवसूची, अंक * 2)
        }
    }
    यच्छ नवसूची
    '''
    result = run_code(code)
    assert result.elements == [4, 8]

def test_error_handling(run_code, capture_output):
    code = '''
    कार्य विभाग(क, ख) {
        यदि ख == 0 {
            यच्छ "शून्य-विभाग-दोष"
        }
        यच्छ क / ख
    }
    मुद्रणः(विभाग(10, 0))
    '''
    output, _ = capture_output(code)
    assert "शून्य-विभाग-दोष" in output

def test_recursive_data_structures(run_code):
    code = '''
    कार्य वृक्ष(मूल्य, वाम, दक्षिण) {
        यच्छ {"मूल्य": मूल्य, "वाम": वाम, "दक्षिण": दक्षिण}
    }
    
    वृक्ष1 = वृक्ष(1, वृक्ष(2, लुप्तः, लुप्तः), वृक्ष(3, लुप्तः, लुप्तः))
    यच्छ वृक्ष1["वाम"]["मूल्य"]
    '''
    result = run_code(code)
    assert result.value == 2

def test_function_composition(run_code):
    code = '''
    कार्य द्विगुण(क) {
        यच्छ क * 2
    }
    
    कार्य जोड़_एक(क) {
        यच्छ क + 1
    }
    
    कार्य संयोजन(फ़1, फ़2) {
        कार्य नया_फलन(क) {
            यच्छ फ़1(फ़2(क))
        }
        यच्छ नया_फलन
    }
    
    मिश्रित = संयोजन(द्विगुण, जोड़_एक)
    यच्छ मिश्रित(5)
    '''
    result = run_code(code)
    assert result.value == 12  # ((5 + 1) * 2)
