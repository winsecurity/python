
import re

fd=open("D:\\regex.txt","r+")
msg=fd.read()


pattern=re.compile(r'\d{3}-\d{3}-\d{3}')
#pattern=re.compile(r'(\d{3})-(\d{3})-(\d{4})')
pat2=re.compile(r'\d{3}')
pat3=re.compile(r'(\w)*\@(\w)*')
matches=pat2.finditer(msg)
match=pattern.search(msg)
match3=pat3.search(msg)
phone=pattern.findall(msg)
print(match3.group())

#print("matches found ",match.groups())
#print(match.group(1))
