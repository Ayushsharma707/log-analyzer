# log_report.py

import csv

def generate_report(log_summary, report_path):
    with open(report_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Log Type', 'Count'])
        for key, value in log_summary.items():
            if key != 'TEST_CASES':
                writer.writerow([key, value])
        writer.writerow([])
        writer.writerow(['Extracted Test Cases'])
        for case in log_summary['TEST_CASES']:
            writer.writerow([case])
