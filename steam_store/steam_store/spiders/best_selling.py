import scrapy
from ..items import SteamStoreItem
from scrapy.loader import ItemLoader

class BestSellingSpider(scrapy.Spider):
    name = 'best_selling'
    allowed_domains = ['store.steampowered.com']
    start_urls = ['http://store.steampowered.com/search/?filter=topsellers/']


    def get_original_price(self, selector_obj):
        div_with_discount = selector_obj.xpath(".//div[@class='col search_discount responsive_secondrow']/span/text()")
        original_price = ""
        if len(div_with_discount) > 0:
            original_price = selector_obj.xpath(".//div[contains(@class,'search_price discounted')]/span/strike/text()").get()
            
        else:
            original_price = selector_obj.xpath(".//div[@class='col search_price  responsive_secondrow']/text()").get() # why getall()
        return original_price

    def parse(self, response):
        games = response.xpath("//div[@id='search_resultsRows']/a")
        for game in games: 
            loader = ItemLoader(item = SteamStoreItem(), selector=game, response=response)
            loader.add_xpath("game_url", "./@href")
            loader.add_xpath("img_url", ".//img/@src")
            loader.add_xpath("game_name", ".//span[@class='title']/text()")
            loader.add_xpath("release_date", ".//div[@class='col search_released responsive_secondrow']/text()")
            loader.add_xpath("platform", ".//span[contains(@class, 'platform_img')]/@class | .//span[@class='vr_supported']/text()") # getall()
            loader.add_xpath("rating",  ".//span[contains(@class, 'search_review_summary')]/@data-tooltip-html")
            loader.add_xpath("original_price", ".//div[contains(@class, 'search_price_discount_combined' )]")
            loader.add_xpath("discount_rate", ".//div[contains(@class,'search_discount')]/span/text()")
            loader.add_xpath("discounted_price", ".//div[@class='col search_price discounted responsive_secondrow']/text()")
            yield loader.load_item()

        abs_url = response.xpath("//a[@class='pagebtn' and text()='>']/@href").get()
        yield scrapy.Request(url = abs_url, callback=self.parse)