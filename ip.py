#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re
content=[]
def get():
        global content
        count=0
        l=[0,1,8,9,16,17,24,25,32,33,40,41,48,49,56,57,64,65,72,73,80,81]
        for page in range(1,11):        
            url='http://www.kuaidaili.com/proxylist/'+str(page)+'/'
            html=requests.get(url);html.encoding='uft-8';
            rawpart=re.findall(r'''<td>(.*)</td>''',html.text);
            
            for i in rawpart:
                if count in l:
                    content.append(str(i))
                count=count+1
            count=0
                  
            print("Page",page,"sannered.")

def filew(contents):
    count=0
    f = open("ip.txt", "w")
    for line in contents:
        f.write(line+'\n')
        count=count+1
    print('All content delivered.')
    print(count/2,'records in total.')

get()
filew(content)
i=input('Press anykey to exit ')

