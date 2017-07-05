from urllib import request

url = "http://www.baidu.com/"
response = request.urlopen(url)
f = open("baidu.txt","w")
page = f.write(str(response.read()))
f.close()
url = "http://www.qq.com/"
response = request.urlopen(url)
f = open("qq.txt","w")
page = f.write(str(response.read()))
f.close()