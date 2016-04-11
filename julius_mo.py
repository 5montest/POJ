# -*- coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import print_function
import socket
from contextlib import closing

def main():
    host = 'localhost'
    port = 10500
    bufsize = 4096
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host,port))
    while True:
        recv_data = sock.recv(bufsize)
        print(recv_data.decode('euc-jp'))
if __name__ == '__main__':
    main()
