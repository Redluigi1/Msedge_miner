import webbrowser
from random import random
from random import choice
import os    
import random
import time


x = webbrowser.get()
a = ''
l1 = ["speed",'velocity','acceleration','biot','savart law','current','charge','density','pressure','electrostatics','displacement','rate of change','relativity','vector','vectorspace','wave','temperature','magnetic','line element','charge density','gauss law,','capacitor']

webbrowser.register('edge', None, webbrowser.BackgroundBrowser("C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"))


for t1 in range(4):
    for t in range(15):
        x = random.randint(1,7)
        for t1 in range(x):
            a+= choice(l1) + ' '
        webbrowser.get('edge').open("https://www.bing.com/search?q=" + a + "&cvid=f755779be0924881a02a99a0e84a87b7&aqs=edge.1.69i57j0l8.11439j0j4&FORM=ANAB01&PC=ASTS")
        a = ''  
        
    time.sleep(7)
    os.system("taskkill /im msedge.exe /f")
    
    
    
webbrowser.get('edge').open("https://rewards.bing.com/?signin=1")

