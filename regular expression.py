import re

mytext="""hi,hello this is naga sai nikhil 
and whats going on guys

127.0.0.1
"""
ip="127.0.0.1"

pattern=re.compile(r'\d\d\d\.\d')
res=pattern.finditer(ip)
for each in res:
    print(each)