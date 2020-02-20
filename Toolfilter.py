#!/usr/bin/python
 # -*-coding:cha-afk -*
 #editer : cha-afk
import sys,urllib2
from colorama import *

from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from colorama import Fore								
from colorama import Style								
from termcolor import colored
import requests, sys, re, os, time, random
from colorama import Fore, Back, Style
init()

la7mar  = '\033[91m'
lazra9  = '\033[94m'
la5dhar = '\033[92m'
movv    = '\033[95m'
lasfar  = '\033[93m'
ramadi  = '\033[90m'
blid    = '\033[1m'
star    = '\033[4m'
bigas   = '\033[07m'
bigbbs  = '\033[27m'
hell    = '\033[05m'
saker   = '\033[25m'
labyadh = '\033[00m'
cyan    = '\033[0;96m'
r = Fore.RED
g = Fore.GREEN
w = Fore.WHITE
b = Fore.BLUE
y = Fore.YELLOW
m = Fore.MAGENTA


def cls():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])


    #------------------------------------------------------------- #
def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """

  _____                 _ _ _____ _ _ _            
 | ____|_ __ ___   __ _(_) |  ___(_) | |_ ___ _ __ 
 |  _| | '_ ` _ \ / _` | | | |_  | | | __/ _ \ '__|
 | |___| | | | | | (_| | | |  _| | | | ||  __/ |   
 |_____|_| |_| |_|\__,_|_|_|_|   |_|_|\__\___|_|   
                                  By Cha

ChaTools 

  _____                 _ _ _____ _ _ _            
 | ____|_ __ ___   __ _(_) |  ___(_) | |_ ___ _ __ 
 |  _| | '_ ` _ \ / _` | | | |_  | | | __/ _ \ '__|
 | |___| | | | | | (_| | | |  _| | | | ||  __/ |   
 |_____|_| |_| |_|\__,_|_|_|_|   |_|_|\__\___|_|   
                                  By Cha

ChaTools

  _____                 _ _ _____ _ _ _            
 | ____|_ __ ___   __ _(_) |  ___(_) | |_ ___ _ __ 
 |  _| | '_ ` _ \ / _` | | | |_  | | | __/ _ \ '__|
 | |___| | | | | | (_| | | |  _| | | | ||  __/ |   
 |_____|_| |_| |_|\__,_|_|_|_|   |_|_|\__\___|_|   
                                  By Cha

ChaTools                                                                                                                       
"""
   

    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
        cls()
print_logo()

def Filteremail(x, y):
    if x!=0 :
      print "   %s[%s+%s]%s %s : %s"%(la7mar,lazra9,la7mar,la5dhar,y,x)

