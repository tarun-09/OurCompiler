"""
Test configuration and shared fixtures for Sansam language tests.
"""
import pytest
import time
import contextlib
import io
import sys
import os

# Add the project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Sansam.Run import run

@pytest.fixture
def run_code():
    def _run_code(code):
        try:
            print(f"\nExecuting code:\n{code}\n")  # Debug output
            value, error = run("<test>", code)
            if error:
                print(f"Error occurred: {error.as_string()}")  # Debug output
                raise Exception(f"Code execution failed: {error.as_string()}")
            print(f"Result value: {value}")  # Debug output
            return value  # Return just the value, not the Result object
        except Exception as e:
            print(f"Exception occurred: {str(e)}")  # Debug output
            raise
    return _run_code

@pytest.fixture
def measure_performance():
    def _measure(code, iterations=1000):
        # Warm-up run
        run("<test>", code)
        
        # Measure execution time
        start_time = time.time()
        for _ in range(iterations):
            run("<test>", code)
        end_time = time.time()
        
        return (end_time - start_time) / iterations
    return _measure

@pytest.fixture
def capture_output():
    def _capture(code):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result, error = run("<test>", code)
            if error:
                raise Exception(f"Code execution failed: {error.as_string()}")
        return output.getvalue().strip(), result
    return _capture
