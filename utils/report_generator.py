
def save_report(report, filename="https_report.txt"):
    """
    Save the HTTPS scan report to a file.

    Args:
        report (list): A list of dictionaries containing URL and status.
        filename (str): The name of the file to save the report to.
    """
    try:
        with open(filename, "w") as file:
            for entry in report:
                file.write(f"{entry['url']} - {entry['status']}\n")
        print(f"Report saved to {filename}")
    except Exception as e:
        print(f"Error saving report: {e}")