class Block {
    constructor(width = 1, height = 1, name = 0) {
        this.h = height
        this.w = width
        this.name = name
    }
}

class Plate {
    constructor(width = 8, height = 8) {
        this.width = width
        this.height = height
        this.plateArray = new Array()
        this._init()
    }

    _init() {
        for (let i = 0; i < this.height; i++) {
            this.plateArray[i] = new Array(this.width)
            for (let j = 0; j < this.width; j++) {
                this.plateArray[i][j] = 0;
            }
        }
    }

    draw() {
        for (let i = 0; i < this.height; i++) {
            for (let j = 0; j < this.width; j++) {
                process.stdout.write(this.plateArray[i][j] + ' ')
            }
            console.log(' ')
        }
    }

    getArrayString() {
        return Plate.arrayToFormattedString(this.plateArray)
    }

    static arrayToFormattedString(theArray) {
        return '[' + theArray.map(line => '[' + line.map(c => '\'' + c + '\'').toString() + ']') + ']'
    }

    static arrayToTupleString(theArray) {
        return '(' + theArray.map(line => '(' + line.map(c => '\'' + c + '\'').toString() + ')') + ')'
    }

    // 获取旋转矩阵。将最小的数字转到左上角。用于Plate间比大小，For Sort
    getRotate() {
        const cornerElements = [this.plateArray[0][0], this.plateArray[7][0], this.plateArray[7][7], this.plateArray[0][7]] // 左上，左下，右下，右上
        const minElemenmt = cornerElements.reduce((p, c) => p < c ? p : c)
        const minIndex = cornerElements.indexOf(minElemenmt)
        const rotatedPlateArray = new Array()
        for (let i = 0; i < this.height; i++) {
            rotatedPlateArray[i] = new Array(this.width)
            for (let j = 0; j < this.width; j++) {
                switch (minIndex) {
                    case 0:
                        rotatedPlateArray[i][j] = this.plateArray[i][j]
                        break;
                    case 1: // 顺时针转90度
                        rotatedPlateArray[i][j] = this.plateArray[this.width - 1 - j][i]
                        break;
                    case 2: // 顺时针转180度
                        rotatedPlateArray[i][j] = this.plateArray[this.height - 1 - i][this.width - 1 - j]
                        break;
                    case 3: // 顺时针转270度
                        rotatedPlateArray[i][j] = this.plateArray[j][this.height - 1 - i]
                        break;
                }
            }
        }
        return rotatedPlateArray
    }


    //position start from (0, 0) (x, y)
    // 目前仅支持规则矩形
    //direction 0 for 正常角度
    //direction 1 for 转90度放入该位置
    putBlock(block, x = 0, y = 0, direction = 0) {
        const h = direction == 0 ? block.h : block.w
        const w = direction == 0 ? block.w : block.h
        const n = block.name
        if (h + y > this.height || w + x > this.width) {
            //console.log('超边 放不下')
            return false
        }
        if (!this._isEmptySubBlock(x, y, w, h)) {
            //onsole.log('这区域里有别的东西，放不下')
            return false
        }
        this._updateSubBlock(x, y, w, h, n)
        return true
    }

    // 擦除具体Block
    erasureBlock(block, x = 0, y = 0, direction = 0) {
        const h = direction == 0 ? block.h : block.w
        const w = direction == 0 ? block.w : block.h
        this._updateSubBlock(x, y, w, h, 0)
    }

    // 擦除指定区域
    erasurePlace(x = 0, y = 0, width, height) {
        for (let i = 0; i < height; i++) {
            for (let j = 0; j < width; j++) {
                this.plateArray[y + i][x + j] = 0
            }
        }
    }

    changeTo(plateArray) {
        this.height = plateArray.length
        this.width = plateArray[0].length
        this.plateArray = plateArray
        return this
    }

    update(names, byPlate) {
        for (let i = 0; i < byPlate.height; i++) {
            for (let j = 0; j < byPlate.width; j++) {
                if (names.includes(byPlate.plateArray[i][j])) {
                    this.plateArray[i][j] = byPlate.plateArray[i][j]
                }
            }
        }
    }

    // 擦除指定内容
    erasureAreas(n) {
        for (let i = 0; i < this.height; i++) {
            for (let j = 0; j < this.width; j++) {
                if (this.plateArray[i][j] == n) {
                    this.plateArray[i][j] = 0
                }
            }
        }
    }

    // 发现指定内容
    have(name) {
        for (let i = 0; i < this.height; i++) {
            for (let j = 0; j < this.width; j++) {
                if (this.plateArray[i][j] == name) {
                    return true
                }
            }
        }
        return false
    }

    // 查找指定内容，返回坐标
    find(name) {
        for (let i = 0; i < this.height; i++) {
            for (let j = 0; j < this.width; j++) {
                if (this.plateArray[i][j] == name) {
                    return [j, i, name]
                }
            }
        }
        return [-1, -1, name]
    }

