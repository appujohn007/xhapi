import requests
from bs4 import BeautifulSoup
import json


# Function to parse the response and extract data
def parse_response(page_number):
    url = f"https://ro.xhamster2.com/{page_number}"
    print(f"Fetching URL: {url}")
    
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve page {page_number}, status code: {response.status_code}")
        return None
    
    print(f"Page {page_number} fetched successfully, parsing content...")
    soup = BeautifulSoup(response.content, 'html.parser')
    videos = []

    # Find all video blocks
    video_blocks = soup.find_all("li", class_="thumb-list-mobile-item")
    print(f"Found {len(video_blocks)} video blocks.")

    for index, video_block in enumerate(video_blocks):
        video_data = {}

        # Extracting thumb image URL
        thumb_img = video_block.find("img")
        if thumb_img and thumb_img.get("src"):
            video_data['thumb'] = thumb_img['src']
       #     print(f"Video {index + 1}: Thumb URL found - {thumb_img['src']}")

        # Extracting video URL (preview video)
        video_tag = video_block.find("a", class_="thumb-image-container")
        if video_tag and video_tag.get("data-previewvideo-fallback"):
            video_data['vid'] = video_tag['data-previewvideo-fallback']
        #    print(f"Video {index + 1}: Video URL found - {video_tag['data-previewvideo-fallback']}")

        # Extracting title
        title_tag = video_block.find("a", class_="root-48288")
        if title_tag:
            video_data['title'] = title_tag.text.strip()
          #  print(f"Video {index + 1}: Title found - {title_tag.text.strip()}")

        # Extracting duration
        duration_tag = video_block.find("time")
        if duration_tag:
            video_data['duration'] = duration_tag.text.strip()
        #    print(f"Video {index + 1}: Duration found - {duration_tag.text.strip()}")

        # Extracting author
        author_tag = video_block.find("a", class_="video-uploader__name")
        if author_tag:
            video_data['author'] = author_tag.text.strip()
         #   print(f"Video {index + 1}: Author found - {author_tag.text.strip()}")

        # Add the extracted video data to the list
        if video_data:
            videos.append(video_data)
        #    print(f"Video {index + 1} added to the list.")

    return videos


# Function to get the list of videos for a page
def get_videos_from_page(page_number):
    print(f"Getting videos for page {page_number}")
    return parse_response(page_number)


page_number = 1 
videos = get_videos_from_page(page_number)
print(f"Result: {videos}")


# Uncomment the following lines to print the videos in JSON format
# for video in videos:
#     print(json.dumps(video, indent=4))
