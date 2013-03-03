'''
Created on Mar 2, 2013

@author: rmdobbins
'''
import unittest
import root.code.main


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_askAdditionQuestion(self):
        self.assertEqual("What is 1 + 1", root.code.main.generatePrompt('+', 1, 1))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()