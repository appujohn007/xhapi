import requests
from bs4 import BeautifulSoup
import json



# Function to parse the response and extract data
def parse_response(page_number):
    url = f"https://xhamster2.com/{page_number}"
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        return f"Failed to retrieve page {page}, status code: {response.status_code}"
    
    soup = BeautifulSoup(response.content, 'html.parser')
    videos = []

    # Find all video blocks
    video_blocks = soup.find_all("li", class_="thumb-list-mobile-item")

    for video_block in video_blocks:
        video_data = {}

        # Extracting thumb image URL
        thumb_img = video_block.find("img")
        if thumb_img and thumb_img.get("src"):
            video_data['thumb'] = thumb_img['src']

        # Extracting video URL (preview video)
        video_tag = video_block.find("a", class_="thumb-image-container")
        if video_tag and video_tag.get("data-previewvideo-fallback"):
            video_data['vid'] = video_tag['data-previewvideo-fallback']

        # Extracting title
        title_tag = video_block.find("a", class_="root-48288")
        if title_tag:
            video_data['title'] = title_tag.text.strip()

        # Extracting duration
        duration_tag = video_block.find("time")
        if duration_tag:
            video_data['duration'] = duration_tag.text.strip()

        # Extracting author
        author_tag = video_block.find("a", class_="video-uploader__name")
        if author_tag:
            video_data['author'] = author_tag.text.strip()

        # Add the extracted video data to the list
        videos.append(video_data)

    return videos


# Function to get the list of videos for a page
def get_videos_from_page(page_number):
    parse_response(page_number)
    return




page_number = 1 
videos = get_videos_from_page(page_number)
print(f" result: {videos}")


#for video in videos:
   # print(json.dumps(video, indent=4))  
