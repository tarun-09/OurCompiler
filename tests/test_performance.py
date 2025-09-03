"""
Performance tests for Sansam language features.
"""
import pytest

def test_arithmetic_performance(measure_performance):
    code = '''
    क = 1
    ख = 2
    यच्छ क + ख * (क + ख) / (क - ख + 3)
    '''
    avg_time = measure_performance(code)
    assert avg_time < 0.001  # Should execute in less than 1ms

def test_loop_performance(measure_performance):
    code = '''
    योग = 0
    क = 0
    यावद् क < 100 {
        योग = योग + क
        क = क + 1
    }
    यच्छ योग
    '''
    avg_time = measure_performance(code, iterations=100)
    assert avg_time < 0.01  # Should execute in less than 10ms

def test_function_call_performance(measure_performance):
    code = '''
    कार्य फिब(न) {
        यदि न <= 1 {
            यच्छ न
        }
        यच्छ फिब(न-1) + फिब(न-2)
    }
    यच्छ फिब(10)
    '''
    avg_time = measure_performance(code, iterations=10)
    assert avg_time < 0.1  # Should execute in less than 100ms

def test_list_operation_performance(measure_performance):
    code = '''
    सूची = []
    क = 0
    यावद् क < 1000 {
        संकलः(सूची, क)
        क = क + 1
    }
    यच्छ सूची
    '''
    avg_time = measure_performance(code, iterations=10)
    assert avg_time < 0.1  # Should execute in less than 100ms

@pytest.mark.benchmark
def test_memory_intensive_operations(measure_performance):
    code = '''
    सूची = []
    क = 0
    यावद् क < 10000 {
        सूची2 = [क, क+1, क+2]
        संकलः(सूची, सूची2)
        क = क + 1
    }
    यच्छ सूची[9999]
    '''
    avg_time = measure_performance(code, iterations=5)
    assert avg_time < 1.0  # Should execute in less than 1s
