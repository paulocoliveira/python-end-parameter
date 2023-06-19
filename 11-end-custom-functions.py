def log_test_step(step_number, description, result):
    print(f"Step {step_number}: {description}", end=' | ')
    print(f"Result: {result}")

# Usage Example
test_step = 3
step_description = "Click the Login button"
step_result = "Passed"
log_test_step(test_step, step_description, step_result)