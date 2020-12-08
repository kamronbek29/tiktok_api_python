from tiktok_api_python.TikTokApi import TikTokApi

api = TikTokApi()
challenge_feed = api.get_challenge_feed('foryou')
print(challenge_feed)

