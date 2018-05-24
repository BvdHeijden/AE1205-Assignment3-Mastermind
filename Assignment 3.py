# -*- coding: utf-8 -*-
"""
Created on Thu May 24 09:36:56 2018

@author: vdhei
"""

from mastertools import gencode, goodplace, goodcolour

codelength=4
maxtries=10

print("\nLet's play Mastermind!")
while True:
    secret=gencode()
    secretstring=''.join(secret)
    
    print('\nI have a code of ',codelength,' numbers between 1 and 6.\nYou have ',maxtries,' turn to guess my code.')
    
    for turn in range(maxtries):
        instring=('Guess '+str(turn+1)+' : ')
        guess=input(instring)
        guess=list(guess)
        
        gp=goodplace(secret,guess)
        gc=goodcolour(secret,guess)
        
        if gp==codelength:
            print('\t!!!Correct!!!, the code was ',secretstring,'\nYou guessed the code in ',str(turn+1),' tries')
            break
        else:
            print('\tScore: ',gp,' good and ',gc,' good colour in the wrong position')
        
        if turn==(maxtries-1):
            print('\toh no! You failed to guess my code. it was ',secretstring,'.')
            break
    
    again=input("Do you want to play again? (y/n): ")
    if again!='y':
        break

    