# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CarscrapeItem(scrapy.Item):
	#IMAGES_MIN_HEIGHT = 110
	#IMAGES_MIN_WIDTH = 110
	image_urls = scrapy.Field()
	images = scrapy.Field()
