#!/usr/bin/python
# coding: utf-8
from paramiko import *
import time, socket, hashlib, requests

# tcp timeout
tcp_tout = 10
# banner_timeout (for paramiko)
b_tout = 10
# connect target
dst = '140.115.59.2'
# target port
dport = 2222
# login as
user = 'server'

localImgMd5 = '4100c034713e3989728888073aa10a2c'

imgurl = 'https://www.whitehouse.gov/wp-content/uploads/2017/11/Immigration.jpg'

def runtest(test = 0):
    if test == 0:
        return microbenchmark()
    elif test == 1:
        return macrobmSSH0()
    elif test == 2:
        return getImgTest()
    else:
        return (-2, 'conf error')

def getImgTest():
    t0 = None
    t1 = None
    try:
        t0 = time.time()
        res = requests.get(imgurl)
        t1 = time.time()
        if hashlib.md5(res.content).hexdigest() == localImgMd5:
            return (t1 - t0, None)
        else:
            return (-(t1 - t0), 'integrity check fail')
    except Exception as e:
        t1 = time.time()
        t1 -= t0
        print(e)
        return (-(t1 - t0), str(e))

def macrobmSSH0():
    t0 = None
    t1 = None
    s = None
    sc = SSHClient()
    k = RSAKey.from_private_key_file('/home/ian/.ssh/id_rsa')
    sc.set_missing_host_key_policy(AutoAddPolicy())
    t0 = time.time()
    try:
        sc.connect(hostname = dst, port = dport, username = user, pkey = k, timeout = tcp_tout, banner_timeout = b_tout)
    except Exception as e:
        t1 = time.time()
        t1 -= t0
        print(e)
        sc.close()
        return (-t1, e)
    t1 = time.time()
    sh = sc.invoke_shell()
    sin = sh.makefile('wb')
    sout = sh.makefile('rb')
    sin.write('''
    ls
    exit
    ''')
    s = sout.readlines()
    sin.close()
    sout.close()
    sh.close()
    sc.close()
    print(t0)
    print(t1)
    for l in s:
        l = l.decode('utf-8')
        if l.find('logout') >= 0:
            print(l)
            return (t1 - t0, None)
    return (-(t1 - t0), 'login fail')

def microbenchmark():
    t0 = None
    t1 = None
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(tcp_tout)
    try:
        t0 = time.time()
        sock.connect((dst, dport))
        t1 = time.time()
        sock.close()
        t1 -= t0
    except Exception as e:
        t1 = time.time()
        sock.close()
        print(e)
        t1 -= t0
        return (-t1, e)
    return (t1, None)