def filtercha():


   nb=0
   notmail=0
   Yahoo=0
   Mailru=0
   inboxru=0
   bkru=0
   hotmail=0
   live=0
   outlook=0
   seznamcz=0
   gmail=0
   orangefr=0
   yandex=0
   gmx=0
   TunisienShitt=0
   aol=0
   freefr=0
   rambler=0
   citromailhu=0
   cncom=0
   Freenetde=0
   freemailhu=0
   abv=0
   tonlinede=0
   op=0
   onet=0
   vp=0
   other=0
   burn =str(raw_input("Mailist/combo name in "'.txt'":"))
   if not os.path.isdir('Filtred#Cha'):
    os.mkdir('Filtred#Cha')
    os.mkdir('Join our discord server')
   with open(burn, 'r') as earth:
      file = earth.read().splitlines()
   for fade in file:
    fade=fade.lower()
    nb=nb+1
    try:
     if '@' not in str(fade):
        notmail=notmail+1
     elif '@yahoo.' in str(fade):
        Yahoo=Yahoo+1
        zzz=open('Filtred#Cha/yahoo.txt','a')
        zzz.write(fade+'\n')
     elif '@mail.ru' in str(fade):
        Mailru=Mailru+1
     elif  '@inbox.ru' in str(fade):
        inboxru=inboxru+1
        zzz=open('Filtred#Cha/inbox.ru.txt','a')
        zzz.write(fade+'\n')
     elif  '@bk.ru' in str(fade):
        bkru=bkru+1
        zzz=open('Filtred#Cha/bk.ru.txt','a')
        zzz.write(fade+'\n')
     elif  '@hotmail' in str(fade):
        hotmail=hotmail+1
        zzz=open('Filtred#Cha/hotmail.txt','a')
        zzz.write(fade+'\n')
     elif  '@live' in str(fade):
        live=live+1
        zzz=open('Filtred#Cha/live.txt','a')
        zzz.write(fade+'\n')
     elif  '@outlook' in str(fade):
        outlook=outlook+1
        zzz=open('Filtred#Cha/outlook.txt','a')
        zzz.write(fade+'\n')
     elif '@seznam.cz' in str(fade):
        seznamcz=seznamcz+1
        zzz=open('Filtred#Cha/seznam.cz.txt','a')
        zzz.write(fade+'\n')
     elif '@gmail.com' in str(fade):
        gmail=gmail+1
        zzz=open('Filtred#Cha/gmail.com.txt','a')
        zzz.write(fade+'\n')
     elif '@orange.' in str(fade):
        orangefr=orangefr+1
        zzz=open('Filtred#Cha/orange.fr.txt','a')
        zzz.write(fade+'\n')
     elif '@yandex.' in str(fade):
        yandex=yandex+1
        zzz=open('Filtred#Cha/yandex.txt','a')
        zzz.write(fade+'\n')
     elif '@gmx.' in str(fade):
        gmx=gmx+1
        zzz=open('Filtred#Cha/gmx.txt','a')
        zzz.write(fade+'\n')
     elif '.tn' in str(fade):
        TunisienShitt=TunisienShitt+1
        zzz=open('Filtred#Cha/tona.txt','a')
        zzz.write(fade+'\n')
     elif '@aol.' in str(fade):
        aol=aol+1
        zzz=open('Filtred#Cha/aol.txt','a')
        zzz.write(fade+'\n')
     elif '@free.fr' in str(fade):
        freefr=freefr+1
        zzz=open('Filtred#Cha/free.fr.txt','a')
        zzz.write(fade+'\n')
     elif '@rambler.' in str(fade):
        rambler=rambler+1
        zzz=open('Filtred#Cha/rambler.txt','a')
        zzz.write(fade+'\n')
     elif '@citromail.hu' in str(fade):
        citromailhu=citromailhu+1
        zzz=open('Filtred#Cha/citromail.txt','a')
        zzz.write(fade+'\n')
     elif '@21cn.com' in str(fade):
        cncom=cncom+1
        zzz=open('Filtred#Cha/21cn.com.txt','a')
        zzz.write(fade+'\n')
     elif '@freenet.de' in str(fade):
        Freenetde=Freenetde+1
        zzz=open('Filtred#Cha/freenet.de.txt','a')
        zzz.write(fade+'\n')
     elif '@freemail.hu' in str(fade):
        freemailhu=freemailhu+1
        zzz=open('Filtred#Cha/freemail.hu.txt','a')
        zzz.write(fade+'\n')
     elif '@abv.bg' in str(fade):
        abv=abv+1
        zzz=open('Filtred#Cha/abv.bg.txt','a')
        zzz.write(fade+'\n')
     elif '@t-online.de' in str(fade):
        tonlinede=tonlinede+1
        zzz=open('Filtred#Cha/t.online.txt','a')
        zzz.write(fade+'\n')
     elif '@op.' in str(fade):
        op=op+1
        zzz=open('Filtred#Cha/op.txt','a')
        zzz.write(fade+'\n')
     elif '@onet.' in str(fade):
        onet=onet+1
        zzz=open('Filtred#Cha/onet.txt','a')
        zzz.write(fade+'\n')
     elif '@vp' in str(fade):
        vp=vp+1
        zzz=open('Filtred#Cha/vp.txt','a')
        zzz.write(fade+'\n')
     else:
        other=other+1
        zzz=open('Filtred#Cha/other.txt','a')
        zzz.write(fade+'\n')
    except:
            pass
   nouwa=Yahoo+Mailru+inboxru+bkru+hotmail+live+outlook+seznamcz+gmail+orangefr+yandex+gmx+TunisienShitt+aol+freefr+rambler+citromailhu+cncom+Freenetde+freemailhu+abv+tonlinede+op+onet+vp+other
   print"%s   [%s+%s] %sTotal Emails : %s"%(la7mar,lazra9,la7mar,la5dhar,nouwa)
   Filteremail(Yahoo, 'Yahoo')
   Filteremail(Mailru, 'Mail.ru')
   Filteremail(inboxru, 'Inbox.ru')
   Filteremail(bkru, 'bk.ru')
   Filteremail(hotmail, 'Hotmail')
   Filteremail(live, 'Live')
   Filteremail(outlook, 'Outlook')
   Filteremail(seznamcz, 'seznam.cz')
   Filteremail(gmail, 'Gmail')
   Filteremail(orangefr, 'Orange.fr')
   Filteremail(yandex, 'Yandex')
   Filteremail(gmx, 'Gmx')
   Filteremail(TunisienShitt, 'Tunisien Shits')
   Filteremail(aol, 'Aol')
   Filteremail(freefr, 'Free.fr')
   Filteremail(citromailhu,'citromailhu')
   Filteremail(rambler, 'Rambler')
   Filteremail(cncom, '21cn.com')
   Filteremail(Freenetde, 'Freenetde')
   Filteremail(freemailhu, 'Freemail.hu')
   Filteremail(abv, 'Abv.bg')
   Filteremail(tonlinede, 'T-online.de')
   Filteremail(op, 'op')
   Filteremail(onet, 'Onet')
   Filteremail(vp, 'Vp')
   Filteremail(other, 'Speciel Domains')
   Filteremail(notmail, 'Not E-Mail')
filtercha()




