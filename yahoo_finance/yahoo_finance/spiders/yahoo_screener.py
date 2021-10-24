import scrapy
import json

class YahooScreenerSpider(scrapy.Spider):
    name = 'yahoo_screener'
    allowed_domains = ['finance.yahoo.com']
    start_urls = ['http://finance.yahoo.com/screener/new?guccounter=1']

    cookie_string = "B=4nojo4pgimf6b&b=3&s=ve; APID=UP1ca5b70d-089e-11ec-a50a-02fbd1bed57c; PRF=t%3D0138.KL%252B0200.KL; A1=d=AQABBAqnYWECEPwKKDqnNH4Oxl4s7Dpe2jYFEgEBBAHkbGE6YnSFb2UB_eMBAAcIyzwrYSZ44ks&S=AQAAAjPMVHtiHoE9aFsCuFHpTF0; A3=d=AQABBAqnYWECEPwKKDqnNH4Oxl4s7Dpe2jYFEgEBBAHkbGE6YnSFb2UB_eMBAAcIyzwrYSZ44ks&S=AQAAAjPMVHtiHoE9aFsCuFHpTF0; GUC=AQEBBAFhbORiOkIhhATK; A1S=d=AQABBAqnYWECEPwKKDqnNH4Oxl4s7Dpe2jYFEgEBBAHkbGE6YnSFb2UB_eMBAAcIyzwrYSZ44ks&S=AQAAAjPMVHtiHoE9aFsCuFHpTF0&j=WORLD; cmp=t=1634828347&j=0; APIDTS=1634828754"

    def start_requests(self):
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
        
        cookie_string = self.cookie_string.split(";")
        cookies = {}
        for cookie in cookie_string:
            try:
                key, val = cookie.split("=")[0], cookie.split("=")[1] # .... 
                cookies[key] = val
            except:
                pass
            
        yield scrapy.Request(url = "https://query1.finance.yahoo.com/v1/finance/screener?crumb=gkR4vV145pO&lang=en-US&region=US&formatted=true&corsDomain=finance.yahoo.com",
                            callback = self.parse,
                            method="POST",
                            headers ={
                                "Content-type": "application/json",
                            },
                            body = json.dumps(json_dict),
                            cookies = cookies, # cookies = {key: value},
                            )


    def parse(self, response):
        print(response.body)
