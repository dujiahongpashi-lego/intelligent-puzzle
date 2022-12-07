import random
from mindstorms import MSHub, Motor, DistanceSensor
from mindstorms.control import wait_for_seconds
import math

# 7的倍数最佳
X_MAX_DC = 1099
Y_MAX_DC = 819

motor_track = Motor('C')
motor_bar = Motor('E')
motor_track.set_default_speed(100)
motor_bar.set_default_speed(100)
motor_track.set_degrees_counted(0)
motor_bar.set_degrees_counted(0)

# 开始前需以左下设为基准，启动程序校验
motor_track.run_to_degrees_counted(Y_MAX_DC)
wait_for_seconds(0.5)
motor_bar.run_to_degrees_counted(X_MAX_DC)
wait_for_seconds(0.5)
motor_track.run_to_degrees_counted(0)
wait_for_seconds(0.5)
motor_bar.run_to_degrees_counted(0)
wait_for_seconds(0.5)

# x:0-7, y:0-7


def move_to(x, y):
    x_stp = int(X_MAX_DC / 7)
    y_stp = int(Y_MAX_DC / 7)
    to_x = x * x_stp
    to_y = (7 - y) * y_stp
    motor_bar.run_to_degrees_counted(to_x)
    motor_track.run_to_degrees_counted(to_y)


