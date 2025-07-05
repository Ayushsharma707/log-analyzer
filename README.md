# 🔍 Log Analyzer

**Log Analyzer** is a Python tool that helps you quickly understand what’s happening in your test logs,without reading every line manually.

It checks log files and gives you a simple summary like:

- ✅ How many tests passed or failed  
- ⚠️ If there were any warnings or errors  

---

## 🔧 What Kind of Logs It Supports

- **Embedded System Logs** - useful when you're testing hardware or device-based projects  
- **Selenium Logs** - helpful if you're testing websites using automation tools like Selenium  

---

## 💡 Why Use This Tool?

When you're testing something (a device or a website), it creates a log file that records everything but reading those logs line by line is slow and tiring.

This tool makes it easier by:

- ✅ Quickly showing you what went well and what didn’t  
- 🚨 Helping you catch errors and failed tests faster  
- ⏱️ Saving time during testing and debugging  

It’s a simple but helpful project for **testers**, **QA engineers**, and **developers** working with both **embedded systems** and **web automation**.



---

## 📁 Folder Structure

```
Log_Analyzer/
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



## 👨‍💻 Built With

- **Python 3**
- **Selenium** (for log generation)
- **Regular Expressions (`re`)** for log parsing

---

## 🙋‍♂️ Developed By

- **Ayush Sharma**  
- **Amit Kumar** 
