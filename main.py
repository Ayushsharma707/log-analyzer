# main.py

from log_parser import parse_log_file
import os

def main():
    log_files = ['embedded_log.txt', 'selenium_log.txt']
    for log_file in log_files:
        print(f"\nAnalyzing: {log_file}")
        filepath = os.path.join('logs', log_file)
        summary = parse_log_file(filepath)

        # Print summary
        for key, value in summary.items():
            if key != 'TEST_CASES':
                print(f"  {key}: {value}")
        

if __name__ == '__main__':
    main()
