import requests

def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        with open('response.txt', 'w', encoding='utf-8') as file:
            file.write(response.text)
        print("Response saved to response.txt")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

if __name__ == "__main__":
    url = 'https://xhamster.com/search/anal?page=3'
    fetch_page(url)
