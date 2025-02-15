import requests

def get_socks_proxies():
    """
    Fetches a list of free proxies from the specified API and extracts only the SOCKS proxies.

    Returns:
        list: A list of strings, where each string represents a SOCKS proxy in the format "socks4://<ip>:<port>" or "socks5://<ip>:<port>".
    """
    url = "https://api.proxyscrape.com/v4/free-proxy-list/get?request=display_proxies&proxy_format=protocolipport"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        proxies = response.text.splitlines()
        socks_proxies = [proxy for proxy in proxies if proxy.startswith("socks4") or proxy.startswith("socks5")]

        return socks_proxies

    except requests.exceptions.RequestException as e:
        print(f"Error fetching proxies: {e}")
        return []

if __name__ == "__main__":
    socks_proxies = get_socks_proxies()

    if socks_proxies:
        with open("proxy.txt", "w") as f:
            for proxy in socks_proxies:
                f.write(proxy + "\n")
        print(f"Found {len(socks_proxies)} SOCKS proxies and saved to proxy.txt")
    else:
        print("No SOCKS proxies found.")