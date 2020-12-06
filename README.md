# Installation
git clone https://github.com/kamronbek29/tiktok_api_python.git

# How to use
```python
from TikTokApi import TikTokApi
Api = TikTokApi()
```

## Get user info by username
```python
user_info = Api.get_user_by_username('kinoteatr_')
print(user_info)
```

## Get user feed by id
```python
user_feed  = Api.get_user_feed_by_id('6887593352386216962')
print(user_feed)
```

## Get user feed by username
```python
user_feed  = Api.get_user_feed_by_username('kinoteatr_')
print(user_feed)
```

## Get user feed by url
```python
user_feed  = Api.get_user_feed_by_username('https://www.tiktok.com/@kinoteatr_')
print(user_feed)
```

## Get music by id
```python
music_info = Api.get_music_by_id('6902700586232204033')
print(music_info)
```

## Get music by url
```python
music_info = Api.get_music_by_url('https://www.tiktok.com/music/original-sound-6902700586232204033')
print(music_info)
```

## Get music feed by id
```python
music_feed = Api.get_music_feed_by_id('6902700586232204033')
print(music_feed)
```

## Get music feed by url
```python
music_feed = Api.get_music_feed_by_url('https://www.tiktok.com/music/original-sound-6902700586232204033')
print(music_feed)
```

## Get trending feed
```python
trending_feed = Api.get_trending_feed()
print(trending_feed)
```

## Get challenge info
```python
challenge_info = Api.get_challenge_info('foryou')
print(challenge_info)
```

## Get challenge feed
```python
challenge_feed = Api.get_challenge_feed('foryou')
print(challenge_feed)
```

## Get video by id
```python
video_info = Api.get_video_by_id('6897853325761350913')
print(video_info)
```

## Get video by url
```python
video_info = Api.get_video_by_url('https://www.tiktok.com/@kinoteatr_/video/6902854770277518593')
print(video_info)
```
