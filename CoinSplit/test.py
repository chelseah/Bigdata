import unittest
import numpy as np
import scipy as sp
from CoinSplit import splitwithlist

class TestCoinSplit(unittest.TestCase):
    def setUp(self):
        return
    def testsplit_one(self):
        #split only with one
        self.assertTrue(splitwithlist(6,[1])==1)       
        self.assertTrue(splitwithlist(6,[5])==0)       

        return
    def testsplit_two(self):
        #split only with two coins 
        self.assertTrue(splitwithlist(6,[5,1])==2)       
        self.assertTrue(splitwithlist(6,[10,1])==1)       
        self.assertTrue(splitwithlist(11,[10,1])==2)       
        self.assertTrue(splitwithlist(15,[5,1])==4)       
        
        return
    def testsplit_three(self):
        self.assertTrue(splitwithlist(6,[10,5,1])==2)       
        self.assertTrue(splitwithlist(11,[25,10,1])==2)       
        self.assertTrue(splitwithlist(11,[10,5,1])==4)       
        self.assertTrue(splitwithlist(25,[10,5,1])==12)       
    def testsplit_four(self):
        self.assertTrue(splitwithlist(6,[25,10,5,1])==2)       
        self.assertTrue(splitwithlist(11,[25,25,10,1])==2)       
        self.assertTrue(splitwithlist(11,[25,10,5,1])==4)       
        self.assertTrue(splitwithlist(25,[25,10,5,1])==13)       

    def tearDown(self):

        return

if __name__=='__main__':
    unittest.main()

