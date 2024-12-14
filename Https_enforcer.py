import requests
from urllib.parse import urlparse

def enforce_https(url):
    try:
        # Parse the URL
        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            url = f"http://{url}"

        # Check HTTPS availability
        https_url = url.replace("http://", "https://")
        response = requests.get(https_url, timeout=10)

        if response.status_code == 200:
            print(f"[SECURE] {url} supports HTTPS.")
            return {"url": url, "status": "Secure"}
        else:
            print(f"[WARNING] {url} does not fully support HTTPS (Status: {response.status_code}).")
            return {"url": url, "status": "Partial Support"}

    except requests.exceptions.SSLError:
        print(f"[ERROR] {url} does not support HTTPS (SSL Error).")
        return {"url": url, "status": "No HTTPS"}

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to connect to {url}: {e}")
        return {"url": url, "status": "Connection Failed"}

def scan_websites(urls):
    report = []
    for url in urls:
        result = enforce_https(url)
        report.append(result)

    return report

def save_report(report, filename="https_report.txt"):
    with open(filename, "w") as file:
        for entry in report:
            file.write(f"{entry['url']} - {entry['status']}\n")
    print(f"Report saved to {filename}")

if __name__ == "__main__":
    # Example input
    urls_to_check = [
        "example.com",
        "http://nonsecurewebsite.com",
        "https://alreadysecure.com"
    ]

    print("Starting HTTPS scan...")
    report = scan_websites(urls_to_check)

    # Save the report
    save_report(report)
