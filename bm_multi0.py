# coding: utf-8
#from test import igunit, unit, analyze
from test import *
import os, time

def main():
    f = igunit.FileConf()
    f.load('file.conf')

    time.sleep(60)
    confname = 'multi_test0'
    conf = igunit.Conf()
    conf.load('conf/' + confname + '.conf')
    conf.clearRaw()
    igunit.multitest(conf)
    data = analyze.Data(os.getpid())
    data.loadAll(conf.rawdir)
    data.summary()
    data.save('data/' + confname + '_' + f.getPostfix())

main()
