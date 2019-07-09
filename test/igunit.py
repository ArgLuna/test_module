#!/usr/bin/python3
# coding: utf-8
from test import unit, analyze
import time, multiprocessing, os, json, random

class Conf():
    def __init__(self):
        self.pnum = 3
        self.max_pnum = 25
        self.times = 3
        self.tunit = 0
        self.rawdir = 'raw/'
        self.isNodump = False

    def printconf(self):
        print('pnum = ' + str(self.pnum))
        print('max_pnum = ' + str(self.max_pnum))
        print('times = ' + str(self.times))
        print('tunit = ' + str(self.tunit))
        print('rawdir = ' + str(self.rawdir))
        print('isNodump = ' + str(self.isNodump))

    def clearRaw(self):
        files = os.listdir(self.rawdir)
        for f in files:
            os.remove(self.rawdir + f)

    def load(self, path):
        tmp = {}
        with open(path) as config:
            tmp = json.load(config)
        self.pnum = tmp['pnum']
        self.max_pnum = tmp['max_pnum']
        self.times = tmp['times']
        self.tunit = tmp['tunit']
        self.rawdir = tmp['rawdir']
        self.isNodump = tmp['isNodump']

    def save(self, path):
        tmp = {'pnum' : self.pnum,
            'max_pnum' : self.max_pnum,
            'times' : self.times,
            'tunit' : self.tunit,
            'rawdir' : self.rawdir,
            'isNodump' : self.isNodump}
        with open(path, 'w') as out:
            json.dump(tmp, out)

default = Conf()

def multitest(conf = default):
    pool = multiprocessing.Pool(conf.max_pnum)
    for i in range(conf.pnum):
        pool.apply_async(singletest, args = (conf,))
    pool.close()
    try:
        pool.join()
    except KeyboardInterrupt:
        pool.terminate()
    except Exception as e:
        print(e)

def singletest(conf = default):
    time.sleep(random.randint(1, 1000) / 1000)
    data = analyze.Data(os.getpid())
    try:
        for i in range(conf.times):
            tup = unit.runtest(conf.tunit)
            data.add(tup)
            print(data.pid + ':' + str(i) + ': adding data: ' + str(tup))
            time.sleep(random.randint(1, 1000) / 1000)
    except KeyboardInterrupt:
        if conf.isNodump:
            return
    except Exception as e:
        print(e)
    data.summary()
    data.save(conf.rawdir + str(data.pid))
