import unittest
import os
from utils.report_generator import save_report

class TestReportGenerator(unittest.TestCase):
    def setUp(self):
        self.sample_report = [
            {"url": "https://example.com", "status": "Secure"},
            {"url": "http://insecure-site.com", "status": "No HTTPS"}
        ]
        self.filename = "test_report.txt"

    def test_save_report(self):
        # Save the report
        save_report(self.sample_report, self.filename)
        
        # Verify the file contents
        self.assertTrue(os.path.exists(self.filename))
        with open(self.filename, "r") as file:
            lines = file.readlines()
            self.assertEqual(len(lines), len(self.sample_report))
            for i, entry in enumerate(self.sample_report):
                self.assertIn(entry['url'], lines[i])
                self.assertIn(entry['status'], lines[i])

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

if __name__ == "__main__":
    unittest.main()
