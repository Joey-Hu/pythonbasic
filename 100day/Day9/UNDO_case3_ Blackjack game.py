# @author: huhao
# @file: UNDO_case3_ Blackjack game.py
# @time: 2019/7/17 16:03
# @Document：https://www.python.org/doc/
# @desc:

import random
import numpy as np
from sys import exit


poker_name = ['♦10', '♦2', '♦3', '♦4', '♦5', '♦6', '♦7', '♦8', '♦9', '♦A', '♦J', '♦K', '♦Q',
 '♣10', '♣2', '♣3', '♣4', '♣5', '♣6', '♣7', '♣8', '♣9', '♣A', '♣J', '♣K', '♣Q',
 '♥10', '♥2', '♥3', '♥4', '♥5', '♥6', '♥7', '♥8', '♥9', '♥A', '♥J', '♥K', '♥Q',
 '♠10', '♠2', '♠3', '♠4', '♠5', '♠6', '♠7', '♠8', '♠9', '♠A', '♠J', '♠K', '♠Q']

poker_value = {'♣A':1,'♥A':1,'♠A':1,'♦A':1,'♦10': 10, '♦2': 2, '♦3': 3, '♦4': 4, '♦5': 5, '♦6': 6, '♦7': 7, '♦8': 8, '♦9': 9,  '♦J': 10, '♦K': 10, '♦Q': 10,
 '♣10': 10, '♣2': 2, '♣3': 3, '♣4': 4, '♣5': 5, '♣6': 6, '♣7': 7, '♣8': 8, '♣9': 9,  '♣J': 10, '♣K': 10, '♣Q': 10,
 '♥10': 10, '♥2': 2, '♥3': 3, '♥4': 4, '♥5': 5, '♥6': 6, '♥7': 7, '♥8': 8, '♥9': 9,  '♥J': 10, '♥K': 10, '♥Q': 10,
 '♠10': 10, '♠2': 2, '♠3': 3, '♠4': 4, '♠5': 5, '♠6': 6, '♠7': 7, '♠8': 8, '♠9': 9,  '♠J': 10, '♠K': 10, '♠Q': 10}


def Dealing_Poker(poker_database):
    # 发一张牌，并在牌堆中删除这张牌
    return poker_database.pop(random.randint(0,len(poker_database)-1))

def Score_Count(hand_poker):
    Score = 0
    Have_Ace = False
    for k in hand_poker:
        Score += poker_value[k]
