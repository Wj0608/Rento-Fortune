__author__ = 'DELL'

import map
import random


class Player:

    def __init__(self, name, balance, m):
        self.name = name
        self.balance = balance
        self.pos = 0
        self.again = False  # �����ظ�����
        self.finish = True  # �غ��Ƿ����
        self.map = m
        self.prison = 0  # ��Ҫ���̶��ٻغ�
        self.prison_card = False
        self.protect_card = False

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
                    if self.map.map[k].fee <= 100: # �ж��Ƿ��з���
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
        r1 = random.randint(1, 6)
        r2 = random.randint(1, 6)
        self.again = False
        if r1 == r2:
            self.again = True
        print("%s gets %d and %d" % (self.name, r1, r2))
        if self.prison != 0:
            if r1 == r2:
                self.prison = 0
                print("lucky dog")
            else:
                print("still need %d turns" % self.prison)
                self.prison -= 1
                self.finish = True
                return
        self.pos += r1 + r2
        if self.pos >= len(self.map.map):
            self.pos -= len(self.map.map)
            #self.balance += 200  # һȦ��200
            print("%s finishes one loop, add 200" % self.name)
        self.map.count[self.pos] += 1
        print("%s goes to block %d" % (self.name, self.pos))
        self.map.map[self.pos].exec(self)
        if self.again:
            print("Bao zi!")
            self.roll()

    def start(self):
        self.finish = False
        if self.prison != 0:  #����ڷ���
            print("in prison")
            if not self.prison_card:  # û�г�����
                x = random.randint(0, 3)  # ģ������ж�����
                if x == 0:  # ��Ǯ����
                    self.balance -= 100
                    self.prison = 0
                    print("pay for freedom")
                # else:  # ����Ǯ
                #     if r1 == r2:
                #         self.prison = 0
                #         print("lucky dog")
                #     else:
                #         print("still need %d turns" % self.prison)
                #         self.prison -= 1
                #         self.finish = True
                #         return
            else:
                print("use a prison card")
                self.prison_card = False
                self.prison = 0
        self.roll()
        self.trade()
        self.build()
        self.finish = True

