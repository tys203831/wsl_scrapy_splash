from os import replace
import scrapy
import json
from scrapy.selector import Selector
import html
from scrapy_splash import SplashRequest

class ListingsSpider(scrapy.Spider):
    name = 'listings'
    allowed_domains = ['www.centris.ca']
    start_urls = ['http://www.centris.ca/en/']
    position = {
        "startPosition": 0
        }       # why start at 0, not 12, not so understand the basic concept although it is quite logical

    http_user = "user"
    http_pass = "userpass"
    http_auth_domain = None

    script = '''
        function main(splash, args)
            splash:on_request(function(request)
                if request.url:find('css') then
                    request.abort()
                end
            end)
            splash.images_enabled = false
            splash.js_enabled = false
            assert(splash:go(args.url))
            assert(splash:wait(0.5))
            return splash:html()
        end
    '''

    def start_requests(self):
        unlock_query= {"uc":1,"uck":"caaffb17-e9d7-48ac-b940-9f9dac5eb6ed"}

        yield scrapy.Request(url="https://www.centris.ca/UserContext/UnLock",
                            callback=self.unlock_query,
                            method="POST", 
                            headers={
                                "content-type": "application/json"
                                },
                            body=json.dumps(unlock_query), 
                            )

    def unlock_query(self, response):
        update_query ={"query": {
                        "UseGeographyShapes": 0,
                        "Filters": [
                            {
                                "MatchType": "CityDistrictAll",
                                "Text": "Montréal (All boroughs)",
                                "Id": 5
                            }
                        ],
                        "FieldsValues": [
                            {
                                "fieldId": "CityDistrictAll",
                                "value": 5,
                                "fieldConditionId": "",
                                "valueConditionId": ""
                            },
                            {
                                "fieldId": "Category",
                                "value": "Residential",
                                "fieldConditionId": "",
                                "valueConditionId": ""
                            },
                            {
                                "fieldId": "SellingType",
                                "value": "Rent",
                                "fieldConditionId": "",
                                "valueConditionId": ""
                            },
                            {
                                "fieldId": "LandArea",
                                "value": "SquareFeet",
                                "fieldConditionId": "IsLandArea",
                                "valueConditionId": ""
                            },
                            {
                                "fieldId": "RentPrice",
                                "value": 0,
                                "fieldConditionId": "ForRent",
                                "valueConditionId": ""
                            },
                            {
                                "fieldId": "RentPrice",
                                "value": 1500,
                                "fieldConditionId": "ForRent",
                                "valueConditionId": ""
                            }
                        ]
                    },
                    "isHomePage": True
                }

        yield scrapy.Request(
            url="https://www.centris.ca/property/UpdateQuery",
            callback=self.update_query,
            method="POST", 
            body=json.dumps(update_query),
            headers={
                "Content-Type": "application/json"
                }, 
            )

    def update_query(self,response):
        yield scrapy.Request("https://www.centris.ca/Property/GetInscriptions",
                            callback=self.parse,
                            method="POST",
                            headers={
                                "Content-Type": "application/json",
                                },
                            body=json.dumps(self.position)
                        )

    def parse(self, response):
        jsonresponse = json.loads(response.body) # unable to decode html
        html_text = html.unescape(jsonresponse.get('d').get('Result').get('html'))
        sel = Selector(text=html_text)
        products = sel.xpath("//*[@itemtype='http://schema.org/Product']")
        for product in products:
            print("5____________________________5")
            url = product.xpath(".//*[@class='shell']/a/@href").get()
            url = url.split("/", 2)[2]
            abs_url = f"http://www.centris.ca/en/{url}"
            # print(abs_url)
            # print("__________________check_url")
            image_url = product.xpath(".//img/@src").get()
            price = product.xpath(".//span[@class='desc']/preceding-sibling::span/text()").get()
            category = product.xpath(".//*[@class='category']/div/text()").get()
            city = product.xpath(".//*[@class='address']/div/text()").get()[1]
            yield SplashRequest(url = abs_url, 
                                callback= self.parse_summary,  
                                endpoint = "render.html",# "execute", 
                                # args={
                                #     "lua_source": self.script
                                #     },
                                meta={
                                        "url": abs_url,
                                        "image url": image_url,
                                        "price": price,
                                        "category": category,
                                        "city": city
                                    }
                                )

        total_product_count = jsonresponse.get('d').get('Result').get('count')
        increment_number = jsonresponse.get('d').get('Result').get('inscNumberPerPage')

        if self.position["startPosition"] < total_product_count:
            self.position["startPosition"] += increment_number
            yield scrapy.Request("https://www.centris.ca/Property/GetInscriptions",
            callback=self.parse,
            method="POST",
            headers={
                "Content-Type": "application/json",
                },
            body=json.dumps(self.position)
            )
    
    def parse_summary(self, response):
        features = response.xpath("//*[@class='row teaser']/div/text()").getall()
        features = features[3:4]
        # features = features.remove("/n")
        address = response.xpath("//h2[@itemprop='address']/text()").get()
        price = response.request.meta["price"]
        frequency = response.xpath("//*[@class='desc']/text()").get()
        image_url = response.request.meta["image url"]
        category = response.request.meta["category"]
        city = response.request.meta["city"]

        yield {
            "features": features,
            "address": address,
            "price": price,
            "frequency": frequency,
            "image_url": image_url,
            "category": category,
            "city": city,
        }




"""     # why this fail?
        products = response.xpath("//*[@itemtype='http://schema.org/Product']")
        for product in products:
            image_url = product.xpath(".//img/@src").get()
            price = product.xpath(".//span[@class='desc']/preceding-sibling::span/text()").get()
            frequency = product.xpath(".//span[@class='desc']").get()
            category = product.xpath(".//*[@class='category']/*/text()").get()
            address = product.xpath(".//*[@class='address']/*/text()").getall()
            address = ", ".join(address)
            yield {
                "image url": image_url,
                "price": price,
                "frequency": frequency,
                "category": category,
                "address": address
            }
"""

        