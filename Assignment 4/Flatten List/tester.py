import sys
import json
import subprocess

def run_script(script, input_data):
    process = subprocess.Popen(['python', script], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input=input_data)
    return stdout.strip(), stderr.strip()

def main():
    if len(sys.argv) != 3:
        print("Usage: python tester.py <script.py> <io.json>")
        sys.exit(1)

    script_file = sys.argv[1]
    io_file = sys.argv[2]

    with open(io_file, 'r') as f:
        test_cases = json.load(f)

    for test_case in test_cases:
        input_data = test_case['input']
        expected_output = test_case['output']

        actual_output, error = run_script(script_file, input_data)

        print(f"Input: {input_data}")
        print(f"Expected Output: {expected_output}")
        print(f"Actual Output: {actual_output}")
        if error:
            print(f"Error: {error}")
        print()

if __name__ == "__main__":
    main()