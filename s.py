# -*- coding: utf-8 -*-

user="111"
with open('email.txt', 'r+') as f:
			text = f.read()        
			f.seek(0, 0)
			f.write(user+'\n'+text)
