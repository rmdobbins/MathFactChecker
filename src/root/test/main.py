'''
Created on Mar 3, 2013

@author: rmdobbins
'''
import unittest
import root.code.main


class Test(unittest.TestCase):


    def setUp(self):
        self.test = root.code.main


    def tearDown(self):
        pass


    def testName(self):
        self.assertEqual("What is 1 + 1", self.test.generatePrompt())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    