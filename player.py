__author__ = 'DELL'

import map
import random


class Player:

    def __init__(self, name, balance, m):
        self.name = name
        self.balance = balance
        self.pos = 0
        self.again = False
        self.finish = True
        self.map = m

    # def execute(self):
    #     if self.pos == 1 or self.pos == 16 or self.pos == 34:
    #         print("at fortune box")
    #     elif self.pos == 4 or self.pos == 26:
    #         print("at rotate plate")
    #     elif self.pos == 6 or self.pos == 24 or self.pos == 36:
    #         print("at lucky leaf")
    #     elif self.pos == 10:
    #         print("at prison")
    #     elif self.pos == 30:
    #         print("at court")
    #     elif self.pos == 20:
    #         print("at parking lot")
    #     elif self.pos == 39:
    #         print("at parking fee")
    #     else:
    #         print("at other places")

    def trade(self):
        print("trade")

    def build(self):
        print("build")
        i = 0
        while i < len(self.map.map):
            ownall = True
            if self.map.map[i].type == 'l' and self.map.map[i].owner == self:
                while self.map.map[i].type == 'l':
                    if self.map.map[i].owner == self:
                        i += 1
                    else:
                        ownall = False
                        break
                if ownall:
                    print("adjacent land!")
                    k = i - 1
                    if self.map.map[k].fee <= 100: # 判断是否有房子
                        print("build house")
                        while self.map.map[k].type == 'l':
                            self.map.map[k].fee *= 10
                            self.balance -= 500
                            print("build house at %s" % self.map.map[k].name)
                            k -= 1
                else:
                    while self.map.map[i].type == 'l':
                        i += 1

            else:
                if self.map.map[i].type != 'l':
                    i += 1
                else:
                    while self.map.map[i].type == 'l':
                        i += 1




    def roll(self):
        self.finish = False
        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        self.again = False
        if r1 == r2:
            self.again = True
        print("%s gets %d and %d" % (self.name, r1, r2))
        self.pos += r1 + r2
        if self.pos >= len(self.map.map):
            self.pos -= len(self.map.map)
            #self.balance += 200
            print("%s finishes one loop, add 200" % self.name)
        self.map.count[self.pos] += 1
        print("%s goes to block %d" % (self.name, self.pos))
        self.map.map[self.pos].exec(self)
        if self.again:
            print("Bao zi!")
            self.roll()
        else:
            self.trade()
            self.build()
            self.finish = True
