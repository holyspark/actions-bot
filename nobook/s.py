# -*- coding: utf-8 -*-


import urllib.request
import sys

# type = sys.getfilesystemencoding()
def run():
	url = "https://forum.nobook.com"
	headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
	req = urllib.request.Request(url=url,headers=headers)
	try:
		data = urllib.request.urlopen(req).read()
	except Exception as e:
		return 0
	html = data.decode("UTF-8")

	result=html.split(r'target="_blank" class="xi2">')
	index = result[1].find('<')
	user = result[1][0:index]
	with open(r'./users.txt', 'rb') as f:  # 打开文件
		first_line = f.readline().strip('\n').strip('\r')  # 取第一行
	if first_line == user:
		quit
	else:
		with open('users.txt', 'r+') as f:
			text = f.read()        
			f.seek(0, 0)
			f.write(user+'\n'+text)

	
if __name__ == "__main__":
	run()
