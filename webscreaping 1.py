from bs4 import BeautifulSoup
from urllib.request import urlopen,HTTPError
import re

html=urlopen("https://www.ethicalhackx.com/ceh-v9-download/")
bs=BeautifulSoup(html.read(),'lxml')
#urls=re.compile("\.\.\/img\/gifts\/img.\.jpg")
#images=bs.findAll("img",{"src":urls})
print(bs)

