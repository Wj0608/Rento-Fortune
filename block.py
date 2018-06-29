__author__ = 'DELL'

import random

class Block:

    def __init__(self, n, t, p, f):
        self.name = n
        self.type = t
        self.price = p
        self.fee = f
        self.owner = None
        self.status = "normal"
        self.pf = 0

    def exec(self, p):
        print("%s execute block %s" % (p.name, self.name))
        if self.type == 'l':  # 买地，收租金
            if self.owner is None:
                print("this is an empty land")
                self.owner = p
                p.balance -= self.price
            else:
                if self.owner == p:
                    print("this is my land")
                else:
                    if not p.is_protected:
                        print("Oops")
                        p.balance -= self.fee
                        self.owner.balance += self.fee
                    else:
                        p.is_protected = False
                        print("cancel one tax")
        if self.type == 'c':  # 法院
            print("go to prison")
            p.pos = 10
            p.prison = 3
        if self.type == 'pf':  # 停车扣100
            p.balance -= 100
            p.map.map[20].pf += 100
        if self.type == 'pk':  # 拿走所有累计停车费
            print("%d dollar in total at pk" % self.pf)
            p.balance += self.pf
            self.pf = 0
        if self.type == 'b':  # 宝箱
            print("pick a box to open")
            p.balance += random.randint(-100,300)
        if self.type == 'r':  # 转盘
            print("rotate the plate")
            x = random.randint(0,9)
            if x == 0:
                p.balance += 500
            elif x == 1:
                p.balance = 1000
            elif x == 2:
                p.balance += 200
            elif x == 3:
                p.balance += 100
            elif x == 4:
                p.balance -= 200
            elif x == 5:
                p.balance -= 100
            elif x == 6:
                p.balance *= 1.1
            elif x == 7:
                p.balance *= 1.2
            elif x == 8:
                p.balance *= 0.8
            elif x == 9:
                p.balance *= 0.9
        if self.type == 'f':  #幸运叶
            print("pick a fortune leaf")
            x = random.randint(0,10)
            if x == 0:
                print("go to hawaii")
                if p.pos > 38:  # 经过起点加200
                    p.balance += 200
                p.pos = 38
                p.map.map[38].exec(p)
            if x == 1:
                print("go to finland")
                if p.pos > 23:  # 经过起点加200
                    p.balance += 200
                p.pos = 23
                p.map.map[23].exec(p)
            if x == 2:
                print("go to next station")
                while p.map.map[p.pos].type != 'st':
                    p.pos += 1
                    if p.pos >= len(p.map.map):
                        p.pos -= len(p.map.map)
                        p.balance += 200
                p.map.map[p.pos].exec(p)
            if x == 3:
                print("go to start point")
                p.pos = 0
                p.balance += 200
            if x == 4:
                print("go to next empty land")
                for i in range(0,40):
                    p.pos += 1
                    if p.pos >= len(p.map.map):
                        p.pos -= len(p.map.map)
                        p.balance += 200
                    if (p.map.map[p.pos].type == 'l' or p.map.map[p.pos].type == 'st' or p.map.map[p.pos].type == 'ch') and p.map.map[p.pos].owner is None:
                        p.map.map[p.pos].exec(p)
                        return
                p.balance += random.randint(0,300)
            if x == 5:
                print("go to prison")
                p.pos = 10
                p.prison = 3
            if x == 6:
                print("-3")
                p.pos -= 3
                p.map.map[p.pos].exec(p)
            if x == 7:
                print("+1")
                p.pos += 1
                p.map.map[p.pos].exec(p)
            if x == 8:
                print("go to poland")
                if p.pos > 11:  # 经过起点加200
                    p.balance += 200
                p.pos = 11
                p.map.map[11].exec(p)
            if x == 9:
                print("get a prison card")
                p.prison_card = True
            if x == 10:
                print("get a protect card")
                p.protect_card = True
        if self.type == 'st':  # 车站
            if self.owner is None:
                print("this is an empty station")
                self.owner = p
                count = 0  # 该玩家拥有车站总数
                blist = []
                for b in p.map.map:
                    if b.type == 'st' and b.owner == p:
                        count += 1
                        blist.append(b)
                print("blist")
                print(blist)
                for b in blist:
                    b.fee = count * 50
                p.balance -= self.price
            else:
                if self.owner == p:
                    print("this is my station")
                else:
                    if not p.is_protected:
                        print("Oops")
                        p.balance -= self.fee
                        self.owner.balance += self.fee
                    else:
                        p.is_protected = False
                        print("cancel one tax")
            if self.owner == p:
                print("travel")  # TODO: travel
        if self.type == 'ch':  # 教堂 踩一脚付当前5%，自己踩得当前5%，价格为当前20%
            if self.owner is None:
                print("this is an empty church")
                self.owner = p
                p.balance *= (1 - self.price)
            else:
                if self.owner == p:
                    print("this is my church")
                    p.balance *= (1 + self.fee)
                else:
                    if not p.is_protected:
                        print("Oops")
                        self.owner.balance += p.balance * self.fee
                        p.balance *= (1 - self.fee)
                    else:
                        p.is_protected = False
                        print("cancel one tax")


