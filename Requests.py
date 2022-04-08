import threading as td
import sys
import requests
import http
from bs4 import BeautifulSoup as bs
import timeit
import socket
from urllib.parse import urlparse
import re

def main():
    try:
        num = int(sys.argv[2])
    except Exception:
        num = 1
    try:
        method = sys.argv[3]
    except Exception:
        method = "GET"
    try:
        browser = sys.argv[4]
    except Exception:
        browser = "false"
    url = sys.argv[1]
    if browser == "true":
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
    else:
        headers = {"User-Agent":"python-requests/"+requests.__version__}
    start_main = timeit.default_timer()
    lock = td.Lock()
    
    for x in range(1,num+1):
        if lock.acquire():
            start = timeit.default_timer()
            html = requests.request(method,url,headers=headers)
            url_ = html.url
            parser = urlparse(url_)
            netloc = parser.netloc
            if re.match(".+:.+",netloc) != None:
                a = re.split(":",netloc)
                netloc = a[0]
            port = "0"
            if parser.scheme == "https":
                port = "443"
            else:
                port = "80"
            status = html.status_code
            s = http.HTTPStatus(status).name
            encoding = str(html.apparent_encoding)
            try:
                serverName = str(html.headers["Server"])
            except KeyError:
                serverName = "???"
            html = bs(html.text,"html.parser")
            try:
                title = html.select("title")[0].text
            except IndexError:
                title = "???"
            end = timeit.default_timer()
            n = str(x) + " To " + str(status) + " String：" + s + " Method：" + method + " Encoding：" + encoding + " Title：" + title + " ServerName：" + serverName + " Host：" + socket.gethostbyname(netloc) + " Port："+ port + " Time：" + str(end-start)
            print(n)
            lock.release()
    end_main = timeit.default_timer()
    print("此程序运行时间：" + str(end_main-start_main))
if __name__ == "__main__":
    td.Thread(target=main).start()
