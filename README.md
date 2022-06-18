# 一些薅羊毛工具

## ammelody 半自动化

快速注册ammelody 的脚本，由于ammelody 注册是有机器人校验，所以这里只根据下面的tempemail 写了一个自动生成邮箱和输出验证码的脚本，网页注册还是需要手工操作

1. metamask 钱包生成一个新账户
2. 账户链接网站
3. 启动脚本获取一个邮箱地址
4. 网页端输入邮箱地址，验证
5. 等待脚本返回验证码
6. 输入验证码，然后输入你自己的邀请码
7. 成功。

![image-20220618142431407](D:\tool\web3\git\haoyangmao\README.assets\image-20220618142431407.png)

## myria 全自动化自动刷分

过几天再更新，我先刷一阵的。

![image-20220618142617715](D:\tool\web3\git\haoyangmao\README.assets\image-20220618142617715.png)

## tempemail

通过linshiyouxiang.net 获取一个随机临时邮箱并监听，直到接收到你指定的特定邮件。

由于linshiyouxiang.net 需要外网，这里需要本地有代理。

```python
#修改脚本中的proxies 为你自己的代理就可以了
#change your proxy host and port
proxies={'https':'http://127.0.0.1:7890'}
```

- createEmailFromLinshiyouxiang() 获取一个随机邮箱名，返回邮箱地址字符串
- keepAliveFromLinshiyouxiang() 保持刚获取的邮箱存活
- getMailFromLinshiyouxiang(emailAddress, fromName) 从指定邮箱地址emailAddress(一般就是刚获取的)监听并尝试接受一个你指定的fromName发件人发送的邮件，返回一个邮件id
- getMailContentFromLinshiyouxiang(emailAddress,mailId) 通过邮箱地址emailAddress 和刚获取的邮件id 获取邮件内容的ntml

后续想要提取邮件那里面的任何内容需要你自己写脚本操作了，不同场景不同。

由于保持存活和接受邮件等操作依赖cookie，这里只设置了全局cookie ，所以一般不能多线程。
