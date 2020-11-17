# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TiktokanItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    authorId = scrapy.Field()
    text = scrapy.Field()
    # createTime = scrapy.Field()
    # meta = scrapy.Field()
    video_url = scrapy.Field()
    # diggCount = scrapy.Field()
    # shareCount = scrapy.Field()
    # commentCount = scrapy.Field()
    # playCount = scrapy.Field()
