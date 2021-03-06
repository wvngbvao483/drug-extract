 # -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ScrapyProjectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
      title = scrapy.Field()
      abstract = scrapy.Field()
      authors = scrapy.Field()
      institutes = scrapy.Field()
      journal = scrapy.Field()
      volume = scrapy.Field()
      keywords = scrapy.Field()