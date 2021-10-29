# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose

def _getraw(obj):
    return obj.get("raw")

def _getfmt(obj):
    return obj.get("fmt")

class YahooFinanceItem(scrapy.Item):
    symbol = scrapy.Field(
        output_processor = TakeFirst()
    )
    longName = scrapy.Field(
        output_processor = TakeFirst()
    )
    averageAnalystRating = scrapy.Field(
        output_processor = TakeFirst()
    )
    epsCurrentYear = scrapy.Field(
        input_processor = MapCompose(_getraw),
        output_processor = TakeFirst()
    )
    epsForward = scrapy.Field(
        input_processor = MapCompose(_getraw),
        output_processor = TakeFirst()
    )
    bookValue = scrapy.Field(
        input_processor = MapCompose(_getraw),
        output_processor = TakeFirst()
    )
    marketCap = scrapy.Field(
        input_processor = MapCompose(_getraw),
        output_processor = TakeFirst()
    )
    fiftyTwoWeekRange = scrapy.Field(
        input_processor = MapCompose(_getraw),
        output_processor = TakeFirst()
    )
    market = scrapy.Field(
        output_processor = TakeFirst()
    )
    exchange = scrapy.Field(
        output_processor = TakeFirst()
    )
    region = scrapy.Field(
        output_processor = TakeFirst()
    )
    trailingPE = scrapy.Field(
        input_processor = MapCompose(_getraw),
        output_processor = TakeFirst()
    )
    currency = scrapy.Field(
        output_processor = TakeFirst()
    )
    fiftyTwoWeekHigh = scrapy.Field(
        input_processor = MapCompose(_getraw),
        output_processor = TakeFirst()
    )
    fiftyTwoWeekLow = scrapy.Field(
        input_processor = MapCompose(_getraw),
        output_processor = TakeFirst()
    )
    forwardPE = scrapy.Field(
        input_processor = MapCompose(_getraw),
        output_processor = TakeFirst()
    )
    epsTrailingTwelveMonths = scrapy.Field(
        input_processor = MapCompose(_getraw),
        output_processor = TakeFirst()
    )
    priceToBook = scrapy.Field(
        input_processor = MapCompose(_getraw),
        output_processor = TakeFirst()
    )
