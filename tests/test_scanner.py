import unittest
from utils.scanner import enforce_https, scan_websites

class TestScanner(unittest.TestCase):
    def test_enforce_https_secure(self):
        result = enforce_https("https://example.com")
        self.assertEqual(result['status'], "Secure")

    def test_enforce_https_no_https(self):
        result = enforce_https("http://nonexistent-website.com")
        self.assertIn(result['status'], ["No HTTPS", "Connection Failed"])

    def test_scan_websites(self):
        urls = ["http://example.com", "https://secure-site.com"]
        report = scan_websites(urls)
        self.assertEqual(len(report), len(urls))
        for entry in report:
            self.assertIn(entry['status'], ["Secure", "Partial Support", "No HTTPS", "Connection Failed"])

if __name__ == "__main__":
    unittest.main()