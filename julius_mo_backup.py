# -*- coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import print_function
import socket
from contextlib import closing
import re

def main():
    pattern = re.compile("WORD=\"([^\"]+)\"")
    host = 'localhost'
    port = 10500
    bufsize = 4096
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))
    while True:
        recv_data = sock.recv(bufsize).decode('euc-jp')
        match = pattern.search(recv_data)
        if match:
            print(match.group()[6:-1])
            

if __name__ == '__main__':
    main()
