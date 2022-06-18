import requests
import time
import json
import random

#change your proxy host and port
proxies={'https':'http://127.0.0.1:7890'}
#default below
linshiyouxiangBaseCookie="__cf_bm=sMOs8zNpsCn8ugMFJjIdwASG5.FXx3ZoKFlsGdr7OeE-1655435374-0-AZWsZr7Cqr65ZMbGjJBQ0IPHIJMFVYWWD0CYGhsluINQRGxM8GZ5ipe0fqSKuizKF1se9DSlQpgrAYHWzati9pVCN9cXRV3T+TJ8jGo5BkiUh2FEwOd1zs968X8BfFl1oQ==; "
linshiyouxiangNewCookie=""
targetEmailName="no-reply"
#get temp email address from www.10minutemail.ort 
#but has but.....
def createTmpEmailFrom10Min():
    tmpEmailURL="https://10minutemail.org/new.html"
    headers = {
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        "Accept": 'application/json',
        "sec-ch-ua-mobile": '?0',
        "sec-ch-ua-platform": '"Windows"',
        "Upgrade-Insecure-Requests": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": 'same-site',
        "Sec-Fetch-Mode": 'navigate',
        "Sec-Fetch-User": '?1',
        "Sec-Fetch-Dest": 'document',
        "Referer": 'https://10minutemail.org/?lang=zh',
        "Accept-Encoding": 'gzip, deflate',
        "Accept-Language": 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,zh-CN;q=0.6',
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        "Cookie": "PHPSESSID=7a24e41fb6697c133d8a1d6cb116b698; NB_SRVID=srv355878; __gads=ID=29bd7eb29f7d64a1-222f2d6786d400e2:T=1655391437:RT=1655391437:S=ALNI_MbbinFGF5fTnh9TO1ORjXDcsCx0CA; __gpi=UID=000006b31e57398a:T=1655391437:RT=1655391437:S=ALNI_Mb3Z8aAWtpEOGtP8kTXg98fUh5Atg; _ga=GA1.2.1688791501.1655391437; _gid=GA1.2.1465632494.1655391438; lang=zh; __atuvc=17%7C24; __atuvs=62ab44cde7511b66008; _gat=1"
    }
    r=requests.request("GET", tmpEmailURL, headers=headers)
    if r.status_code != 200:
        print("[-] Get new temp Email fail! HTTP code is: "+str(r.status_code))
        return False
    targetStr="class=\"mailtext\" value="
    emailIdx=r.text.find(targetStr)+len(targetStr)
    emailEnd=r.text[emailIdx:].find("\" />")
    emailStr=r.text[emailIdx:emailIdx+emailEnd]
    print(emailStr)
    if(emailStr[0] == "\""):
        emailStr = emailStr[1:]
    if(emailStr[-3:] != "com"):
        print("[-] Get new temp Email fail! HTTP code is: "+str(r.status_code))
        return False
    print("[+] Get new temp Email success!")
    print("    [*] Email Address: "+emailStr)
    return emailStr
#with bug that cannot get email
def getEmailFrom10Min():
    getEmailURL="https://10minutemail.org/mailbox.ajax.php"
    millis = str(int(round(time.time() * 1000)))
    params = {
        "_": millis,
    }
    headers = {
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        "Accept": '*/*',
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua-mobile": '?0',
        "sec-ch-ua-platform": '"Windows"',
        "Upgrade-Insecure-Requests": "1",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Sec-Fetch-Site": 'same-origin',
        "Sec-Fetch-Mode": 'cors',
        "Sec-Fetch-Dest": 'empty',
        "Referer": 'https://10minutemail.org/',
        "Accept-Encoding": 'gzip, deflate',
        "Accept-Language": 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,zh-CN;q=0.6',
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        "Cookie": "PHPSESSID=7a24e41fb6697c133d8a1d6cb116b698; NB_SRVID=srv355878; __gads=ID=29bd7eb29f7d64a1-222f2d6786d400e2:T=1655391437:RT=1655391437:S=ALNI_MbbinFGF5fTnh9TO1ORjXDcsCx0CA; __gpi=UID=000006b31e57398a:T=1655391437:RT=1655391437:S=ALNI_Mb3Z8aAWtpEOGtP8kTXg98fUh5Atg; _ga=GA1.2.1688791501.1655391437; _gid=GA1.2.1465632494.1655391438; lang=zh; __atuvc=18%7C24; __atuvs=62ab44cde7511b66007; _gat=1"
    }
    r=requests.request("GET", getEmailURL, params=params, headers=headers)
    print(r.status_code)
    print(r.text)
