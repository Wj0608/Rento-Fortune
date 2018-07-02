__author__ = 'DELL'

import map
import player
import time
import copy


def recover(p):
    for b in p.map.map:
        if b.owner == p:
            b.price = b.init_price
            b.fee = b.init_fee
            b.owner = None
            b.status = "n"


def run():
    m = map.Map()
    plist = []
    p1 = player.Player('player1', 5000, m)
    plist.append(p1)
    p2 = player.Player('player2', 5000, m)
    plist.append(p2)
    p3 = player.Player('player3', 5000, m)
    plist.append(p3)
    p4 = player.Player('player4', 5000, m)
    plist.append(p4)
    p5 = player.Player('player5', 5000, m)
    plist.append(p5)
    n = 0
    plist_copy = copy.copy(plist)
    while len(plist) > 1:
        print("\nRound %d" % n)
        for p in plist:
            print("%s's turn" % p.name)
            p.start()
            while not p.finish:
                time.sleep(1)
            i = 0
            while i < len(plist):
                if plist[i].balance < 0:
                    print("%s is out" % plist[i].name)
                    recover(plist[i])
                    plist.remove(plist[i])
                else:
                    i += 1
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
    print(m.count)


if __name__ == '__main__':
    run()