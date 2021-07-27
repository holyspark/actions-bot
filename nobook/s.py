# -*- coding: utf-8 -*-


import urllib.request
import sys

type = sys.getfilesystemencoding()
def run():
	url = "https://forum.nobook.com"
	headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
	req = urllib.request.Request(url=url,headers=headers)
	try:
		data = urllib.request.urlopen(req).read()
	except Exception as e:
		return 0
	html = data.decode("UTF-8").encode(type)

	result=html.split(r'target="_blank" class="xi2">')
	index = result[1].find('<')
	user = result[1][0:index]
	with open("users.txt", 'w', encoding="utf-8") as f:
		f.writelines(user)

	
if __name__ == "__main__":
	run()
