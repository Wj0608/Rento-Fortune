__author__ = 'DELL'

import map
import player
import os
import sys
import random
import time
import multiprocessing
from multiprocessing import Process


def run(): #TODO: put player into a list
    m = map.Map()
    p1 = player.Player('player1', 5000, m)
    p2 = player.Player('player2', 5000, m)
    p3 = player.Player('player3', 5000, m)

    # m.map[2].owner = p1
    # m.map[3].owner = p1

    n = 0
    while p1.balance>0 and p2.balance>0 and p3.balance>0:
        print("\nRound %d" % n)
        print("Player 1's turn")
        p1.start()
        while not p1.finish:
            time.sleep(1)
        print("\nPlayer 2's turn")
        p2.start()
        while not p2.finish:
            time.sleep(1)
        print("\nPlayer 3's turn")
        p3.start()
        while not p3.finish:
            time.sleep(1)
        n += 1
    print(p1.balance)
    print(p2.balance)
    print(p3.balance)
    s = ""
    ss = ""
    for i in m.map:
        ss += str(i.fee) + " "
        if i.owner is None:
            s += "None "
        else:
            s += i.owner.name + " "
    print(s)
    print(ss)


if __name__ == '__main__':
    run()


