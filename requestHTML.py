import requests 
from bs4 import BeautifulSoup

f = open("log.txt", "w")

def addLog(obj, message = ""):
	f.write("[LOG]" + message + '\n')
	f.write(str(obj) + '\n\n\n')
	f.flush()

HOST = "https://www.kinopoisk.ru"
HEADERS = {
	"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",

	"cookie": "mda_exp_enabled=1; yandex_login=pereg.sergey; yandexuid=6332085291630942024; gdpr=0; _ym_uid=1631552610117021587; yuidss=6332085291630942024; i=jokAsPWUvwFQUOZHFyS0Id80GhrYlA1cxLD9Yna/Ptzvrk1ffxcUadXggisvs8wJ9VcVKKmfetgRy4duAJIUe3ih/qk=; mykp_button=movies; my_perpages=%5B%5D; mustsee_sort_v5=00.10.200.21.31.41.121.131.51.61.71.81.91.101.111; _yasc=zc8bpKYWvvUMsPreMXXlLzTluWb8UymQSgMdZuOLJciW9g==; desktop_session_key=c57b0da9388339b2669b9ab39dbebc2db1bfdb764e31cb792b7d1d9a17e110377105942421d62f56928fa4bf026d7a0c943c2e889823bcbfc3d2005e6febfd47b9d6ab66c9e5cbcf0d79d1d47e65b904beb63cdcf5825bdb71d011990a5c12c1; desktop_session_key.sig=3rLO6UwxeeeKMaRxqPWyveoTsM0; ys=udn.cDrQodC10YDQs9C10Lkg0J/QtdGA0LXQs9GD0LTQvtCy#c_chck.2013928299; _csrf=f7PFD-bUKD-ezv2AIBCPJNHa; ya_sess_id=3:1652017915.5.0.1631216691905:xphX1Q:15.1.2:1|675380481.0.2|30:207067.260217.BqiPcq3apN9jVYnGBRCw4YCKswI; mda2_beacon=1652017915895; sso_status=sso.passport.yandex.ru:blocked; _ym_isad=1; yp=1652104330.yu.6332085291630942024; ymex=1654609930.oyu.6332085291630942024; location=1; PHPSESSID=5d22189297de7899eeb7fb054bdf85a9; user_country=ru; yandex_gid=10716; tc=5961; uid=15887248; crookie=AHpzlSzEido/MY3Xdyc2WLAIuPCw6C0Sf3542e+t3ahS7hSQBJi+v70RPDrTf+KicQf69LT4mtPC7I+uIKXjLoYGmZc=; cmtchd=MTY1MjAxNzk1MTczOA==; _csrf_csrf_token=9vr4DJ4yAepPwNdqjQMg_5fUk3RscWWCVGxncI4GkMo; mobile=no; _ym_visorc=b; _ym_d=1652025873",

	"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"
}

def getInfo(filmName):
	url_requests = "https://www.kinopoisk.ru/index.php?kp_query" + "=" + '+'.join(filmName.split())	
	addLog(url_requests, "URL")
	content = requests.get(url_requests, headers=HEADERS)		
	addLog(content, "RESPONSE_ON_REQUEST")	
	soup = BeautifulSoup(content.text, "lxml")
	item = soup.find_all("div", class_="element most_wanted")[0]
	info = {
		"data-id" : item.find("div", class_="info").find(class_="js-serp-metrika").get("data-id"), 
		"url" : item.find("div", class_="info").find(class_="js-serp-metrika").get("data-url"),
		"filmName" : item.find("div", class_="info").find(class_="js-serp-metrika").get_text()
	}
	addLog(info, "INFO")	
	return info
	

def getDescription(info): 	
	url_requests = HOST + info["url"] + "/"	
	addLog(url_requests, "URL")
	content = requests.get(url_requests, headers=HEADERS)
	addLog(content, "RESPONSE_ON_REQUEST")	
	soup = BeautifulSoup(content.text, "lxml")				
	item = soup.find_all("div", class_="styles_topText__p__5L")[0]		
	addLog(item, "ITEM")	
	return item.get_text()	

def getPoster(info): 
	url_requests = "https://www.kinopoisk.ru/film/" + info["data-id"] + "/posters/"	
	content = requests.get(url_requests, headers=HEADERS)
	soup = BeautifulSoup(content.text, "lxml")
	item = soup.find_all("img", class_="styles_img__hL694 styles_cover__sfkea image styles_root__DZigd")[0]	
	return "https:" + item.get("src")
	
'''
def getMovieTrailer(info): 
	url_requests = HOST + info["url"] + "/"		
	content = requests.get(url_requests, headers=HEADERS)
	soup = BeautifulSoup(content.text, "lxml")				
	item = soup.find_all("div", class_="styles_previewWithAction__24bFH styles_preview__ruOp9")[0]	
	print(item.find("img", class_="styles_previewImg__zhMic image styles_root__DZigd").get("src"))	
	class_="styles_previewWithAction__24bFH styles_preview__ruOp9"
	url_requests = "https://www.kinopoisk.ru/film/" + info["data-id"] + "/posters/"	
	content = requests.get(url_requests, headers=HEADERS)
	soup = BeautifulSoup(content.text, "lxml")
	item = soup.find_all("img", class_="styles_img__hL694 styles_cover__sfkea image styles_root__DZigd")[0]	
	return "https:" + item.get("src")
	
info = getInfo("лулу и бриггс")
getMovieTrailer(info)
'''