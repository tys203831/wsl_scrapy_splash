import scrapy
import json
from ..utils import cookie_parser
from scrapy.loader import ItemLoader
from ..items import YahooFinanceItem

class YahooScreenerSpider(scrapy.Spider):
    name = 'yahoo_screener'
    allowed_domains = ['finance.yahoo.com']
    # start_urls = ['http://finance.yahoo.com/screener/new?guccounter=1']

    json_dict = {
                "size": 25,
                "offset": 0,
                "sortField": "intradaymarketcap",
                "sortType": "DESC",
                "quoteType": "EQUITY",
                "topOperator": "AND",
                "query": {
                    "operator": "AND",
                    "operands": [
                        {
                            "operator": "or",
                            "operands": [
                            {
                                "operator": "EQ",
                                "operands": [
                                    "region",
                                    "us"
                                ]
                            }
                            ]
                        }
                    ]
                },
                "userId": "",
                "userIdType": "guid"
                }

    def start_requests(self):
        yield scrapy.Request(url = "https://query2.finance.yahoo.com/v1/finance/screener?crumb=Va9geevwyQQ&lang=en-US&region=US&formatted=true&corsDomain=finance.yahoo.com",
                            callback = self.parse,
                            method="POST",
                            headers ={
                                "Content-Type": "application/json",
                            },
                            body = json.dumps(self.json_dict),
                            cookies = cookie_parser(),
                            )

    def parse(self, response):
        jsonresponse = json.loads(response.body)
        quotes = jsonresponse.get("finance").get("result")[0].get("quotes")
        
        for quote in quotes:
            loader = ItemLoader(item=YahooFinanceItem(), selector=quote)
            loader.add_value("symbol", quote.get("symbol"))
            loader.add_value("longName", quote.get("longName"))
            loader.add_value("averageAnalystRating", quote.get("averageAnalystRating"))
            loader.add_value("epsCurrentYear", quote.get("epsCurrentYear"))
            loader.add_value("epsForward", quote.get("epsForward"))
            loader.add_value("bookValue", quote.get("bookValue"))
            loader.add_value("marketCap", quote.get("marketCap"))
            loader.add_value("fiftyTwoWeekRange", quote.get("fiftyTwoWeekRange"))
            loader.add_value("market", quote.get("market"))
            loader.add_value("exchange", quote.get("exchange"))
            loader.add_value("region", quote.get("region"))
            loader.add_value("trailingPE", quote.get("trailingPE"))
            loader.add_value("currency", quote.get("currency"))
            loader.add_value("fiftyTwoWeekHigh", quote.get("fiftyTwoWeekHigh"))
            loader.add_value("fiftyTwoWeekLow", quote.get("fiftyTwoWeekLow"))
            loader.add_value("forwardPE", quote.get("forwardPE"))
            loader.add_value("epsTrailingTwelveMonths", quote.get("epsTrailingTwelveMonths"))
            loader.add_value("priceToBook", quote.get("priceToBook"))
            yield loader.load_item()

        increment_num = jsonresponse.get("finance").get("result")[0].get("count")
        total_count = jsonresponse.get("finance").get("result")[0].get("total")

        if jsonresponse.get("finance").get("result")[0].get("start") < total_count:
            self.json_dict["offset"] += increment_num
            yield scrapy.Request(url = "https://query2.finance.yahoo.com/v1/finance/screener?crumb=Va9geevwyQQ&lang=en-US&region=US&formatted=true&corsDomain=finance.yahoo.com",
                                callback = self.parse,
                                method="POST",
                                headers ={
                                    "Content-Type": "application/json",
                                },
                                body = json.dumps(self.json_dict),
                                cookies = cookie_parser(),
                                )


