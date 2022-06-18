from tempemail import *
noReplyStr="no-reply"

#get check code from mail content html
#mailContent: mail content html return from <getMailContentFromLinshiyouxiang> in tempmail
#return: check code in mail
def getCheckCode(mailContent):
    tarStr="Verification code:<br/>"
    checkCodeIdx=mailContent.find(tarStr)
    checkCodeEnd=mailContent[checkCodeIdx+len(tarStr):].find('<br/>')
    checkCode=mailContent[checkCodeIdx+len(tarStr)+1:checkCodeIdx+len(tarStr)+checkCodeEnd]
    print("[+] Get check code success!")
    print("    [*] check code: "+checkCode)
    return checkCode

if __name__ == '__main__':
    emailAddress=createEmailFromLinshiyouxiang()
    keepAliveFromLinshiyouxiang()
    mailId=getMailFromLinshiyouxiang(emailAddress,noReplyStr)
    time.sleep(5)
    #wait for the register mail
    while not mailId:
        keepAliveFromLinshiyouxiang()
        mailId=getMailFromLinshiyouxiang(emailAddress,noReplyStr)
        time.sleep(5)

    mailContent=getMailContentFromLinshiyouxiang(emailAddress, mailId)
    checkCode=getCheckCode(mailContent)
    print("[V] CHECK CODE: "+checkCode)
