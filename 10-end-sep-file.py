def log_test_result(test_case, result):
    with open("test.log", "a") as file:
        print("Test case:", test_case, "Result:", result, sep=' | ', end='\n', file=file)

# Usage Example
test_case = "Login Test"
result = "Passed"
log_test_result(test_case, result)