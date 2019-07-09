#!/usr/bin/python3
# coding: utf-8
from statistics import mean, median, stdev
import json, os

class Data():
    def __init__(self, pid):
        self.pid = str(pid)
        self.success = []
        self.err = []

    # tup = (time, error message)
    def add(self, tup):
        if tup[0] <= 0:
            self.err.append(tup)
        else:
            self.success.append(tup[0])

    def clear(self):
        self.success = []
        self.err = []

    def summary(self):
        print('*' * 10 + '\n'
            + self.pid + ': success = ' + str(len(self.success)) + '\n'
            + self.pid + ': fail = ' + str(len(self.err)))
        if len(self.success) <= 0:
            print(self.pid + ': All fail.')
        else:
            print(self.pid + ': avg = ' + str(mean(self.success)))
            print(self.pid + ': med = ' + str(median(self.success)))
            print(self.pid + ': stdev = ' + str(stdev(self.success)))

    # dump to a json file
    def save(self, file):
        tmp = {'pid' : self.pid,
            'success' : self.success,
            'err' : self.err}
        with open(file, 'w') as out:
            json.dump(tmp, out)
        print(self.pid + ': Save complete.')

    def load(self, file):
        with open(file) as i:
            tmp = json.load(i)
            self.success.extend(tmp['success'])
            self.err.extend(tmp['err'])
        print(self.pid + ': ' + tmp['pid'] + ' Load complete.')

    # load json file
    def loadAll(self, dir):
        files = os.listdir(dir)
        print('loading ' + str(files) + ' ...')
        for f in files:
            if f == '.keep':
                continue
            with open(dir + f) as jf:
                tmp = json.load(jf)
                self.success.extend(tmp['success'])
                self.err.extend(tmp['err'])
            print(self.pid + ': ' + tmp['pid'] + ' Load complete.')
