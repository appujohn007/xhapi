import requests
from bs4 import BeautifulSoup

def fetch_video_details(query, page):
    url = f"https://www.xnxx.com/search/{query}/{page}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        video_list = []

        # Assuming each video entry is contained in a div with class 'thumb-block'
        for video in soup.find_all('div', class_='thumb-block'):
            name_tag = video.find('p', class_='title')
            if name_tag:
                name = name_tag.get_text(strip=True)

                thumb_tag = video.find('img', class_='thumb')
                thumb = thumb_tag['data-src'] if thumb_tag and 'data-src' in thumb_tag.attrs else None

                link_tag = video.find('a', href=True)
                link = f"https://www.xnxx.com{link_tag['href']}" if link_tag else None

                duration_tag = video.find('span', class_='duration')
                duration = duration_tag.get_text(strip=True) if duration_tag else None

                views_tag = video.find('span', class_='views')
                views = views_tag.get_text(strip=True) if views_tag else None

                video_list.append({
                    'name': name,
                    'thumb': thumb,
                    'link': link,
                    'duration': duration,
                    'views': views
                })

        return video_list
    else:
        print("Failed to retrieve the webpage.")
        return None

# Example usage:
query = "bdsm"
page = 1
videos = fetch_video_details(query, page)
for video in videos:
    print(videos)
