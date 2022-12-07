import random

class Block:
    def __init__(self, width=1, height=1, name=0):
        self.h = height
        self.w = width
        self.name = name


class Plate:
    def __init__(self, width=8, height=8):
        self.width = width
        self.height = height
        self.plateArray = [['0'] * width for _ in range(height)]
        self._initPlate()

    def _initPlate(self):
        for i in range(self.height):
            for j in range(self.width):
                self.plateArray[i][j] = '0'

    def draw_detail(self):
        for i in range(self.height):
            print(i, self.plateArray[i])

    def draw(self):
        line = ''
        for i in range(self.height):
            for j in range(self.width):
                line += self.plateArray[i][j] + ' '
            print(line)
            line = ''

    def putBlock(self, block, x=0, y=0, direction=0):
        h = [block.w, block.h][direction == 0]
        w = [block.h, block.w][direction == 0]
        n = block.name
        if h + y > self.height or w + x > self.width:
            # print('超边 放不下')
            return False

        if not self._isEmptySubBlock(x, y, w, h):
            # print('这区域里有别的东西，放不下')
            return False

        self._updateSubBlock(x, y, w, h, n)
        return True

    def erasureBlock(self, block, x=0, y=0, direction=0):
        h = [block.w, block.h][direction == 0]
        w = [block.h, block.w][direction == 0]
        self._updateSubBlock(x, y, w, h, '0')

    def erasurePlace(self, x=0, y=0, width=1, height=1):
        for i in range(height):
            for j in range(width):
                self.plateArray[y + i][x + j] = '0'

    def erasureAreas(self, n):
        for i in range(self.height):
            for j in range(self.width):
                if (self.plateArray[i][j] == n):
                    self.plateArray[i][j] = 0

    def have(self, name):
        for i in range(self.height):
            for j in range(self.width):
                if (self.plateArray[i][j] == name):
                    return True
        return False

    def find(self, name):
        for i in range(self.height):
            for j in range(self.width):
                if (self.plateArray[i][j] == name):
                    return [j, i, name]
        return [-1, -1, name]

    def changeTo(self, plateArray):
        self.height = len(plateArray)
        self.width = len(plateArray[0])
        self.plateArray = plateArray

    def changeByNuM(self, num):
        decode_map = {
            '0001': '1',
            '0010': '2',
            '0011': '3',
            '1000': 'A',
            '1001': 'B',
            '1010': 'C',
            '1011': 'D',
            '1100': 'E',
            '1101': 'F',
            '1110': 'G',
            '1111': 'H',
        }
        str = bin(num)[2:]
        for i in range(self.height):
            for j in range(self.width):
                index = (i*self.height + j)*4
                self.plateArray[i][j] = decode_map[str[index: index+4]]

    def _isEmptySubBlock(self, x=0, y=0, width=1, height=1):
        valueChecker = '0'
        for i in range(height):
            for j in range(width):
                currentPotValue = self.plateArray[y + i][x + j]
                if currentPotValue != '0':
                    valueChecker = currentPotValue

        return valueChecker == '0'

    def _updateSubBlock(self, x=0, y=0, width=1, height=1, n='0'):
        for i in range(height):
            for j in range(width):
                self.plateArray[y + i][x + j] = n

    def _randomPosition():
        x = random.randint(0, 7)
        y = random.randint(0, 7)
        dir = random.randint(0, 1)
        return x, y, dir

    def _putRandom(self, block):
        x, y, dir = Plate._randomPosition()
        if not self.putBlock(block, x, y, dir):
            self._putRandom(block)

    def randomInitAs123(self):
        # 随机出题
        self._initPlate()
        block1 = Block(1, 1, '1')
        block2 = Block(1, 2, '2')
        block3 = Block(1, 3, '3')
        self._putRandom(block1)
        self._putRandom(block2)
        self._putRandom(block3)

    def randomInitAs123(self):
        self.randomInit([Block(1, 1, '1'), Block(1, 2, '2'), Block(1, 3, '3')])

    def randomInitAs123H(self):
        self.randomInit([Block(1, 1, '1'), Block(1, 2, '2'),
                        Block(1, 3, '3'), Block(3, 4, 'H')])

    def randomInitAsGH(self):
        self.randomInit([Block(2, 5, 'G'), Block(3, 4, 'H')])

    def randomInit(self, seed):
        self._initPlate()
        for s in seed:
            self._putRandom(s)

    def putBlocks(self, blocks):
        # 深度优先递归
        b = blocks[0]
        directions = ([0, 1], [0])[b.w == b.h]
        for i in range(self.height):
            for j in range(self.width):
                for dir in directions:
                    # 尝试在ji位置放置一块
                    if self.putBlock(b, j, i, dir):
                        currenBlockCount = len(blocks)
                        if currenBlockCount == 1:
                            # 放置成功后发现已经是最后一块了，
                            return True

                        remainingBlocks = blocks[1: currenBlockCount]
                        if self.putBlocks(remainingBlocks):
                            # 对剩下的块深度优先递归，看看是否成功
                            return True

                        # 剩下的块都递归完了，并未成功，则擦除当前块
                        self.erasureBlock(b, j, i, dir)

        # 所有位置都遍历了一遍还未成功，则此次递归失败
        return False

plate = Plate(width=8, height=8)
block_H = Block(3, 4, 'H')# 白 12
block_G = Block(2, 5, 'G')# 白 10
block_F = Block(3, 3, 'F')# 黄 9
block_E = Block(2, 4, 'E')# 红 8
block_D = Block(2, 3, 'D')# 红 6
block_C = Block(1, 5, 'C')# 白 5
block_B = Block(2, 2, 'B')# 白 4
block_A = Block(1, 4, 'A')# 红 4
block_1 = Block(1, 1, '1')# 蓝 1
block_2 = Block(1, 2, '2')# 蓝 2
block_3 = Block(1, 3, '3')# 蓝 3

freeBlocks = [block_H, block_G, block_F, block_E, block_D, block_C, block_B, block_A]

print('Start...')
import time
start = time.time()
plate.randomInitAs123()
plate.putBlocks(freeBlocks)
end = time.time()
print('Total time used:', end - start, 's')

