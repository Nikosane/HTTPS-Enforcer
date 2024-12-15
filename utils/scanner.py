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
            return {"url": url, "status": "Secure"}
        else:
            return {"url": url, "status": "Partial Support"}

    except requests.exceptions.SSLError:
        return {"url": url, "status": "No HTTPS"}

    except requests.exceptions.RequestException:
        return {"url": url, "status": "Connection Failed"}

def scan_websites(urls):
    report = []
    for url in urls:
        result = enforce_https(url)
        report.append(result)

    return report