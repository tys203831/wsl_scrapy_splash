# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
# https://docs.scrapy.org/en/latest/topics/loaders.html#input-and-output-processors

import scrapy
from itemloaders.processors import Identity, TakeFirst, MapCompose, Join
from w3lib.html import remove_tags
from scrapy.selector import Selector

def get_platforms(one_class): # since items.py does not take list as argument, it takes single value inside the list in loop 
    platforms = []
    platform = one_class.split(' ')[-1]
    if "win" in platform:
        platforms.append("Windows")
    if "mac" in platform:
        platforms.append("Mac os")
    if "linux" in platform:
        platforms.append("Linux")
    if "vr_supported" in platform:
        platforms.append("VR Supported")
    return platforms

def get_original_price(html_markup):
    original_price = ""
    selector_obj = Selector(text=html_markup)
    div_with_discount = selector_obj.xpath(".//div[@class='col search_discount responsive_secondrow']/span/text()")
    original_price = ""
    if len(div_with_discount) > 0:
        original_price = selector_obj.xpath(".//div[contains(@class,'search_price discounted')]/span/strike/text()").get()
    else:
        original_price = selector_obj.xpath(".//div[@class='col search_price  responsive_secondrow']/text()").get()
    return original_price

def clean_discounted_price(discounted_price):
    if discounted_price:
        return discounted_price.strip()
    return discounted_price

def clean_discount_rate(discount_rate):
    if discount_rate:
        discount_rate = discount_rate.lstrip("-")
        return discount_rate
    return discount_rate

class SteamStoreItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    game_url = scrapy.Field(
        output_processor = TakeFirst()
    )
    img_url = scrapy.Field(
        output_processor = TakeFirst()
    )
    game_name = scrapy.Field(
        output_processor = TakeFirst()
    )
    release_date = scrapy.Field(
        output_processor = TakeFirst()
    )
    platform = scrapy.Field(
        input_processor = MapCompose(get_platforms),
        output_processor = Identity() 
    )
    rating = scrapy.Field(
        input_processor = MapCompose(remove_tags),
        output_processor = TakeFirst()
    )
    original_price = scrapy.Field(
        input_processor = MapCompose(get_original_price, str.strip),
        output_processor = Join("")
    )
    discounted_price = scrapy.Field(
        input_processor = MapCompose(clean_discounted_price),
        output_processor = TakeFirst()
    )
    discount_rate = scrapy.Field(
        input_processor = MapCompose(clean_discount_rate),
        output_processor = TakeFirst()
    )
