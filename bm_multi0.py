# coding: utf-8
#from test import igunit, unit, analyze
from test import *
import os, time

def main():
    modmode = 'nomod'
    migmode = 'normal'
    accpprob = ''

    time.sleep(60)
    f = igunit.FileConf()
    f.load('file.conf')
    conf = igunit.Conf()
    conf.load('conf/multi_test0.conf')
    conf.clearRaw()
    igunit.multitest(conf)
    data = analyze.Data(os.getpid())
    data.loadAll(conf.rawdir)
    data.summary()
    data.save('data/multi_test0_' +f.getPostfix())

main()
