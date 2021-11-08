import scrapy
from ..utils import URL, cookie_parser, parse_new_url
import json

class ZillowHousesSpider(scrapy.Spider):
    name = 'zillow_houses'
    allowed_domains = ['www.zillow.com']
    start_urls = ["http://www.zillow.com"]

    def start_requests(self):
        yield scrapy.Request(
        url=URL,
        callback=self.parse,
        cookies = cookie_parser(),
        meta = {
            "currentPage": 1
        }
        )

    def parse(self, response):
        jsonresponse = json.loads(response.body)
        houses = jsonresponse.get("cat1").get("searchResults").get("listResults")        
        for house in houses:
            address = house.get("address")
            yield {"address": address}  

        # next page pagination
        currentPage = response.request.meta["currentPage"]
        total_pages = jsonresponse.get("cat1").get("searchList").get("totalPages")

        if currentPage <= total_pages:
            currentPage += 1
            yield scrapy.Request(url = parse_new_url(url = URL, page_number = currentPage),
                                callback = self.parse, 
                                method="GET",
                                cookies = cookie_parser(),
                                meta = {
                                    "currentPage": currentPage,
                                },
                                )

