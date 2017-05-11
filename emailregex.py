#!/usr/bin/env python3

import re

emailregex=re.compile(r'^([a-zA-Z0-9_]+)@([a-z0-9]+).(com)')

def email_choose(email):
	if emailregex.match(email)==None:
		print('%s email adress is invail.' % email)
	elif emailregex.match(email).group(2)=='microsoft':
		print('%s is miscrosoft email.' % email)
	elif emailregex.match(email).group(2)=='qq':
		print('%s is qq mail.' % email)
	elif emailregex.match(email).group(2)=='163':
		print('%s is 163 mail' % email)
	else:
		print('the email address is not require.')

email1 = 'someone@microsoft.com'
email2 = 'gasgasd@qq.com'
email3 = 'eadfdfa@163.com'
email4 = 'asdf<a2132__@163.com'

email_choose(email1)
email_choose(email2)
email_choose(email3)
email_choose(email4)