    _isEmptySubBlock(x = 0, y = 0, width, height) {
        if (this.plateArray[y][x] != 0) {
            return false
        }
        const subBlock = new Array() // 中转变量
        let valueChecker = 0
        for (let i = 0; i < height; i++) {
            subBlock[i] = new Array(width)
            for (let j = 0; j < width; j++) {
                const currentPotValue = this.plateArray[y + i][x + j]
                subBlock[i][j] = currentPotValue
                if (currentPotValue != 0) {
                    valueChecker = currentPotValue
                }
            }
        }
        return valueChecker == 0
    }

    _updateSubBlock(x = 0, y = 0, width, height, n) {
        for (let i = 0; i < height; i++) {
            for (let j = 0; j < width; j++) {
                this.plateArray[y + i][x + j] = n
            }
        }
    }

    _randomPosition() {
        const x = Math.floor((Math.random() * 8)) // 0-7
        const y = Math.floor((Math.random() * 8)) // 0-7
        const dir = Math.floor((Math.random() * 2)) // 0-1
        return { x, y, dir }
    }

    _putRandom(block) {
        const { x, y, dir } = this._randomPosition()
        if (!this.putBlock(block, x, y, dir)) {
            this._putRandom(block)
        }
    }

    // 随机出题--种子123
    randomInitAs123() {
        this.randomInit([new Block(1, 1, '1'), new Block(1, 2, '2'), new Block(1, 3, '3')])
    }

    // 随机出题--种子123H
    seed123H() {
        this.randomInit([new Block(1, 1, '1'), new Block(1, 2, '2'), new Block(1, 3, '3'), new Block(3, 4, 'H')])
    }

    // 随机出题--种子GH
    seedGH() {
        this.randomInit([new Block(2, 5, 'G'), new Block(3, 4, 'H')])
    }

    // 随机出题--种子FGH
    seedFGH() {
        this.randomInit([new Block(3, 3, 'F'), new Block(2, 5, 'G'), new Block(3, 4, 'H')])
    }

    // 随机出题--种子HGF1
    seedHGF1() {
        this.randomInit([new Block(3, 3, 'F'), new Block(2, 5, 'G'), new Block(3, 4, 'H'), new Block(1, 1, '1')])
    }

    // 以种子包生成随机种子
    randomInit(seed) {
        this._init()
        seed.forEach(e => this._putRandom(e))
    }

    // 深度优先递归
    putBlocks(blocks) {
        const b = blocks[0]
        const directions = b.w == b.h ? [0] : [0, 1]
        for (let i = 0; i < this.height; i++) {
            for (let j = 0; j < this.width; j++) {
                for (let dir in directions) {
                    // 尝试在ji位置放置一块
                    if (this.putBlock(b, j, i, dir)) {
                        const currenBlockCount = blocks.length
                        if (currenBlockCount == 1) {
                            // 放置成功后发现已经是最后一块了，
                            return true
                        }
                        const remainingBlocks = blocks.slice(1, currenBlockCount)
                        if (this.putBlocks(remainingBlocks)) {
                            // 对剩下的块深度优先递归，看看是否成功
                            return true
                        }
                        // 剩下的块都递归完了，并未成功，则擦除当前块
                        this.erasureBlock(b, j, i, dir)
                    }
                }
            }
        }
        // 所有位置都遍历了一遍还未成功，则此次递归失败
        return false
    }
}


// 用例：摆放自定义Block
// const plate = new Plate(width = 8, height = 8)
// const block = new Block(width = 3, height = 2, name = 'B')
// console.log(plate.putBlock(block, 1, 2))
// console.log(plate.putBlock(block, 2, 3))
// plate.draw()

// 用例：自动生成随机初始块
// const plate = new Plate(width = 8, height = 8)
// plate.randomInitAs123()
// plate.draw()

const plate = new Plate(width = 8, height = 8)
const block_H = new Block(3, 4, 'H')// 白 12
const block_G = new Block(2, 5, 'G')// 白 10
const block_F = new Block(3, 3, 'F')// 黄 9
const block_E = new Block(2, 4, 'E')// 红 8
const block_D = new Block(2, 3, 'D')// 红 6
const block_C = new Block(1, 5, 'C')// 白 5
const block_B = new Block(2, 2, 'B')// 白 4
const block_A = new Block(1, 4, 'A')// 红 4
const block_1 = new Block(1, 1, '1')// 蓝 1
const block_2 = new Block(1, 2, '2')// 蓝 2
const block_3 = new Block(1, 3, '3')// 蓝 3
let freeBlocks = [block_H, block_G, block_F, block_E, block_D, block_C, block_B, block_A]


let counter = 0
let start = new Date().getTime()
freeBlocks = [block_F, block_E, block_D, block_C, block_B, block_A, block_3, block_2, block_1]
while (counter < 24000) {
    plate.seedGH() // 优选随机种子
    if (plate.putBlocks(freeBlocks)) {
        counter++
    }
}
let end = new Date().getTime()
console.log('成功出题', counter, '个，用时', (end - start) / 1000, 's')
plate.draw()