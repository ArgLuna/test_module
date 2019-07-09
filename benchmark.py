# coding: utf-8
#from test import igunit, unit, analyze
from test import *
import os, time

def main():
#    time.sleep(60)
    conf = igunit.Conf()
    conf.times = 1000
    conf.pnum = 1
    conf.max_pnum = 1
    conf.testunit = 1
    conf.clearRaw()
    path = 'data/single_nomod_normal1'
    igunit.multitest(conf)
    data = analyze.Data(os.getpid())
    data.loadAll(conf.rawdir)
    data.summary()
    data.save(path)
    conf.save(path + '.conf')

    time.sleep(60)
    conf = igunit.Conf()
    conf.times = 100
    conf.pnum = 100
    conf.max_pnum = 10
    conf.testunit = 1
    conf.clearRaw()
    path = 'data/multi_nomod_normal1'
    igunit.multitest(conf)
    data = analyze.Data(os.getpid())
    data.loadAll(conf.rawdir)
    data.summary()
    data.save(path)
    conf.save(path + '.conf')

main()
