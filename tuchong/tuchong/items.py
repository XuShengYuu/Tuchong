# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

# import scrapy
from scrapy import Item, Field

class TuchongItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    collection = 'images'
    author_id = Field()
    comments = Field()
    delete = Field()
    favorites = Field()
    image_count = Field()
    images = Field()
    post_id = Field()
    published_at = Field()
    site = Field()
    tags = Field()
    title = Field()
    title_image = Field()
    type = Field()
    update = Field()
    url = Field()
