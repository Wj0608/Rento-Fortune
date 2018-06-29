__author__ = 'DELL'

import block
from block import Block


class Map:

    def __init__(self):
        self.map = [Block('start', 's', 0, 0), Block('box', 'b', 0, 0), Block('libya', 'l', 100, 100), Block('sudan', 'l', 100, 100),
                    Block('rotate', 'r', 0, 0), Block('station japan', 'st', 50, 50), Block('fortune', 'f', 0, 0),
                    Block('turkey', 'l', 100, 100), Block('greece', 'l', 100, 100), Block('bulgaria', 'l', 100, 100),
                    Block('prison', 'p', 0, 0), Block('poland', 'l', 100, 100), Block('russia', 'l', 100, 100),
                    Block('ukraine', 'l', 100, 100), Block('church', 'ch', 0.2, 0.05), Block('station spain', 'st', 50, 50),
                    Block('box', 'b', 0, 0), Block('lithuania', 'l', 100, 100), Block('latvia', 'l', 100, 100),
                    Block('estonia', 'l', 100, 100), Block('parking lot', 'pk', 0, 0), Block('norway', 'l', 100, 100),
                    Block('sweden', 'l', 100, 100),Block('finland', 'l', 100, 100),Block('fortune', 'f', 0, 0),
                    Block('station usa', 'st', 50, 50), Block('rotate', 'r', 0, 0), Block('germany', 'l', 100, 100),
                    Block('france', 'l', 100, 100), Block('uk', 'l', 100, 100), Block('court', 'c', 0, 0), Block('canada', 'l', 100, 100),
                    Block('mexico', 'l', 100, 100), Block('usa', 'l', 100, 100), Block('box', 'b', 0, 0), Block('station uk', 'st', 50, 50),
                    Block('fortune', 'f', 0, 0), Block('dubai', 'l', 100, 100), Block('hawaii', 'l', 100, 100), Block('parking fee', 'pf', 0, 0)]
        self.count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

