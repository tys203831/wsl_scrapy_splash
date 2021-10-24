import scrapy
import json
from urllib.parse import urlencode
from ..utils import cookie_parser

class YahooScreenerSpider(scrapy.Spider):
    name = 'yahoo_screener'
    allowed_domains = ['finance.yahoo.com']
    start_urls = ['http://finance.yahoo.com/screener/new?guccounter=1']

    # https://udc.yahoo.com/v2/public/yql?yhlVer=2&yhlClient=rapid&yhlS=1183335883&yhlCT=2&yhlBTMS=1635069532760&yhlClientVer=3.53.31&yhlRnd=lM0jiz1xJ4bAbnqv&yhlCompressed=0

    def start_requests(self):
        data_raw = {"q": "select%20*%20from%20x%20where%20a%20%3D%20'%7B%22bp%22%3A%7B%22_guc%22%3A%22AQEBAQFhdn9hf0IgFASH%22%2C%22_a1s%22%3A%22d%3DAQABBKwtdWECEGeudFoH5R3g9S3riu_tm58FEgEBAQF_dmF_YQAAAAAA_eMAAAcIwi11YQH99ik%26S%3DAQAAAtfdrqKrQSihfuaew1R24Vc%26j%3DWORLD%22%2C%22_pl%22%3A%221%22%2C%22A_v%22%3A%223.53.31%22%2C%22A_cn%22%3A%22EVERGREEN-PROD%22%2C%22test%22%3A%22fd-tm-autosub-ctrl%2Cfd-pf-holdings-ctrl%2Cfd-a2-upsell-2%2Cfd-adobe-promo-2%2Cfd-nav-1%2Cfdw-nativebb-bc-1%2CJRVXP-finance-plutus-start-idx-5%2Cfd-advancedchart-ctrl%22%2C%22_bt%22%3A%22rapid%22%2C%22guccounter%22%3A%221%22%2C%22A_pr%22%3A%22https%22%2C%22A_tzoff%22%3A%228%22%2C%22A_cnf%22%3A%22%7B%5C%22async_all_clicks%5C%22%3Atrue%2C%5C%22click_timeout%5C%22%3A300%2C%5C%22client_only%5C%22%3A1%2C%5C%22compr_type%5C%22%3A%5C%22deflate%5C%22%2C%5C%22pageview_on_init%5C%22%3Atrue%2C%5C%22query_parameters%5C%22%3Atrue%2C%5C%22test_id%5C%22%3A%5C%22fd-tm-autosub-ctrl%2Cfd-pf-holdings-ctrl%2Cfd-a2-upsell-2%2Cfd-adobe-promo-2%2Cfd-nav-1%2Cfdw-nativebb-bc-1%2CJRVXP-finance-plutus-start-idx-5%2Cfd-advancedchart-ctrl%5C%22%2C%5C%22tracked_mods_viewability%5C%22%3A%5B%5D%2C%5C%22track_right_click%5C%22%3Atrue%2C%5C%22viewability%5C%22%3Atrue%2C%5C%22dwell_on%5C%22%3Atrue%2C%5C%22perf_navigationtime%5C%22%3A2%2C%5C%22perf_resourcetime%5C%22%3A1%2C%5C%22webworker_file%5C%22%3A%5C%22%2F__rapidworker-1.2.js%5C%22%2C%5C%22spaceid%5C%22%3A1183335883%7D%22%7D%2C%22r%22%3A%5B%7B%22t%22%3A%22pv%22%2C%22s%22%3A%221183335883%22%2C%22pp%22%3A%7B%22A_sid%22%3A%22ELFjzjKOPsh8u5rr%22%2C%22_w%22%3A%22finance.yahoo.com%2Fscreener%2Fnew%3Fguccounter%3D1%22%2C%22ver%22%3A%22ydotcom%22%2C%22navtype%22%3A%22client%22%2C%22pt%22%3A%22utility%22%2C%22pct%22%3A%22screener%22%2C%22pg_name%22%3A%22detail%22%2C%22pstcat%22%3A%22equity%22%2C%22mrkt%22%3A%22us%22%2C%22site%22%3A%22finance%22%2C%22lang%22%3A%22en-US%22%2C%22colo%22%3A%22sg3%22%2C%22_yrid%22%3A%22c5nsf1dgnadjb%22%2C%22_rid%22%3A%22c5nsf1dgnadjb%22%2C%22abk%22%3A%22%22%2C%22_guc%22%3A%22AQEBAQFhdn9hf0IgFASH%22%2C%22_a1s%22%3A%22d%3DAQABBKwtdWECEGeudFoH5R3g9S3riu_tm58FEgEBAQF_dmF_YQAAAAAA_eMAAAcIwi11YQH99ik%26S%3DAQAAAtfdrqKrQSihfuaew1R24Vc%26j%3DWORLD%22%2C%22A_%22%3A%221%22%2C%22A_sr%22%3A%221280x720%22%2C%22A_vr%22%3A%221280x672%22%2C%22A_do%22%3A%221%22%2C%22A_ib%22%3A%221280x301%22%2C%22A_ob%22%3A%221280x672%22%2C%22A_srr%22%3A%221.5%22%7D%2C%22_ts%22%3A%221635071652%22%2C%22_ms%22%3A%22303%22%2C%22lv%22%3A%5B%5D%7D%5D%2C%22yrid%22%3A%22%22%2C%22optout%22%3A%220%22%2C%22nol%22%3A%220%22%7D'"}
       
        yield scrapy.Request(url = "https://udc.yahoo.com/v2/public/yql?yhlVer=2&yhlClient=rapid&yhlS=1183335883&yhlCT=2&yhlBTMS=1635071652494&yhlClientVer=3.53.31&yhlRnd=e79B0tNeQ4uA1k3s&yhlCompressed=0",
                            callback=self.update_query,
                            method="POST",
                            headers={
                                "Content-Type": "application/x-www-form-urlencoded"
                                },
                            body = urlencode(data_raw),
                            cookies = cookie_parser(),
                            )

    def update_query(self, response):
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
        
        yield scrapy.Request(url = "https://query2.finance.yahoo.com/v1/finance/screener?crumb=Va9geevwyQQ&lang=en-US&region=US&formatted=true&corsDomain=finance.yahoo.com",
                            callback = self.parse,
                            method="POST",
                            headers ={
                                "Content-type": "application/json",
                                "referer": "https://finance.yahoo.com/screener/unsaved/408ca2da-76f2-47fd-8c2f-41b4dd4b8bd5",
                            },
                            body = json.dumps(json_dict),
                            cookies = cookie_parser(),
                            )

    def parse(self, response):
        with open("my_file.txt","wb") as File:
            File.write(response.body)