#get temp email address from mail.td
#bug too
def createTmpEmailFromMailtd():
    mailTailList=["@nqmo.com", "@end.tw", "@uuf.me", "@yzm.de"]
    emailAddress=''.join(random.sample(string.ascii_letters, 8))+mailTailList[random.randint(1,100000000)%4]
    print(emailAddress)
    tmpEmailURL="https://mail.td/en/mail/esc6didj@nqmo.com"
    print(tmpEmailURL)
    headers = {
        "sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
        "Accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        "sec-ch-ua-mobile": '?0',
        "sec-ch-ua-platform": '"Windows"',
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Site": 'same-origin',
        "Sec-Fetch-Mode": 'navigate',
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": 'document',
        "Referer": 'https://mail.td/en',
        "Accept-Encoding": 'gzip, deflate',
        "Accept-Language": 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7,zh-CN;q=0.6',
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        #"Cookie": "mtd_address=catttt111%40end.tw; _ga=GA1.1.758815748.1655397563; __cf_bm=PIuoE_.Aw36QUKwo2ZjZTaTxSjc1IWbm23iyFKhWT5Q-1655397568-0-ARW2N73hPRufYGKaOSI9vuENhtzmxaoWUoWTIdU0g9wYzAAy1y94vEi+JYSSBDgXuV+/Yy4PAh8EvmgWW/t6YXe4K+9MPGr1fp7fE9Wa6DR+1WhCvWohKPDCNC4AWj7MYw==; __gpi=UID=000006b346ac3091:T=1655397637:RT=1655397637:S=ALNI_MaY3csU74vsqXPsAI6ZuQELRiro1A; auth_token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2NTUzOTgxMDYsImV4cCI6MTY1NTM5ODQwNn0.-E8zvAPIHjjuXV-umHDRAoVf3qMW5AWxNXCCty5MI-c; __gads=ID=4decb23aed0f9f10:T=1655397637:S=ALNI_MbC95hMYmUGpFx_5k5_3bXTU3xdLA; _ga_9CEFYHPFDT=GS1.1.1655397563.1.1.1655398107.47"
    }
    params = {
        "name": emailAddress,
    }
    r=requests.request("GET", tmpEmailURL,  headers=headers)
    print(r.status_code)

#get email address from linshiyouxiang.net
#success, but need proxy
#get a random email address
#return: email address string
def createEmailFromLinshiyouxiang():
    global linshiyouxiangNewCookie
    linshiyouxiangNewCookie=""
    mailTailList=["@idrrate.com","@besttempmail.com","@bytetutorials.net","@linshiyouxiang.net","@meantinc.com","@companycontactslist.com","@comparisions.net","@companycontacts.net"]
    createEmailURL="https://www.linshiyouxiang.net/api/v1/mailbox/keepalive"
    timeStr=str(int(time.time()))
    param={
        "force_change": "1",
        "_ts":timeStr,
    }
    headers={
        "Cookie": linshiyouxiangBaseCookie,
        "Referer": "https://www.linshiyouxiang.net/"
    }
    r=requests.get(createEmailURL, params=param, headers=headers,proxies=proxies)
    if r.status_code != 200:
        print("[-] Get new temp Email fail! HTTP code is: "+str(r.status_code))
        return False
    linshiyouxiangNewCookie=r.headers["Set-Cookie"]
    tempmailIdx=linshiyouxiangNewCookie.find("tempmail=")
    tempmailEnd=linshiyouxiangNewCookie.find(";")
    linshiyouxiangNewCookie=linshiyouxiangNewCookie[tempmailIdx:tempmailEnd+1]
    jsonResult=json.loads(r.text)
    emailAddress=jsonResult['mailbox']+mailTailList[random.randint(0,7)]
    print("[+] Get new temp Email success!")
    print("    [*] Email Address: "+emailAddress)
    return emailAddress

#keep the email alive that you just get
def keepAliveFromLinshiyouxiang():
    keepAliveURL="https://www.linshiyouxiang.net/api/v1/mailbox/keepalive"
    headers={
        "Cookie": linshiyouxiangBaseCookie+linshiyouxiangNewCookie,
        "Referer": "https://www.linshiyouxiang.net/"
    }
    r=requests.get(keepAliveURL, headers=headers,proxies=proxies)
    if(r.status_code == 200):
        return True
    else:
        print("[-] Keep alive Fail! HTTP code is: "+str(r.status_code))
        return False

#listen this email address if it has received a mail you specified
#emailAddress: email address string
#fromName: whos email you want to receive
#return: mail id, use in <getMailContentFromLinshiyouxiang>
def getMailFromLinshiyouxiang(emailAddress, fromName):
    getMailURL="https://www.linshiyouxiang.net/api/v1/mailbox/"+emailAddress
    headers={
        "Cookie": linshiyouxiangBaseCookie+linshiyouxiangNewCookie,
        "Referer": "https://www.linshiyouxiang.net/"
    }
    r=requests.get(getMailURL, headers=headers,proxies=proxies)
    if(r.text[:2] != "[]"):
        jsonResult=json.loads(r.text)
        for i in jsonResult:
            if (i["from"] == fromName):
                print("[+] Receive mail from "+fromName+" success! id is: "+i["id"])
                return i["id"]
    print("[.] Waiting and Listening ...")
    return False

#get the mail content html
#emailAddress: email address string
#mailId: mail id you could get it from <getMailFromLinshiyouxiang>
#return: html mail content
def getMailContentFromLinshiyouxiang(emailAddress,mailId):
    emailAddress = emailAddress[:emailAddress.find("@")]
    getMailContentURL="https://www.linshiyouxiang.net/mailbox/"+emailAddress+"/"+mailId
    headers={
        "Cookie": linshiyouxiangBaseCookie+linshiyouxiangNewCookie,
        "Referer": "https://www.linshiyouxiang.net/"
    }
    r=requests.get(getMailContentURL, headers=headers,proxies=proxies)
    if r.status_code != 200:
        print("[-] Get mail content fail! HTTP code is: "+str(r.status_code))
        return False
    return r.text



if __name__ == '__main__':
    emailAddress=createEmailFromLinshiyouxiang()
    keepAliveFromLinshiyouxiang()
    mailId=getMailFromLinshiyouxiang(emailAddress,targetEmailName)
    while not mailId:
        keepAliveFromLinshiyouxiang()
        mailId=getMailFromLinshiyouxiang(emailAddress,targetEmailName)
        time.sleep(5)
    print(getMailContentFromLinshiyouxiang(emailAddress, mailId))
    