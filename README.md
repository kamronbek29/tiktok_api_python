# Installation
1. git clone https://github.com/kamronbek29/tiktok_api_python.git
2. pip install requests

# How to use
```python
from TikTokApi import TikTokApi
Api = TikTokApi()
```

### Get user info by username
Inputs
* username - Username, eg - <em>kinoteatr_</em>

```python
user_info = Api.get_user_by_username(username)
print(user_info)
```

## Get user feed by id
Inputs
* user_id - Username, eg - <em>6887593352386216962</em>
* count - Number of videos to fetch

```python
user_feed  = Api.get_user_feed_by_id(user_id, count=count)
print(user_feed)
```

## Get user feed by username
Inputs
* username - Username, eg - <em>kinoteatr_</em>
* count - Number of videos to fetch

```python
user_feed  = Api.get_user_feed_by_username(username, count=count)
print(user_feed)
```

### Get user feed by url
Inputs
* user_url - Link to user profile, eg - <em>https://www.tiktok.com/@kinoteatr_</em>
* count - Number of videos to fetch

```python
user_feed  = Api.get_user_feed_by_username(user_url, count=count)
print(user_feed)
```

### Get music by id
Inputs
* music_id - Music Id, eg - <em>6902700586232204033</em>

```python
music_info = Api.get_music_by_id(music_id)
print(music_info)
```

### Get music by url
Inputs
* music_url - Music url, eg <em>https://www.tiktok.com/music/original-sound-6902700586232204033</em>

```python
music_info = Api.get_music_by_url(music_url)
print(music_info)
```

### Get music feed by id
Inputs
* music_id - Music Id, eg - <em>6902700586232204033</em>
* count - Number of videos to fetch

```python
music_feed = Api.get_music_feed_by_id(music_id, count=count)
print(music_feed)
```

### Get music feed by url
Inputs
* music_url - Music url, eg <em>https://www.tiktok.com/music/original-sound-6902700586232204033</em>
* count - Number of videos to fetch

```python
music_feed = Api.get_music_feed_by_url(music_url, count=count)
print(music_feed)
```

### Get trending feed
Inputs
* count - Number of videos to fetch

```python
trending_feed = Api.get_trending_feed(count=count)
print(trending_feed)
```

### Get challenge info
Inputs
* challenge - Challenge, eg <em>foryou</em>

```python
challenge_info = Api.get_challenge_info(challenge)
print(challenge_info)
```

### Get challenge feed
Inputs
* challenge - Challenge, eg <em>foryou</em>
* count - Number of videos to fetch

```python
challenge_feed = Api.get_challenge_feed(challenge, count=count)
print(challenge_feed)
```

### Get video by id
Inputs
* video_id - Video Id, eg - <em>6843481669886954757</em>

```python
video_info = Api.get_video_by_id(video_id)
print(video_info)
```

### Get video by url
Inputs
* video_url - Video Url, eg - <em>https://www.tiktok.com/@lunardog/video/6879030007885237505</em>

```python
video_info = Api.get_video_by_url(video_url)
print(video_info)
```
