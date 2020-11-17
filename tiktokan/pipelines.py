# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import psycopg2

class TiktokanPipeline:
    def open_spider(self, spider):
        hostname = 'localhost'
        username = 'postgres'
        password = '020'
        database = 'scraped'
        self.connection = psycopg2.connect(host=hostname, 
            user=username, password=password, dbname=database)
        self.curr = self.connection.cursor()

    def close_spider(self, spider):
        self.curr.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.curr.execute("insert into tiktokan(id, authorId, video_url) \
                 values(%s, %s, %)", (item['id'], item['authorId'], item['video_url']))
                #     item['text'], item['createTime'], item['video_url'], \
                #     item['diggCount'], item['commentCount']))

        self.connection.commit()
        return item
