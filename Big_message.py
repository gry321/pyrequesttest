from logging import exception
import socket
from urllib.parse import urlparse
import time
import threading
import sys
import re


def main():
    if len(sys.argv) < 2 or sys.argv[1] == '-h' or sys.argv[1] == '--help':
        print("Usage: python3 big_message.py <url> <message : String default=null > <nums> : Integer default=1>")
        exit(1)
    url = sys.argv[1]
    try:
        hostname = urlparse(url).hostname
        port = urlparse(url).port
        if port is None:
            port = 80
    except socket.gaierror:
        print("Invalid URL")
        exit(1)
    try:
        hostname = socket.gethostbyname(hostname)
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        exit(1)
    except TypeError:
        print("Hostname could not be resolved. Exiting")
        exit(1)
    try:
        message = sys.argv[2]
        result = re.findall("\.(.+):\*(\d+)", message)
        if result != []:
            for i in result:
                string = i[0]
                try:
                    num = int(i[1])
                except ValueError:
                    num = 1
                message = message.replace(
                    "."+i[0]+":*"+i[1], string * num)
    except Exception:
        message = ""

    try:
        nums = int(sys.argv[3])
    except ValueError:
        nums = 1
    except IndexError:
        nums = 1

    start_time = time.time()
    for i in range(nums):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            send_start_time = time.time()
            s.connect((hostname, port))
            s.sendall(message.encode())
            send_end_time = time.time()
            print("第{}次发送成功，时间：{}，内容：{}".format(
                i+1, send_end_time - send_start_time, "空" if message == "" else message))
            s.shutdown(socket.SHUT_WR)
            s.close()
        except socket.error:
            print("Connection error")
            exit(1)
        end_time = time.time()
    print("总共用时: {}".format(end_time - start_time))


if __name__ == "__main__":
    threading.Thread(target=main, name="BigMessageThread").start()
