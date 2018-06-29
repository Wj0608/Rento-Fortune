__author__ = 'DELL'

import map
import player
import time
import copy


def run():
    m = map.Map()
    plist = []
    p1 = player.Player('player1', 5000, m)
    p2 = player.Player('player2', 5000, m)
    p3 = player.Player('player3', 5000, m)
    plist.append(p1)
    plist.append(p2)
    plist.append(p3)
    n = 0
    plist_copy = copy.copy(plist)
    while len(plist) > 1:
        print("\nRound %d" % n)
        for p in plist:
            print("%s's turn" % p.name)
            p.start()
            while not p.finish:
                time.sleep(1)
            for pp in plist:
                if pp.balance < 0:
                    plist.remove(pp)
                    print("%s is over" % p.name)
        n += 1
    print("Game is over, %s wins the Rento Fortune!" % plist[0].name)

    for i in plist_copy:
        print("%s has %d balance" % (i.name, i.balance))
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


