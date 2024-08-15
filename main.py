import requests
from bs4 import BeautifulSoup


def extract_video_details(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch URL: {url} - Status code: {response.status_code}")
    

    print("Parsing HTML content...")  # Debugging: Parsing status
    soup = BeautifulSoup(response.text, 'html.parser')

    result_list = []
    video_blocks = soup.find_all('div', class_='thumb-list__item')

    for index, block in enumerate(video_blocks):
     
        thumb_tag = block.find('img')
        video_link_tag = block.find('a', class_='video-thumb__image-container')
        title_tag = block.find('a', class_='video-thumb-info__name')
        duration_tag = block.find('div', class_='thumb-image-container__duration')
        author_tag = block.find('div', class_='video-uploader-data')

        
        if not all([thumb_tag, video_link_tag, title_tag, duration_tag, author_tag]):
            continue

        thumb_url = thumb_tag['src']
        video_url = video_link_tag['data-previewvideo']
        title = title_tag.text.strip()
        duration = duration_tag.text.strip()
        author = author_tag.text.strip()

     
        video_info = {
            'thumb': thumb_url,
            'vid': video_url,
            'title': title,
            'duration': duration,
            'author': author
        }

        result_list.append(video_info)

    print(f"Extracted {len(result_list)} videos in total.")  # Debugging: Total videos extracted
    return result_list

# Example usage:
page_number = 1
url = f'https://xhamster.com/search/anal?page=3'

result = extract_video_details(url)
print("Final Result:", result)  # Debugging: Final result output
