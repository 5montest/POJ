# -*- coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import print_function
import socket
from contextlib import closing
import re

def main():
    pattern = re.compile("WORD=\"([^\"]+)\"")
    htmldel = re.compile(r"<[^>]*?>")
    host = 'localhost'
    port = 10500
    bufsize = 4096
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))
    while True:
        recv_data = sock.recv(bufsize).decode('utf-8')
        match = pattern.search(recv_data)
        if match != None:
            matchgroup = match.group()[6:-1]
            print(htmldel.sub("", matchgroup))
            bookname = htmldel.sub("", matchgroup)
            if bookname == "忍たま乱太郎":
                print("忍たま乱太郎認識")
            elif bookname == "王さまめいたんてい":
                print("王さまめいたんてい認識")
            elif bookname == "まじょ子といちごの王子さま":
                print("まじょ子認識")
            elif bookname == "黒魔女さんが通る":
                print("黒魔女認識")
            elif bookname == "安倍晴明は名探偵":
                print("安倍晴明認識")
            else:
                print("三人組認識")
            
            
if __name__ == '__main__':
    main()
