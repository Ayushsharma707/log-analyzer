# log_parser.py

import re

def parse_log_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    log_data = {
        'INFO': 0,
        'WARNING': 0,
        'ERROR': 0,
        'PASS': 0,
        'FAIL': 0,
        'TEST_CASES': []
    }

    for line in lines:
        if '[INFO]' in line:
            log_data['INFO'] += 1
        if '[WARNING]' in line:
            log_data['WARNING'] += 1
        if '[ERROR]' in line:
            log_data['ERROR'] += 1
        if '[PASS]' in line:
            log_data['PASS'] += 1
        if '[FAIL]' in line:
            log_data['FAIL'] += 1
        match = re.search(r'test_[\w]+', line)
        if match:
            log_data['TEST_CASES'].append(match.group())

    return log_data
