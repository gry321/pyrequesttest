import requests
import os
import sys
import urllib.parse as up
import re


class UrlIsError(Exception):
    pass


url = sys.argv[1]
if re.match("(http|ftp|https):\/\/[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&:/~\+#]*[\w\-\@?^=%&/~\+#])?", url):
    pass
else:
    raise UrlIsError("网址格式不对")
try:
    filename = sys.argv[2]
except Exception:
    filename = up.urlsplit(
        url).path.split("/")[-1]
try:
    speed = sys.argv[3]
    speed = int(speed)
except Exception:
    speed = 50
try:
    path = sys.argv[4]
except Exception:
    path = "."
try:
    browser = sys.argv[5]
except Exception:
    browser = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36"


def main():
    try:
        headers = {"User-Agent": browser}
        html = requests.get(url, headers=headers, stream=True)
    except Exception:
        print("请求错误")
    else:
        echo_num = 0
        os.chdir(path)
        ok = True
        is_open = False
        if filename in os.listdir():
            p = input("那个目录下有这个文件，请指示\nw: 覆盖\nq: 结束")
            if p.upper() == "W":
                f = open(filename, "wb+")
                is_open = True
            elif p.upper() == "Q":
                ok = False
        if ok == False:
            return None
        if is_open == False:
            f = open(filename, "wb+")
        for x in html.iter_content(chunk_size=speed):
            f.write(x)
            echo_num += len(x)
            # print("一共写入%s个字符" % str(echo_num))
            print("本次写入{}个字符，一共写入{}个字符".format(str(len(x)), str(echo_num)))
            # print("本次写入%s个字符" % str(len(x)))
        f.close()
        print("下载完成")


if __name__ == "__main__":
    main()
