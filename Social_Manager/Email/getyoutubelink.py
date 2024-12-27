# import requests



# def get_youtube_video_link(video_id, api_key):

#     url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"

#     response = requests.get(url)

#     data = response.json()
#     print(data)

#     video_link = "https://www.youtube.com/watch?v=" + data['items'][0]['snippet']['resourceId']['videoId']

#     return video_link

# get_youtube_video_link('H8Qr7wXQNck', 'AIzaSyA6WuFuTWJch1lF6B9uH4LGQa9h0OGs-NY')

import requests

def get_youtube_video_link(video_id, api_key):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        try:
            video_link = "https://www.youtube.com/watch?v=" + data['items'][0]['snippet']['resourceId']['videoId']
            return video_link
        except (KeyError, IndexError):
            print(f"Error: Could not find video with ID {video_id}")
            return None
    else:
        print(f"Error: API request failed with status code {response.status_code}")
        return None

# Usage
my_video_id = "H8Qr7wXQNck"
video_url = get_youtube_video_link(my_video_id, "AIzaSyA6WuFuTWJch1lF6B9uH4LGQa9h0OGs-NY")

if video_url:
    print(f"Video URL: {video_url}")