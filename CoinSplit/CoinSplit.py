#!/usr/bin/env python
import numpy as np
import scipy as sp
import sys
from optparse import OptionParser

def read_command_line():
    #provide three utils for the code as the exercise requires.
    parser = OptionParser(usage='%prog [options]',
                          description='calculate the number of ways'
                          'to split amounts or a range of amount into' 
                          'coins with value [25,10,5,1].')
    parser.add_option('-s','--split',action='store',type='string',
                        help='the amount to split')
    parser.add_option('-r','--ranges',action='store',type='string',
                        help='amount from range one to the input number'
                             'will be splited.')
    parser.add_option('-e','--example',action='store_true',
                        help='answer the example required in exercise.')
    options,args = parser.parse_args()
    return options

def splitwithlist(target,lists):
    # Split target amount using the given list of coins
    # 1) iterate through the number of possible choices for 
    #    the biggest coin (first element in the list),
    #    assuming list is sorted.
    # 2) split the rest of amount with the rest of the list 
    #    by iteratively call itself.
    # 3) when there is only one type of coin left, 
    #    count as one type when divisible, otherwise 
    #    count as 0 type.
    ntop = int(target/lists[0])
    if(len(lists)==1):
        if(ntop*lists[0]==target):
            return 1
        else:
            return 0
    nsum=0
    for i in xrange(ntop+1):
        nsum+=splitwithlist(target-i*lists[0],lists[1:])
    return nsum

def main():
    lists = [25,10,5,1]
    options = read_command_line()
    if not options.split == None:
        ntotal=splitwithlist(eval(options.split),lists)
        print '################'
        print 'total number of splits: %d' % ntotal
    elif not options.ranges == None:
        for i in xrange(1,eval(options.ranges)+1):
            print i, splitwithlist(i,lists)
    elif (options.example):
        a = range(1,100)
        nsum=0
        noddsum=0
        for i in a[::5]:
            count=splitwithlist(i,lists)
            print i,count
            nsum+=count
            if(count%2==1):
                noddsum+=count
        ntotal=nsum*5
        nodd=noddsum*5
        print '################'
        print 'total number of splits for range 1-100: %d' % ntotal
        print 'sum of those who are odd: %d' % nodd

if __name__=='__main__':
    main()
