from scrapy import Spider
from TikTokApi import TikTokApi
from ..items import TiktokanItem
from selenium import webdriver

api = TikTokApi()

class TiktokSpider(Spider):
    name = 'tiktokan'
    allowed_domains = ['tiktok.com']
    start_urls = [
        'https://www.tiktok.com/tag/omnibuslaw?lang=id'
    ]

    def __init__(self):
        self.driver = webdriver.Chrome()

    def parse(self, response):
        self.driver.get(response.url)
        items = TiktokanItem()
        all_items = response.xpath("//div[contains(@class, 'tt-feed')]")
        for item in all_items:
            id = item.xpath("//div")
            authorId = item.xpath("//h2[contains(@class, 'user-username')]").extract()
            video_url = item.xpath("//a[contains(@class, 'jsx-256221443')]").extract()
            # text = item.xpath("//h1[contains(@class, 'jsx-4100551008')]").extract()
            # createTime = item.xpath("//h2[contains(@class, 'user-nickname')]").extract()
            # diggCount = item.xpath("//strong[contains(@class, 'like-text')]").extract()
            # commentCount = item.xpath("//strong[contains(@class, 'comment-text')]").extract()

            items['id'] = id
            items['authorId'] = authorId
            # items['text'] = text
            # items['createTime'] = createTime
            items['video_url'] = video_url
            # items['diggCount'] = diggCount
            # items['commentCount'] = commentCount

            yield items
