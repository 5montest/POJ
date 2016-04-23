#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#from __future__ import print_function
import socket
from contextlib import closing
import re 
import time
import serial

def main():
    ser = serial.Serial('/dev/ttyUSB0',9600)
    pattern = re.compile("WORD=\"([^\"]+)\"")
    htmldel = re.compile(r"<[^>]*?>")
    host = 'localhost'
    port = 10500
    bufsize = 4096
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))
    majoko = "$MAJOKO\n".encode()
    ousama = "$OBAKE_\n".encode()
    abehar = "$NEKO__\n".encode()
    rantar = "$BRUNA_\n".encode()
    sannin = "$KING__\n".encode()
    kuromj = "$KAIDAN\n".encode()

    while True:
        recv_data = sock.recv(bufsize).decode('utf-8')
        match = pattern.search(recv_data)
        if match != None:
            matchgroup = match.group()[6:-1]
            print(htmldel.sub("", matchgroup))
            bookname = htmldel.sub("", matchgroup)

            if (bookname == "忍たま乱太郎"
                    or bookname == "忍たま"
                    or bookname == "乱太郎"):
                print("忍たま乱太郎認識")
                time.sleep(3)
                ser.write(rantar)

            elif (bookname == "王さまめいたんてい"
                    or bookname == "王さま"
                    or bookname == "めいたんてい"):
                print("王さまめいたんてい認識")
                time.sleep(3)
                ser.write(ousama)

            elif (bookname == "まじょ子といちごの王子さま"
                    or bookname == "まじょ子"):
                print("まじょ子認識")
                time.sleep(3)
                ser.write(majoko)

            elif (bookname == "黒魔女さんが通る"
                    or bookname == "黒魔女さん"):
                print("黒魔女認識")
                time.sleep(3)
                ser.write(kuromj)

            elif (bookname == "安倍晴明は名探偵"
                    or bookname == "安倍晴明"):
                print("安倍晴明認識")
                time.sleep(3)
                ser.write(abehar)

            elif (bookname == "ズッコケ三人組の卒業式"
                    or bookname == "ズッコケ三人組"):
                print("三人組認識")
                time.sleep(3)
                ser.write(sannin)
            
if __name__ == '__main__':
    main()
