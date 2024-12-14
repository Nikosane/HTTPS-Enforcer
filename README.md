# HTTPS Enforcer

## Overview
The **HTTPS Enforcer** is a Python-based tool designed to scan websites and verify their HTTPS support. It ensures secure connections by testing for SSL/TLS compliance and generates a detailed report categorizing the HTTPS status of each URL.

## Features
- **Secure Connection Verification:** Checks if websites enforce HTTPS.
- **Error Detection:** Identifies SSL/TLS errors and other connection issues.
- **Comprehensive Reports:** Categorizes URLs as Secure, Partial Support, or No HTTPS.
- **Bulk URL Scanning:** Accepts multiple URLs for batch processing.

## Skills Learned
- Understanding and implementing SSL/TLS protocols.
- Crafting efficient network requests using Python's `requests` library.
- Parsing and validating URLs.
- Handling exceptions and generating user-friendly reports.


## Getting Started

### Prerequisites
1. Python 3.6 or above.
2. Install the required dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Script
1. Clone the repository:
   ```bash
   git clone https://github.com/Nikosane/https-enforcer.git
   cd https-enforcer
   ```
2. Run the main script:
   ```bash
   python https_enforcer.py
   ```
3. View the generated report in the `reports/https_report.txt` file.

## Example Report
```
example.com - Secure
http://nonsecurewebsite.com - No HTTPS
https://alreadysecure.com - Secure
```

## Contributing
Contributions are welcome! Feel free to fork the repository, make improvements, and submit a pull request. Whether it's bug fixes, new features, or documentation updates, your efforts are greatly appreciated.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

**Let’s make the web more secure, one URL at a time! 🚀**
