Datacom Debugging & Refactoring Project

Overview

This project simulates a real-world software engineering task involving debugging, testing, and optimizing a legacy Python data-processing system.

The original script experienced intermittent failures during customer data export and suffered from inefficient processing logic. The project focuses on identifying the root cause, reproducing the issue with unit tests, refactoring the codebase, and improving overall performance and reliability.

⸻

Features

* Customer CSV data processing
* Transaction analytics processing
* JSON and CSV export functionality
* Unit testing using Python unittest
* Logging and error handling
* Performance optimization
* Refactored export pipeline

⸻

Problem Statement

A legacy Python script responsible for processing customer and transaction data was:

* failing intermittently during export,
* poorly documented,
* and running slower than expected.

The goal was to:

1. Diagnose the production issue
2. Reproduce the bug using automated tests
3. Refactor the problematic logic
4. Improve performance and maintainability

⸻

Root Cause Analysis

The export functionality assumed all customer records were valid dictionaries.

Malformed records caused the following runtime error:

'dict' object has no attribute 'keys'

The issue was resolved by:

* validating customer record structures,
* safely handling malformed data,
* and improving export robustness.

⸻

Performance Improvements

Before Refactoring

* Repeated dictionary traversal
* Inefficient lookup operations
* Minimal validation handling
* Slower processing for larger datasets

After Refactoring

* Optimized dictionary-based lookups
* Reduced repeated operations
* Improved error handling
* Batch row generation for exports
* Cleaner and more maintainable logic

⸻

Project Structure

.
├── process_data.py
├── TEST_CASES.py
├── customers.csv
├── transactions.csv
├── DEBUG_LOG.md
└── README.md

⸻

Technologies Used

* Python 3
* CSV Processing
* JSON
* unittest
* Logging

⸻

How to Run

Run Main Script

python process_data.py

Run Unit Tests

python TEST_CASES.py

⸻

Sample Dataset

The project includes:

* customer records
* transaction history
* analytics calculations
* export functionality

⸻

Skills Demonstrated

* Debugging legacy systems
* Root cause analysis
* Python refactoring
* Unit testing
* Data processing
* Performance optimization
* Error handling
* Software maintenance

⸻

Author

Akash
