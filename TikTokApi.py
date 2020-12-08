import requests


def get_redirected_url(url_to_request):
    get_request = requests.get(url_to_request)
    redirected_url = str(get_request.url)

    return redirected_url


class TikTokApi:
    def __init__(self):
        self.main_url = 'https://www.tiktok.com/node/{}'
        self.api_url = 'https://www.tiktok.com/api/{}'
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}

    def _make_request(self, url_path, params=None):
        get_request = requests.get(self.main_url.format(url_path), headers=self.headers, params=params)
        response_json = get_request.json()

        return response_json

    def get_music_by_id(self, music_id):
        url_path = 'share/music/original-sound-{}'.format(music_id)
        response_json = self._make_request(url_path)

        return response_json

    def get_music_by_url(self, music_url):
        redirected_url = get_redirected_url(music_url)
        music_id = redirected_url.split('?')[0].split('-')[-1]
        music_info = self.get_music_by_id(music_id)

        return music_info

    def get_music_feed_by_id(self, music_id, max_cursor=0, count=10):
        params = {"type": 4, "secUid": "", "id": music_id, "count": count, "minCursor": 0,
                  "maxCursor": max_cursor, "shareUid": "", "lang": "", "verifyFp": ""}

        url_path = 'video/feed'
        response_json = self._make_request(url_path, params)

        return response_json

    def get_music_feed_by_url(self, music_url, max_cursor=0, count=10):
        redirected_url = get_redirected_url(music_url)
        music_id = redirected_url.split('?')[0].split('-')[-1]

        params = {"type": 4, "secUid": "", "id": music_id, "count": count, "minCursor": 0,
                  "maxCursor": max_cursor, "shareUid": "", "lang": "", "verifyFp": ""}

        url_path = 'video/feed'
        response_json = self._make_request(url_path, params)

        return response_json

    def get_trending_feed(self, max_cursor=0, count=10):
        params = {"type": 5, "secUid": "", "id": 1, "count": count, "minCursor": 0, "maxCursor": max_cursor,
                  "shareUid": "", "lang": "", "verifyFp": ""}

        url_path = 'video/feed'
        response_json = self._make_request(url_path, params)

        return response_json

    def get_user_by_username(self, username):
        url_path = 'share/user/@{}'.format(username)
        response_json = self._make_request(url_path)

        return response_json

    def get_user_by_url(self, user_url):
        redirected_url = get_redirected_url(user_url)
        username = redirected_url.split('?')[0].split('@')[1]
        response_json = self.get_user_by_username(username)

        return response_json

    def get_user_feed_by_id(self, user_id, max_cursor=0, count=10):
        params = {"type": 1, "secUid": "", "id": user_id, "count": count, "minCursor": 0, "maxCursor": max_cursor,
                  "shareUid": "", "lang": "", "verifyFp": ""}

        url_path = 'video/feed'
        response_json = self._make_request(url_path, params)

        return response_json

    def get_user_feed_by_username(self, username, max_cursor=0, count=10):
        user_info = self.get_user_by_username(username)
        user_id = user_info['userInfo']['user']['id']

        response_json = self.get_user_feed_by_id(user_id, max_cursor, count)

        return response_json

    def get_user_feed_by_url(self, user_url, max_cursor=0, count=10):
        user_info = self.get_user_by_url(user_url)
        user_id = user_info['userInfo']['user']['id']

        params = {"type": 1, "secUid": "", "id": user_id, "count": count, "minCursor": 0, "maxCursor": max_cursor,
                  "shareUid": "", "lang": "", "verifyFp": ""}

        url_path = 'video/feed'
        response_json = self._make_request(url_path, params)

        return response_json

    def get_challenge_info(self, challenge):
        url_path = 'share/tag/{}'.format(challenge)

        response_json = self._make_request(url_path,)

        return response_json

    def get_challenge_feed(self, challenge, max_cursor=0, count=10):
        challenge_info = self.get_challenge_info(challenge)
        challenge_id = challenge_info['challengeInfo']['challenge']['id']

        params = {"type": 3, "secUid": "", "id": challenge_id, "count": count, "minCursor": 0,
                  "maxCursor": max_cursor, "shareUid": "", "lang": "", "verifyFp": ""}

        url_path = 'video/feed'
        response_json = self._make_request(url_path, params)

        return response_json

    def get_video_by_id(self, video_id):
        return video_id

    def get_video_by_url(self, video_url):
        redirected_url = get_redirected_url(video_url)
        if 'com/v/' in redirected_url:
            video_id = redirected_url.split('/v/')[1].split('.')[0].replace('/', '')
        else:
            video_id = redirected_url.split('/video/')[1].split('?')[0].replace('/', '')

        response_json = self.get_video_by_id(video_id)

        return response_json
