"""
爬取数据
"""

import requests
from bs4 import BeautifulSoup

# url文件地址
URL_PATH = r'C:\Users\12391\Desktop\THUCNews\07财经.txt'
# 爬取数据输出的目录，建议目录的命名按照我群里发的名称，每一个类单独一个目录
OUTPUT_DIR = r'C:\Users\12391\Desktop\THUCNews\07财经'

def write_one_data_from_url(url, output_path):
	req = requests.get(url)
	req.encoding = 'GB2312'
	bf = BeautifulSoup(req.text, 'html.parser')
	div = bf.find('div', attrs={'class': 'left_zw'})
	if div is None:
		return
	out = open(output_path, 'w', encoding='utf8')
	p = div.find_all('p', text=True)
	for ptext in p:
		out.write(ptext.text + '\n');
	out.close()

urlfile = open(URL_PATH, 'r')

# 如果中途出错，可以用以下代码跳过已经爬取的url
# for i in range(60000):
# 	urlfile.readline()

# range函数里面是要爬多少数据
for i in range(25000):
	url = urlfile.readline()
	if url[0]=='/':
		url = 'http://www.chinanews.com' + url
	if url[-1] == '\n':
		url = url[:-1]

	write_one_data_from_url(url, OUTPUT_DIR + r'\%d.txt' % i)
	print('%d.txt' % i)

urlfile.close()