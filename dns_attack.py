import threading
import socket
from urllib.parse import urlparse
import sys

def main():
    url = sys.argv[1]
    num = None
    try:
        num = int(sys.argv[2])
    except Exception:
        pass
    parse = urlparse(url)
    netloc = parse.netloc
    for x in range(num):
        print("DNS："+socket.gethostbyname(netloc))
if __name__ == "__main__":
    threading.Thread(target=main).start()
