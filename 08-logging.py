def log_test_result(test_case, result, timestamp):
    print("[LOG]", end=' ')
    print(f"Test Case: {test_case}", end=' | ')
    print(f"Result: {result}", end=' | ')
    print(f"Timestamp: {timestamp}")

# Usage Example
test_case = "Login Test"
result = "Passed"
timestamp = "2023-06-18 10:23:45"
log_test_result(test_case, result, timestamp)
