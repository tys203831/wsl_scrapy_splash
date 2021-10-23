# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SteamStoreItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    game_url = scrapy.Field()
    img_url = scrapy.Field()
    game_name = scrapy.Field()
    release_date = scrapy.Field()
    platform = scrapy.Field()
    rating = scrapy.Field()
    original_price = scrapy.Field()
    discounted_price = scrapy.Field()
    discount_rate = scrapy.Field()
