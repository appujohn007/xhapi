import requests
from requests.exceptions import ProxyError, ConnectTimeout

def fetch_proxies(url):
    try:
        response = requests.get(url)
        # Split the response text by new lines to get each proxy
        proxy_list = response.text.strip().split('\n')
        return proxy_list
    except requests.RequestException as e:
        print(f"Failed to fetch proxies: {e}")
        return []

def check_proxy(proxy):
    try:
        # Use the proxy for an HTTP request
        proxies = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}"
        }
        # Try connecting to a test site to check if the proxy works
        response = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=5)
        if response.status_code == 200:
            return True
    except (ProxyError, ConnectTimeout):
        pass
    return False

def get_first_working_proxy(url):
    proxies = fetch_proxies(url)
    for proxy in proxies:
        if check_proxy(proxy):
            return proxy
    return None

# Example usage
url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=sg&ssl=all&anonymity=all"
working_proxy = get_first_working_proxy(url)
if working_proxy:
    print(f"First working proxy: {working_proxy}")
else:
    print("No working proxies found.")
