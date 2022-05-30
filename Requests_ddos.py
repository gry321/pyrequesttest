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
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"}
    else:
        headers = {"User-Agent": "python-requests/"+requests.__version__}
    try:
        se = sys.argv[5]
    except Exception:
        se = "false"

    def thread(num):
        #print("[Python-Debug] %s Start" % str(num))
        start = timeit.default_timer()
        html = requests.request(method, url, headers=headers)
        url_ = html.url
        parser = urlparse(url_)
        netloc = parser.netloc
        if re.match(".+:.+", netloc) != None:
            a = re.split(":", netloc)
            netloc = a[0]
        port = "0"
        if parser.scheme == "https":
            port = "443"
        else:
            port = "80"
        if se == "true":
            html.encoding = html.apparent_encoding
        status = html.status_code
        s = http.HTTPStatus(status).name
        encoding = str(html.apparent_encoding)
        try:
            serverName = str(html.headers["Server"])
        except KeyError:
            serverName = "???"
        html = bs(html.text, "html.parser")
        try:
            title = html.select("title")[0].text
        except IndexError:
            title = "???"
        #n = str(x) + " To " + str(status) + " String：" + s + " Method：" + method + " Encoding：" + str(html.apparent_encoding)
        end = timeit.default_timer()
        n = str(status) + " String：" + s + " Method：" + method + " Encoding：" + encoding + " Title：" + title + \
            " ServerName：" + serverName + " Host：" + \
            socket.gethostbyname(netloc) + " Port：" + \
            port + " Time：" + str(end-start)
        print(n)
        #print("[Python-Debug] %s End" % str(num))
    for x in range(1, num+1):
        td.Thread(target=thread, args=(x,)).start()


if __name__ == "__main__":
    td.Thread(target=main).start()
