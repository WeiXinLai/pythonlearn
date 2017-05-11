#!/usr/bin/env python3

import hashlib
db={}

def get_md5(word):
	md5 = hashlib.md5()
	md5.update(word.encode('utf-8'))
	return md5.hexdigest()

def register(username,passwd):
	db[username]=get_md5(username+passwd+'add salt')

def login(username,passwd):
	p=get_md5(username+passwd+'add salt')
	if username in db:
		if p == db[username]:
			print('login success.')
		else:
			print('passwd wrong.')
	else:
		print('username is not exit.')


while True:
	x = input('register:1 login:2 quit:0\n')
	if x == '0':
		break
	elif x =='1':
		username = input('Input your username:\n')
		passwd = input('Input your passwd:\n')
		register(username,passwd)
	elif x == '2':
		username = input('Input your username:\n')
		passwd = input('Input your passwd:\n')
		login(username,passwd)
	else:
		print('wrong')



	




