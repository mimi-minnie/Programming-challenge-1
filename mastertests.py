import multiples
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def test1(self):
        multiples.multiples(5,20)==[5,10,15] #Test 1 fails
        
    def test2(self):
        inlist = [1,2,3]
        total = 6
        assert (multiples.totalList(inlist) == total) #test 2 fails

if __name__ == '__main__':
    unittest.main()