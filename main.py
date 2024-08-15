import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    print(f"Fetching URL: {url}")  # Debugging: URL being fetched
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch URL: {url} - Status code: {response.status_code}")
        return None
    else:
        print(f"Successfully fetched URL: {url}")  # Debugging: Successful fetch
        
        # Save the HTML content to a .txt file
        with open('fetched_page.txt', 'w', encoding='utf-8') as file:
            file.write(response.text)
            print("HTML content saved to 'fetched_page.txt'")  # Debugging: File save status

        return response.text

def extract_video_details(url):
    page_content = fetch_page(url)
    if page_content is None:
        return []

    print("Parsing HTML content...")  # Debugging: Parsing status
    soup = BeautifulSoup(page_content, 'html.parser')

    result_list = []
    video_blocks = soup.find_all('div', class_='thumb-list__item')
    print(f"Found {len(video_blocks)} video blocks.")  # Debugging: Number of video blocks found

    for index, block in enumerate(video_blocks):
        print(f"Processing video block {index + 1}/{len(video_blocks)}")  # Debugging: Processing status
        
        thumb_tag = block.find('img')
        video_link_tag = block.find('a', class_='video-thumb__image-container')
        title_tag = block.find('a', class_='video-thumb-info__name')
        duration_tag = block.find('div', class_='thumb-image-container__duration')
        author_tag = block.find('div', class_='video-uploader-data')

        # Debugging: Verify tags found
        if not all([thumb_tag, video_link_tag, title_tag, duration_tag, author_tag]):
            print(f"Skipping incomplete video block {index + 1}")
            continue

        thumb_url = thumb_tag['src']
        video_url = video_link_tag['data-previewvideo']
        title = title_tag.text.strip()
        duration = duration_tag.text.strip()
        author = author_tag.text.strip()

        print(f"Video {index + 1} details:\nThumb: {thumb_url}\nVideo: {video_url}\nTitle: {title}\nDuration: {duration}\nAuthor: {author}")  # Debugging: Video details
        
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
url = f'https://xhamster.com/{page_number}'

result = extract_video_details(url)
print("Final Result:", result)  # Debugging: Final result output