answer = [[['A', 'D', 'D', 'D', 'E', 'E', 'E', 'E'], ['A', 'D', 'D', 'D', 'E', 'E', 'E', 'E'], ['A', 'B', 'B', 'G', 'G', 'G', 'G', 'G'], ['A', 'B', 'B', 'G', 'G', 'G', 'G', 'G'], ['1', '3', 'F', 'F', 'F', 'H', 'H', 'H'], ['2', '3', 'F', 'F', 'F', 'H', 'H', 'H'], ['2', '3', 'F', 'F', 'F', 'H', 'H', 'H'], ['C', 'C', 'C', 'C', 'C', 'H', 'H', 'H']],
        [['A', 'C', 'G', 'G', 'H', 'H', 'H', 'H'], ['A', 'C', 'G', 'G', 'H', 'H', 'H', 'H'], ['A', 'C', 'G', 'G', 'H', 'H', 'H', 'H'], ['A', 'C', 'G', 'G', 'F', 'F', 'F', '3'], [
            '2', 'C', 'G', 'G', 'F', 'F', 'F', '3'], ['2', '1', 'D', 'D', 'F', 'F', 'F', '3'], ['B', 'B', 'D', 'D', 'E', 'E', 'E', 'E'], ['B', 'B', 'D', 'D', 'E', 'E', 'E', 'E']],
        [['2', '2', 'A', 'A', 'A', 'A', 'B', 'B'], ['G', 'G', 'G', 'G', 'G', '1', 'B', 'B'], ['G', 'G', 'G', 'G', 'G', 'D', 'D', 'D'], ['C', 'E', 'E', 'E', 'E', 'D', 'D', 'D'], [
            'C', 'E', 'E', 'E', 'E', 'H', 'H', 'H'], ['C', '3', 'F', 'F', 'F', 'H', 'H', 'H'], ['C', '3', 'F', 'F', 'F', 'H', 'H', 'H'], ['C', '3', 'F', 'F', 'F', 'H', 'H', 'H']],
        [['2', '2', 'G', 'G', 'E', 'E', 'E', 'E'], ['1', 'C', 'G', 'G', 'E', 'E', 'E', 'E'], ['A', 'C', 'G', 'G', 'F', 'F', 'F', '3'], ['A', 'C', 'G', 'G', 'F', 'F', 'F', '3'], [
            'A', 'C', 'G', 'G', 'F', 'F', 'F', '3'], ['A', 'C', 'H', 'H', 'H', 'H', 'D', 'D'], ['B', 'B', 'H', 'H', 'H', 'H', 'D', 'D'], ['B', 'B', 'H', 'H', 'H', 'H', 'D', 'D']],
        [['1', 'A', 'A', 'A', 'A', 'D', 'D', 'D'], ['G', 'G', 'G', 'G', 'G', 'D', 'D', 'D'], ['G', 'G', 'G', 'G', 'G', 'F', 'F', 'F'], ['C', 'E', 'E', 'E', 'E', 'F', 'F', 'F'], [
            'C', 'E', 'E', 'E', 'E', 'F', 'F', 'F'], ['C', '2', 'B', 'B', 'H', 'H', 'H', 'H'], ['C', '2', 'B', 'B', 'H', 'H', 'H', 'H'], ['C', '3', '3', '3', 'H', 'H', 'H', 'H']],
        [['1', '2', '2', 'A', 'A', 'A', 'A', 'C'], ['D', 'D', 'B', 'B', '3', '3', '3', 'C'], ['D', 'D', 'B', 'B', 'F', 'F', 'F', 'C'], ['D', 'D', 'G', 'G', 'F', 'F', 'F', 'C'], [
            'E', 'E', 'G', 'G', 'F', 'F', 'F', 'C'], ['E', 'E', 'G', 'G', 'H', 'H', 'H', 'H'], ['E', 'E', 'G', 'G', 'H', 'H', 'H', 'H'], ['E', 'E', 'G', 'G', 'H', 'H', 'H', 'H']],
        [['1', '2', '2', 'A', 'A', 'A', 'A', 'C'], ['G', 'G', 'E', 'E', '3', '3', '3', 'C'], ['G', 'G', 'E', 'E', 'F', 'F', 'F', 'C'], ['G', 'G', 'E', 'E', 'F', 'F', 'F', 'C'], [
            'G', 'G', 'E', 'E', 'F', 'F', 'F', 'C'], ['G', 'G', 'H', 'H', 'H', 'H', 'D', 'D'], ['B', 'B', 'H', 'H', 'H', 'H', 'D', 'D'], ['B', 'B', 'H', 'H', 'H', 'H', 'D', 'D']],
        [['2', '2', '1', 'E', 'E', 'E', 'E', 'C'], ['F', 'F', 'F', 'E', 'E', 'E', 'E', 'C'], ['F', 'F', 'F', 'H', 'H', 'H', '3', 'C'], ['F', 'F', 'F', 'H', 'H', 'H', '3', 'C'], [
            'A', 'B', 'B', 'H', 'H', 'H', '3', 'C'], ['A', 'B', 'B', 'H', 'H', 'H', 'D', 'D'], ['A', 'G', 'G', 'G', 'G', 'G', 'D', 'D'], ['A', 'G', 'G', 'G', 'G', 'G', 'D', 'D']],
        [['1', '2', '2', 'A', 'A', 'A', 'A', 'C'], ['G', 'G', 'D', 'D', '3', '3', '3', 'C'], ['G', 'G', 'D', 'D', 'F', 'F', 'F', 'C'], ['G', 'G', 'D', 'D', 'F', 'F', 'F', 'C'], [
            'G', 'G', 'E', 'E', 'F', 'F', 'F', 'C'], ['G', 'G', 'E', 'E', 'H', 'H', 'H', 'H'], ['B', 'B', 'E', 'E', 'H', 'H', 'H', 'H'], ['B', 'B', 'E', 'E', 'H', 'H', 'H', 'H']],
        [['2', '2', '1', 'C', 'C', 'C', 'C', 'C'], ['H', 'H', 'H', 'B', 'B', 'D', 'D', 'D'], ['H', 'H', 'H', 'B', 'B', 'D', 'D', 'D'], ['H', 'H', 'H', 'G', 'G', 'G', 'G', 'G'], [
            'H', 'H', 'H', 'G', 'G', 'G', 'G', 'G'], ['A', 'A', 'A', 'A', 'F', 'F', 'F', '3'], ['E', 'E', 'E', 'E', 'F', 'F', 'F', '3'], ['E', 'E', 'E', 'E', 'F', 'F', 'F', '3']],
        [['2', '2', '1', 'B', 'B', 'A', 'E', 'E'], ['H', 'H', 'H', 'B', 'B', 'A', 'E', 'E'], ['H', 'H', 'H', 'G', 'G', 'A', 'E', 'E'], ['H', 'H', 'H', 'G', 'G', 'A', 'E', 'E'], [
            'H', 'H', 'H', 'G', 'G', '3', '3', '3'], ['D', 'D', 'D', 'G', 'G', 'F', 'F', 'F'], ['D', 'D', 'D', 'G', 'G', 'F', 'F', 'F'], ['C', 'C', 'C', 'C', 'C', 'F', 'F', 'F']],
        [['2', '2', '1', 'E', 'E', 'E', 'E', 'A'], ['3', '3', '3', 'E', 'E', 'E', 'E', 'A'], ['C', 'C', 'C', 'C', 'C', 'B', 'B', 'A'], ['G', 'G', 'G', 'G', 'G', 'B', 'B', 'A'], [
            'G', 'G', 'G', 'G', 'G', 'H', 'H', 'H'], ['D', 'D', 'F', 'F', 'F', 'H', 'H', 'H'], ['D', 'D', 'F', 'F', 'F', 'H', 'H', 'H'], ['D', 'D', 'F', 'F', 'F', 'H', 'H', 'H']],
        [['C', 'F', 'F', 'F', 'E', 'E', 'E', 'E'], ['C', 'F', 'F', 'F', 'E', 'E', 'E', 'E'], ['C', 'F', 'F', 'F', 'A', 'A', 'A', 'A'], ['C', 'B', 'B', 'H', 'H', 'H', 'H', '3'], [
            'C', 'B', 'B', 'H', 'H', 'H', 'H', '3'], ['2', '2', '1', 'H', 'H', 'H', 'H', '3'], ['D', 'D', 'D', 'G', 'G', 'G', 'G', 'G'], ['D', 'D', 'D', 'G', 'G', 'G', 'G', 'G']],
        ]


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

    def findBlock(self, block):
        name = block.name
        a = self.find(block.name)
        if a[0] == -1:
            return [-1, -1, name, -1]
        w = block.w
        h = block.h
        direction = 0
        if a[0]+w-1 > 7 or a[1]+h-1 > 7:
            direction = 1
        elif self.plateArray[a[1]+h-1][a[0]+w-1] != name:
            direction = 1
        return [a[0], a[1], name, direction]

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


