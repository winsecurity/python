#import requests #importing requests library 
from urllib.request import urlopen,HTTPError    #imports urllib.requests
from bs4 import BeautifulSoup

#myfunctions

def getHtml(url):    #establishes connection to webserver and gets our GET(requested) html
    try:
        html=urlopen(url)
        return html #GET  html by urlopen method
    except HTTPError as e:   # raises an error if page not found
        print(e)

def scrape(url):
    html=getHtml(url)
    p=[]
    a=[]
    try:
    #print(html.read())   #print html response in readable format
        bs=BeautifulSoup(html.read(),'lxml')
    #change code here to ur need
        #title=bs.html.title
        text=bs.findAll("p",{"class":"s2"})  #gets all paragraph elements that belong to class s2
        #lnews=bs.findAll({"ul"},{"id":"news"})    #
        links=bs.findAll({"p"},{"align":"justify"})         #get all paras in latest news section
        for each in links:    
            p.append(each.get_text())
        for ele in bs.findAll({"p"},{"align":"justify"}):
            
            a.append(ele.findAll('a'))
##        for ele in bs.findAll({"p"},{"align":"justify"}).children:
##            print(ele)


       
        for each in range(0,len(p)):
            print(p[each])
            print(a[each])
            
        
                    
    except AttributeError as e:
        print("Attribute not found")
#print(bs)  




scrape("http://www.rvrjcce.ac.in/")
  
    

