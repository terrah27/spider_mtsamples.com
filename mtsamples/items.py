# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MtsamplesItem(scrapy.Item):
	medical_specialty = scrapy.Field()
	sample_name = scrapy.Field()
	description = scrapy.Field()
	transcription = scrapy.Field()
	pass
