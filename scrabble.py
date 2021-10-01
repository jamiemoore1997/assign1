from random import randint
from nltk.corpus import words
import time
import timeit
import threading 
import sys

class scrabble(object):
    def longshort_word():
        global min,max
        min=len(min(words.words(),key=len))
        max=len(max(words.words(),key=len))
        return min,max

    def timer():
        global timeTotal
        timeTotal=15   
        while timeTotal:  
            timer='{:02d}'.format(timeTotal)
            #print(timer,end="\r")
            time.sleep(1)
            timeTotal -= 1           
        print (' Time is up,Game Over!!!')
        #sys.exit(0)

    def is_word(word,x):
        word=word.lower()
        if len(word) != x:
            print('Length is not matching')
            return ('InvalidWordLength')
        elif word.isalpha() == False:
            print ('There is at least one wrong character')
            return('InvalidWordCharacter')
        elif word not in words.words():
            print('It is not in the dictionary')
            return('InvalidWord')
        return True
            
    def score(word,time_elasped):
        score_dict={"a": 1, "e": 1, "i": 1, "o": 1, "u": 1, "l": 1,
                    "n": 1, "r": 1, "s": 1, "t": 1, "d": 2, "g": 2,
                    "b": 3, "c": 3, "m": 3, "p": 3, "f": 4, "h": 4,
                    "v": 4, "w": 4, "y": 4, "k": 5, "j": 8, "x": 8,
                    "q": 10, "z": 10}
        point = 0
        for letter in word:
            point += score_dict[letter.lower()]
        if time_elasped <=5:
            return point
        elif 10>= time_elasped >5:
            return round(point*0.7,1)
        elif 15> time_elasped >10:
            return round(point*0.5,1)

    def play():
        timer_thread=threading.Thread(target=scrabble.timer)
        timer_thread.setDaemon(True)
        timer_thread.start()
        a,b= scrabble.longshort_word() 
        x=randint(a,b)
        print('*************************')
        print('Find word with'+' '+str(x)+' '+'letters')
        while True:
            word=str(input('X: '))  
            if scrabble.is_word(word,x) == True:                
                time_elasped=15-timeTotal
                score= scrabble.score(word,time_elasped)
                print('  You got '+str(score)+' score')
                sys.exit(0)   
            else:
                continue 

if __name__ == '__main__':
    scrabble.play()




