# 🔍 TestLog Analyzer

**TestLog Analyzer** is a Python-based tool to automatically scan and summarize logs generated during testing of embedded systems or Selenium-based automation tests.

This project helps testers and developers quickly get an overview of:
- How many logs were generated at each severity level
- Whether tests passed or failed
- Common warning or error indicators

---

## 📁 Folder Structure

```
LogiTest_Analyzer/
├── main.py              # Main script to run the log analyzer
├── selenium_test.py     # Script to generate a Selenium test log
├── log_parser.py        # Parses log files and extracts key information
│
├── logs/                # Store log information
│   ├── embedded_log.txt
│   └── selenium_log.txt
│
```

---

## ⚙️ How to Run

### Step 1: Generate a Selenium Log

This will open a browser, perform a search, and generate a new log file in `logs/`.

```bash
python selenium_test.py
```

### Step 2: Analyze Logs

Run the analyzer to process all `.txt` files inside the `logs/` folder:

```bash
python main.py
```

---

## 📊 Example Output

```yaml
Analyzing: selenium_log.txt
  INFO: 0
  WARNING: 0
  ERROR: 0
  PASS: 1
  FAIL: 0
```

---

## 💡 Why This Project?

As part of embedded system testing and automation workflows, analyzing logs manually can be time-consuming and error-prone. This project automates that process and helps engineers quickly assess the quality of test runs, especially during:

- Embedded device boot tests  
- Web UI testing using Selenium  
- Error/Warning pattern detection  

---

## 👨‍💻 Built With

- **Python 3**
- **Selenium** (for log generation)
- **Regular Expressions (`re`)** for log parsing

---

## 🙋‍♂️ Developed By

- **Ayush Sharma**  
- **Amit Kumar** 
