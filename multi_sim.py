# coding: utf-8
#from test import igunit, unit, analyze
from test import *
import os, time

def main():
    conf = igunit.Conf()
    conf.load('conf/multi_sim.conf')
    conf.clearRaw()
    igunit.multitest(conf)

main()
