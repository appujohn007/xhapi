import requests
from requests.exceptions import ProxyError, ConnectTimeout

def fetch_first_working_proxy(url):
    try:
        response = requests.get(url)
        proxy_list = response.text.strip().split('\n')
        for proxy in proxy_list:
            proxies = {
                "http": f"http://{proxy}",
                "https": f"http://{proxy}"
            }
            try:
                res = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=5)
                if res.status_code == 200:
                    print(f"First working proxy: {proxy}")
                    return proxy
            except (ProxyError, ConnectTimeout):
                continue
        print("No working proxies found.")
    except requests.RequestException as e:
        print(f"Failed to fetch proxies: {e}")

if __name__ == "__main__":
    url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=sg&ssl=all&anonymity=all"
    fetch_first_working_proxy(url)
