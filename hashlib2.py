import hashlib

f=open("D:\\xml.html","r")
md5hash=hashlib.md5(f)
print(md5hash.hexdigest())
