# -*- coding: utf-8 -*-
import scrapy
from scrapy import Spider, Request
from urllib.parse import urlencode
from tuchong.items import TuchongItem
import json

class TuchongSpider(scrapy.Spider):
    name = 'tuchong'
    allowed_domains = ['tuchong.com']
    start_urls = ['http://tuchong.com/']

    def start_requests(self):
        data = {'query':'风光','count':'20'}
        base_url = 'https://tuchong.com/rest/search/posts?'
        for page in range(1,self.settings.get('MAX_PAGE')+1):
            data['page'] = page
            params = urlencode(data)
            url = base_url+params
            yield Request(url,self.parse)

    def parse(self, response):
        # print(response.text)
        result = json.loads(response.text)
        item = TuchongItem()
        post_list = result.get('data').get('post_list')
        for image in post_list:
            item['author_id'] = image.get('author_id')
            item['comments'] = image.get('comments')
            item['delete'] = image.get('adelete')
            item['favorites'] = image.get('favorites')
            item['image_count'] = image.get('image_count')
            item['images'] = image.get('images')
            item['post_id'] = image.get('post_id')
            item['published_at'] = image.get('published_at')
            item['site'] = image.get('site')
            item['tags'] = image.get('tags')
            item['title']= image.get('title')
            item['title_image'] = image.get('title_image')
            item['type'] = image.get('type')
            item['update'] = image.get('update')
            item['url'] = image.get('url')
        yield item
        # for field in item.fields:
        #     if field in result.keys():
        #         item[field] = result.get(field)
        # yield item
        # if 'data' in result.keys():
        #     print(data)
        #     for image in result.get('post_list'):
        #         item[author_id] = result.get(author_id)
        # for image in result.get('data'):
        #     item['author_id'] = image.get('author_id')
            # item['images'] = image.get('images')
            # item['post_id'] = image.get('post_id')
            # item['published_at'] = image.get('published_at')
            # item['site'] = image.get('site')
            # item['tags'] = image.get('tags')
            # item['title'] = image.get('title')
            # item['url'] = image.get('url')

                    
