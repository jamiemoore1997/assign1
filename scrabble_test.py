import unittest
from scrabble import *
import timeit
class TestScrabble(unittest.TestCase):
    #1.
    def test_is_word_upcase(self):
        self.assertEqual(scrabble.is_word('baiL',4),True)
        self.assertEqual(scrabble.is_word('HABIT',6),'InvalidWordLength')
        self.assertEqual(scrabble.is_word('xoXo',4),'InvalidWord')
    
    def test_score_upcase(self):
        self.assertEqual(scrabble.score('biLL',2),6)
        self.assertEqual(scrabble.score('BILL',7),4.2)    
    #2.
    def test_is_word_len(self):
        self.assertEqual(scrabble.is_word('bead',4),True)
        self.assertEqual(scrabble.is_word('habit',6),'InvalidWordLength')
    #3.
    def test_is_word_char(self):
        self.assertEqual(scrabble.is_word('hack',4),True)
        self.assertEqual(scrabble.is_word('/$$',3),'InvalidWordCharacter')
        self.assertEqual(scrabble.is_word(' ',1),'InvalidWordCharacter')
    #4.
    def test_is_word_dict(self):
        self.assertEqual(scrabble.is_word('bail',4),True)
        self.assertEqual(scrabble.is_word('abc',3),'InvalidWord')
        self.assertEqual(scrabble.is_word('xoxo',4),'InvalidWord')
    #5.
    def test_score(self):
        self.assertEqual(scrabble.score('bill',2),6)
        self.assertEqual(scrabble.score('bill',7),4.2)    
        self.assertEqual(scrabble.score('bill',12),3)

    #6.
    def test_longshort_word(self):
        a,b=scrabble.longshort_word()
        self.assertEqual(b,24)
        self.assertEqual(a,1)   
    #7.
    def test_play_15_secs(self):
        start=timeit.timeit()
        scrabble.timer()
        end=timeit.timeit()
        self.assertEqual(round(start-end),0)
        
    
if __name__ == '__main__':
    unittest.main()


