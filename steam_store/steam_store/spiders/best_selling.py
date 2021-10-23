import scrapy
from ..items import SteamStoreItem
from w3lib.html import remove_tags

class BestSellingSpider(scrapy.Spider):
    name = 'best_selling'
    allowed_domains = ['store.steampowered.com']
    start_urls = ['http://store.steampowered.com/search/?filter=topsellers/']

    def get_platforms(self, multiple_classes):
        platforms = []
        platform = [one_class.split(' ')[-1] for one_class in multiple_classes]
        if "win" in platform:
            platforms.append("Windows")
        if "mac" in platform:
            platforms.append("Mac os")
        if "linux" in platform:
            platforms.append("Linux")
        if "vr_supported" in platform:
            platforms.append("VR Supported")
        return platforms

    def clean_discount_rate(self, discount_rate):
        if discount_rate:
            discount_rate = discount_rate.lstrip("-")
        return discount_rate

    def get_original_price(self, selector_obj):
        div_with_discount = selector_obj.xpath(".//div[@class='col search_discount responsive_secondrow']/span/text()")
        original_price = ""
        if len(div_with_discount) > 0:
            original_price = str(selector_obj.xpath(".//div[contains(@class,'search_price discounted')]/span/strike/text()").get()).strip()
            
        else:
            original_price = str(selector_obj.xpath(".//div[@class='col search_price  responsive_secondrow']/text()").get()).strip()
        return original_price

    def parse(self, response):
        steam_item = SteamStoreItem()
        games = response.xpath("//div[@id='search_resultsRows']/a")
        for game in games: 
            steam_item["game_url"] = game.xpath("./@href").get()
            steam_item ["img_url"] = game.xpath(".//img/@src").get()
            steam_item ["game_name"] = game.xpath(".//span[@class='title']/text()").get()
            steam_item ["release_date"] = game.xpath(".//div[@class='col search_released responsive_secondrow']/text()").get()
            steam_item ["platform"] = self.get_platforms(game.xpath(".//span[contains(@class, 'platform_img')]/@class | .//span[@class='vr_supported']/text()").getall())
            steam_item ["rating"] = remove_tags(game.xpath(".//span[contains(@class, 'search_review_summary')]/@data-tooltip-html").get())
            steam_item ["original_price"] = self.get_original_price(game)
            steam_item ["discount_rate"] = self.clean_discount_rate(game.xpath(".//div[contains(@class,'search_discount')]/span/text()").get())
            steam_item ["discounted_price"] = [discount_price.strip() for discount_price in game.xpath(".//div[@class='col search_price discounted responsive_secondrow']/text()").getall() if discount_price.strip() != ""]
            yield steam_item

        abs_url = response.xpath("//a[@class='pagebtn' and text()='>']/@href").get()
        yield scrapy.Request(url = abs_url, callback=self.parse)