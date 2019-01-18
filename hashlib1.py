import hashlib
import sys

print("Enter your Choice")
choice=int(input(""" 1.get md5 hash
             2. get sha1 hash
             3.get sha256 hash"""))
if choice==1:
    md5obj=hashlib.md5(sys.argv[1].encode())
    print(md5obj.hexdigest())
    
