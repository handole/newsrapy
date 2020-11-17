from TikTokApi import TikTokApi
import pandas as pd
import datetime

api = TikTokApi()

def simple_dict(tiktok_dict):
    to_return = {}
    # to_return['user_name'] = tiktok_dict['authorId']
    to_return['user_id'] = tiktok_dict['itemInfos']['authorId']
    to_return['video_id'] = tiktok_dict['itemInfos']['id']
    to_return['video_desc'] = tiktok_dict['itemInfos']['text']
    to_return['createTime'] = datetime.datetime.fromtimestamp(int(tiktok_dict['itemInfos']['createTime']))
    to_return['video_length'] = tiktok_dict['itemInfos']['video']['videoMeta']
    to_return['video_link'] = tiktok_dict['itemInfos']['video']['urls']
    to_return['n_likes'] = tiktok_dict['itemInfos']['diggCount']
    to_return['n_shares'] = tiktok_dict['itemInfos']['shareCount']
    to_return['n_comments'] = tiktok_dict['itemInfos']['commentCount']
    to_return['n_plays'] = tiktok_dict['itemInfos']['playCount']
    return to_return

n_videos = 10
hashtag = 'omnibuslaw'
tiktoks = api.byHashtag(hashtag, count=n_videos)
tiktoks = (simple_dict(v) for v in tiktoks)

tag_df = pd.DataFrame(tiktoks)
tag_df.to_csv('{}_videos.csv'.format(hashtag), index=False)

# for tiktok in tiktoks:
#     print(tiktok)
