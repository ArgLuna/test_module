# coding: utf-8
#from test import igunit, unit, analyze
from test import *
import os, time

def main():
    modmode = 'nomod'
    migmode = 'normal'
    accpprob = ''

    time.sleep(60)
    conf = igunit.Conf()
    conf.load('conf/single_test0.conf')
    conf.clearRaw()
    igunit.multitest(conf)
    data = analyze.Data(os.getpid())
    data.loadAll(conf.rawdir)
    data.summary()
    data.save('data/single_test0_' + modmode + '_' + migmode + '_' + accpprob)

    time.sleep(60)
    conf = igunit.Conf()
    conf.load('conf/single_test1.conf')
    conf.clearRaw()
    igunit.multitest(conf)
    data = analyze.Data(os.getpid())
    data.loadAll(conf.rawdir)
    data.summary()
    data.save('data/single_test1_' + modmode + '_' + migmode + '_' + accpprob)

    time.sleep(60)
    conf = igunit.Conf()
    conf.load('conf/multi_test0.conf')
    conf.clearRaw()
    igunit.multitest(conf)
    data = analyze.Data(os.getpid())
    data.loadAll(conf.rawdir)
    data.summary()
    data.save('data/multi_test0_' + modmode + '_' + migmode + '_' + accpprob)

    time.sleep(60)
    conf = igunit.Conf()
    conf.load('conf/multi_test1.conf')
    conf.clearRaw()
    igunit.multitest(conf)
    data = analyze.Data(os.getpid())
    data.loadAll(conf.rawdir)
    data.summary()
    data.save('data/multi_test1_' + modmode + '_' + migmode + '_' + accpprob)

main()
