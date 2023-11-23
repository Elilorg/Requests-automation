# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazondropsItem(scrapy.Item):

    title = scrapy.Field()
    price  = scrapy.Field()
    link  = scrapy.Field()
    ref_page = scrapy.Field()

    pass