puzzle = Plate(width=8, height=8)
#puzzle.changeTo(answer[random.randint(0, len(answer)-1)])
puzzle.changeTo(answer[8])
puzzle.draw()

hub = MSHub()
dc = DistanceSensor('B')
dist_cm = dc.get_distance_cm()

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
blocks = [block_3, block_2, block_1, block_H, block_G, block_F, block_E, block_D,
        block_C, block_B, block_A]
current_block = 0

def hub_show_next(index):
    next_name = blocks[index].name
    hub.light_matrix.write(next_name)
    print(next_name)

hub_show_next(current_block)

while True:
    wait_for_seconds(0.1)
    if hub.left_button.was_pressed():
        move_to(0, 7)
        current_block = 0
        hub_show_next(current_block)
    if hub.right_button.was_pressed():
        current_block = 0
        puzzle.changeTo(answer[random.randint(0, len(answer)-1)])
        puzzle.draw()
        hub_show_next(current_block)
        move_to(3, 3)
    dist_cm = dc.get_distance_cm()
    if dist_cm != None and dist_cm < 5:
        target_position = puzzle.findBlock(blocks[current_block])
        print(target_position[0], target_position[1])
        move_to(target_position[0], target_position[1])
        hub_image = 'ARROW_S'
        if target_position[3] == 1:
            hub_image = 'ARROW_E'
        hub.light_matrix.show_image(hub_image)

        wait_for_seconds(7.5)
        print('Ready')
        current_block += 1
        if current_block == len(blocks):
            current_block -= 1
        hub_show_next(current_block)
        hub.speaker.beep()
