
from http.cookies import SimpleCookie

def cookie_parser():
    #print("_________________")
    #cookie_string = response.headers.getlist("Set-Cookie")[0]
    #print(cookie_string)
    #print("_________________")
    cookie_string="APID=UP1ca5b70d-089e-11ec-a50a-02fbd1bed57c; APIDTS=1635060589; B=2jtnt05gnabe2&b=3&s=fb; A1=d=AQABBKwtdWECEGeudFoH5R3g9S3riu_tm58FEgEBAQF_dmF_YQAAAAAA_eMAAAcIwi11YQH99ik&S=AQAAAtfdrqKrQSihfuaew1R24Vc; A3=d=AQABBKwtdWECEGeudFoH5R3g9S3riu_tm58FEgEBAQF_dmF_YQAAAAAA_eMAAAcIwi11YQH99ik&S=AQAAAtfdrqKrQSihfuaew1R24Vc; GUC=AQEBAQFhdn9hf0IgFASH; A1S=d=AQABBKwtdWECEGeudFoH5R3g9S3riu_tm58FEgEBAQF_dmF_YQAAAAAA_eMAAAcIwi11YQH99ik&S=AQAAAtfdrqKrQSihfuaew1R24Vc&j=WORLD; cmp=t=1635071619&j=0"
    cookie = SimpleCookie()
    cookie.load(cookie_string)
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value
    return cookies