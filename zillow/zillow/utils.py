from http.cookies import SimpleCookie

#URL = "https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22usersSearchTerm%22%3A%22Miami%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-86.61482697108377%2C%22east%22%3A-74.96931915858377%2C%22south%22%3A23.021516141937614%2C%22north%22%3A28.26801732301331%7D%2C%22mapZoom%22%3A6%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12700%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%2C%22sortSelection%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D&wants={%22cat1%22:[%22listResults%22,%22mapResults%22],%22cat2%22:[%22total%22]}&requestId=9"
URL = "https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Miami%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-81.02713473828126%2C%22east%22%3A-79.57144626171876%2C%22south%22%3A25.397916287929792%2C%22north%22%3A26.053612766348127%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12700%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%2C%22isForRent%22%3A%7B%22value%22%3Atrue%7D%2C%22isForSaleByAgent%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleByOwner%22%3A%7B%22value%22%3Afalse%7D%2C%22isNewConstruction%22%3A%7B%22value%22%3Afalse%7D%2C%22isComingSoon%22%3A%7B%22value%22%3Afalse%7D%2C%22isAuction%22%3A%7B%22value%22%3Afalse%7D%2C%22isForSaleForeclosure%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A9%7D&wants={%22cat1%22:[%22listResults%22,%22mapResults%22]}&requestId=4"
# URL = "https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Miami%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-81.02713473828126%2C%22east%22%3A-79.57144626171876%2C%22south%22%3A25.397916287929792%2C%22north%22%3A26.053612766348127%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12700%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sortSelection%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A9%7D&wants={%22cat1%22:[%22mapResults%22]}&requestId=3"

#URL2 = "https://www.zillow.com/search/GetSearchPageState.htm?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A2%7D%2C%22usersSearchTerm%22%3A%22Miami%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-81.02713473828126%2C%22east%22%3A-79.57144626171876%2C%22south%22%3A25.397916287929792%2C%22north%22%3A26.053612766348127%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A12700%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sortSelection%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22isAllHomes%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A9%7D&wants={%22cat1%22:[%22listResults%22,%22mapResults%22],%22cat2%22:[%22total%22]}&requestId=4"

def cookie_parser():
    cookie_string = "zguid=23|%24bcb39a55-c204-42b4-bf8b-c4b8b692eb46; zgsession=1|f7902b40-563d-43ea-8f4b-22dddbbf6635; _ga=GA1.2.601984951.1635059853; _gid=GA1.2.804526973.1635059853; zjs_user_id=null; zjs_anonymous_id=%22bcb39a55-c204-42b4-bf8b-c4b8b692eb46%22; _pxvid=75e6c4a2-349a-11ec-9e82-746c696d536c; _gcl_au=1.1.253433338.1635059858; KruxPixel=true; DoubleClickSession=true; __pdst=7b6be91b76c9494b995aef5d753e8b2d; _fbp=fb.1.1635059860934.877078292; utag_main=v_id:017cb129855a000c80855923dd5f05083001707b007e8$_sn:1$_se:1$_ss:1$_st:1635061660831$ses_id:1635059860831%3Bexp-session$_pn:1%3Bexp-session$dcsyncran:1%3Bexp-session$tdsyncran:1%3Bexp-session$dc_visit:1$dc_event:1%3Bexp-session$dc_region:ap-east-1%3Bexp-session; _pin_unauth=dWlkPVpHWXpaRFl6TmpVdFpqazJOeTAwWkRKaExUbGxNRGd0WldFd1lXUXlZV1prTjJVMg; g_state={'i_p':1635067064595,'i_l':1}; KruxAddition=true; __gads=ID=2401228fde7f0986:T=1635059977:S=ALNI_MbDKwU9Q41uKL07Qifqwv-rnNf64g; JSESSIONID=1DF680F1DDD5EB2110D8E59A0946E0BC; _pxff_tm=1; _px3=fd2857f780935fb7bab16db1c413bb0312e55b5a2482ef74b2020b12a966a1b1:02IR++i32ct5vIq8hXITRxbyGELT4TeXGp3VyLN3dcqQANY3P7nK9g4mdwQfMxr5gElaqZuAFkAlBf5vmAcQAQ==:1000:bGEGnCvWDi8YcyGc/L577XcVldKJc5sNa0wGEs6qemsprnq11ea9ERQ/dA29aw+lVQFYjcYxPp+kY+K7fZzHfMQU3PYVsJMxmtvb+lUy9Exm2VAUvNT2MF8SwU88v0b2MwL1qyMDo6F1gkobYZnlsaCgqwW2byudX0YlXY5ieQU++4sdmKloImNG/vJidtop5toEH1BICGCtlKebLiiVvA==; _uetsid=7850b260349a11ec8899c70a70dc25d5; _uetvid=7853a570349a11ec9fd915a9fd99594f; AWSALB=m8cFljHaDKtSeYe3fQBw75sQo4+7PZUUbMsKkSbSXRUNcb1r2zh9yOsRhtKmVYUnNHOzTjxSoIO4dwzMrEo1zIFEFPB1TvyJN+udDi2yUd4r/gqG37HzWzlVHObW; AWSALBCORS=m8cFljHaDKtSeYe3fQBw75sQo4+7PZUUbMsKkSbSXRUNcb1r2zh9yOsRhtKmVYUnNHOzTjxSoIO4dwzMrEo1zIFEFPB1TvyJN+udDi2yUd4r/gqG37HzWzlVHObW; search=6|1637656393555%7Crect%3D28.26801732301331%252C-74.96931915858377%252C23.021516141937614%252C-86.61482697108377%26rid%3D12700%26disp%3Dmap%26mdm%3Dauto%26p%3D3%26z%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26excludeNullAvailabilityDates%3D0%09%0912700%09%09%09%09%09%09; _gat=1"
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    cookies = {}
    for key, morsel in cookie.items():
        cookies [key] = morsel.value
    return cookies

from urllib.parse import urlparse, parse_qs, urlencode
import json

def parse_new_url(url, page_number):
    url_parsed = urlparse(url)
    print(url_parsed.query)
    query_string = parse_qs(url_parsed.query)
    #print(query_string)
    #print(type(query_string))
    #print("_____________________________")
    search_query_state = json.loads(query_string.get("searchQueryState")[0])
    #print(search_query_state)
    #print(type(search_query_state))
    #print("___________________________")
    search_query_state["pagination"] = {"currentPage": page_number}
    #print(search_query_state)
    query_string.get("searchQueryState")[0] = search_query_state
    encoded_qs = urlencode(query_string, doseq =1) # doseq=True because if you didn't do it, the value here will become a list which will break url structure
    #print(encoded_qs)
    #print("__________________________")
    new_url = f"https://www.zillow.com/search/GetSearchPageState.htm?{encoded_qs}"
    return new_url