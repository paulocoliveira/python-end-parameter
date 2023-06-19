def generate_test_report(test_results):
    print("Test Report")
    print("-----------")

    for result in test_results:
        print("Test Case:", end='\t')
        print(f"{result['test_case']}", end='\t\t')
        print("Status:", end=' ')
        print(f"{result['status']}")

# Usage Example
test_results = [
    {"test_case": "Login Test", "status": "Passed"},
    {"test_case": "Logout Test", "status": "Failed"},
    {"test_case": "Search Test", "status": "Passed"},
]
generate_test_report(test_results)
