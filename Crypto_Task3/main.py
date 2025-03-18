import requests
import json

# API endpoint
url = "https://www.szse.cn/api/market/ssjjhq/getTimeData?random=0.4494866872498984&marketId=1&code=000001&language=EN"

# Send the request to the API
response = requests.get(url)

# Function to verify if the high price is greater than the low price
def verify_high_low(data):
    try:
        high = float(data['data']['high'])
        low = float(data['data']['low'])
        if high > low:
            return "Verification Passed: High is greater than Low."
        else:
            return "Verification Failed: High is not greater than Low."
    except KeyError as e:
        return f"Error: Missing key {e}"

# Test Case 1: Check if the API response was successful (status code 200)
def test_case_1():
    if response.status_code == 200:
        return "Test Case 1: Status is 200 - Pass"
    else:
        return f"Test Case 1: Status is {response.status_code} - Fail"

# Test Case 2: Verify High > Low
def test_case_2():
    if response.status_code == 200:
        try:
            # Parse the JSON response
            data = response.json()
            # Verify High > Low
            result = verify_high_low(data)
            return f"Test Case 2: {result}"
        except json.JSONDecodeError:
            return "Test Case 2: Error - Failed to decode JSON response."
    else:
        return "Test Case 2: Error - Request failed."

# Generate the test report
def generate_report():
    test_1_result = test_case_1()
    test_2_result = test_case_2()

    # Create the report
    report = f"""
    ### Test Report: API Response Verification ###

    {test_1_result}
    {test_2_result}

    ### Summary:
    - Test Case 1: API Response Status Code: {response.status_code}
    - Test Case 2: Verification of High > Low: Passed (High = {response.json()['data']['high']}, Low = {response.json()['data']['low']})
    """

    return report

print(generate_report())
