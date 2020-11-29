"""
爬取数据的url
"""

import requests
from bs4 import BeautifulSoup 
import re

class_lables = ['国际','国内','文化','法治']

# caijing = open('../res/财经.txt', 'a', encoding='UTF-8')
# jiaju = open('../res/家居.txt', 'a', encoding='UTF-8')
# jiaoyu = open('../res/教育.txt', 'a', encoding='UTF-8')
# shehui = open('../res/社会.txt', 'a', encoding='UTF-8')
# shizheng = open('../res/时政.txt', 'a', encoding='UTF-8')
# youxi = open('../res/游戏.txt', 'a', encoding='UTF-8')
# yule = open('../res/娱乐.txt', 'a', encoding='UTF-8')
guoji = open('../res/国际.txt', 'a', encoding='UTF-8')
guonei = open('../res/国内.txt', 'a', encoding='UTF-8')
wenhua = open('../res/文化.txt', 'a', encoding='UTF-8')
fazhi = open('../res/法治.txt', 'a', encoding='UTF-8')

def getUrls(url):
	req = requests.get(url)
	req.encoding = 'gb2312'
	req = req.text
	if req is None:
		return
	bf = BeautifulSoup(req, 'html.parser')
	# div_bf = bf.find('div', attrs={'id': 'news_list'})
	div_bf = bf.find('div', attrs={'class': 'content_list'})
	if div_bf is None:
		return
	div_a = div_bf.find_all('li')
	for div in div_a:
		# link = div.find('a', attrs={"target": "_blank"})
		# lable = div.find("a")
		link = div.find("div", attrs={"class": "dd_bt"})
		lable = div.find('div', attrs={"class": "dd_lm"})
		if link is None:
			continue
		
		link = link.find("a").get("href")
		lable = lable.find("a").text
		# link = link.get("href")
		# lable = lable.text
		# lable = lable[0] + lable[-1]
		if lable not in class_lables:
			continue
		# if lable == "财经":
		#     caijing.write(link+'\n')
		# elif lable == "家居":
		#     jiaju.write(link+'\n')
		# elif lable == "教育":
		#     jiaoyu.write(link+'\n')
		# elif lable == "社会":
		#     shehui.write(link+'\n')
		# elif lable == "时政":
		#     shizheng.write(link+'\n')
		# elif lable == "游戏":
		#     youxi.write(link+'\n')
		# elif lable == "娱乐":
		#     yule.write(link+'\n')
		if lable == '国内':
			guonei.write(link+'\n')
		elif lable == '国际':
			guoji.write(link + '\n')
		elif lable == '文化':
			wenhua.write(link + '\n')
		elif lable == '法治':
			fazhi.write(link + '\n')


years = ['2014', '2015', '2016', '2017', '2018', '2019']
# years = ['2009', '2010']
months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
days = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
for year in range(6):
	# if year in [0,1,2,3,4,5,6]:
	#     continue
	for month in range(12):
		if year == 0 and month in [0,1,2,3,4,5,6]:
			continue
		for day in range(31):
			if year == 0 and month == 7 and day in [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]:
				continue
			print(years[year] + " " + months[month] + " " + days[day])
			url = "http://www.chinanews.com/scroll-news/" + years[year] + "/" + months[month] + days[day] + "/news.shtml"
			getUrls(url)

# caijing.close()
# jiaju.close()
# jiaoyu.close()
# shehui.close()
# shizheng.close()
# youxi.close()
# yule.close()
guoji.close()
guonei.close()
wenhua.close()
fazhi.close()
