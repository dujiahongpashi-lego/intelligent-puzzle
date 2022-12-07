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

    // 以种子包生成随机种子
    randomInit(seed) {
        this._init()
        seed.forEach(e => this._putRandom(e))
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
    randomInitAs123H() {
        this.randomInit([new Block(1, 1, '1'), new Block(1, 2, '2'), new Block(1, 3, '3'), new Block(3, 4, 'H')])
    }

    // 随机出题--种子GH
    randomInitAsGH() {
        this.randomInit([new Block(2, 5, 'G'), new Block(3, 4, 'H')])
    }

    // 随机出题--种子FGH
    randomInitAsFGH() {
        this.randomInit([new Block(3, 3, 'F'), new Block(2, 5, 'G'), new Block(3, 4, 'H')])
    }

    // 随机出题--种子HGF1
    randomInitAsHGF1() {
        this.randomInit([new Block(3, 3, 'F'), new Block(2, 5, 'G'), new Block(3, 4, 'H'), new Block(1, 1, '1')])
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

// 出题模式
// console.log('出题：')
// plate.putBlock(block_1, 7, 2, 0) // 出题位置1
// plate.putBlock(block_2, 0, 2, 0) // 出题位置2
// plate.putBlock(block_3, 3, 3, 0) // 出题位置3
// plate.draw()
// console.log('解密：')
// plate.putBlocks(freeBlocks)
// plate.draw()

/*
// 随机出题/解密模式
console.log('开始随机出题/解密')
let counter = 1
let start = new Date().getTime()
freeBlocks = [block_H, block_G, block_F, block_E, block_D, block_C, block_B, block_A]
plate.randomInitAs123()
while (!plate.putBlocks(freeBlocks)) {
    counter++
    plate.randomInitAs123()
}
let end = new Date().getTime()
console.log('随机出题尝试共', counter, '次，总用时', end - start, 'ms')
// plate.draw()

// 更换成GH种子
counter = 1
start = new Date().getTime()
freeBlocks = [block_F, block_E, block_D, block_C, block_B, block_A, block_3, block_2, block_1]
plate.randomInitAsGH()
while (!plate.putBlocks(freeBlocks)) {
    counter++
    plate.randomInitAsGH()
}
end = new Date().getTime()
console.log('最优种子随机出题尝试共', counter, '次，总用时', end - start, 'ms')
// plate.draw()
// console.log(plate.getRotate())
// console.log(plate.getArrayString())

// 用最优种子尝试N次
counter = 0
let times = 0
start = new Date().getTime()
freeBlocks = [block_F, block_E, block_D, block_C, block_B, block_A, block_3, block_2, block_1] // 最优方式种子获得解10000个，随机出题尝试共 11130 次，总用时 6515 ms
// freeBlocks = [block_1, block_2, block_3, block_A, block_B, block_C, block_D, block_E, block_F] // 直接卡死
// freeBlocks = [block_E, block_D, block_C, block_B, block_A, block_3, block_2, block_1] // 最优方式种子获得解10000个，随机出题尝试共 12128 次，总用时 8026 ms
while (counter < 10) {
    plate.randomInitAsGH()
    times++
    if (plate.putBlocks(freeBlocks)) {
        counter++
    }

}
end = new Date().getTime()
console.log('最优方式种子获得解' + counter + '个，随机出题尝试共', times, '次，总用时', end - start, 'ms')
// plate.draw()
*/

// 生成、排序、去重、输出
const results = new Array()
counter = 0
times = 0
start = new Date().getTime()
//freeBlocks = [block_F, block_E, block_D, block_C, block_B, block_A, block_3, block_2, block_1] // 获得解10000个，去重后剩余1312个,随机出题尝试共 11165 次，总用时 6959 ms
//freeBlocks = [block_E, block_D, block_C, block_B, block_A, block_3, block_2, block_1] // 获得解10000个，去重后剩余4951个,随机出题尝试共 12091 次，总用时 8830 ms
freeBlocks = [block_E, block_D, block_C, block_B, block_A, block_3, block_2] // 获得解10000个，去重后剩余8794个,随机出题尝试共 29630 次，总用时 59245 ms|获得解15000个，去重后剩余12408个,随机出题尝试共 44570 次，总用时 89308 ms
while (counter < 1800) {
    plate.randomInitAsHGF1()
    times++
    if (plate.putBlocks(freeBlocks)) {
        results.push(plate.getRotate()) // 转制
        counter++
    }
}
// 排序
const sortedResults = results.sort((a, b) => {
    for (let i = 0; i < a.length; i++) {
        for (let j = 0; j < a[i].length; j++) {
            if (a[i][j] < b[i][j]) {
                return -1
            }
            else if (a[i][j] > b[i][j]) {
                return 1
            }
        }
    }
    return 0
})
// 去重
let duplicateRemoved = sortedResults.reduce((p, c) => {
    const l = p.length
    if (l == 0) {
        return [c]
    }
    const last = p[l - 1]
    let eq = true
    for (let i = 0; i < c.length; i++) {
        for (let j = 0; j < c[i].length; j++) {
            if (c[i][j] != last[i][j]) {
                eq = false
            }
        }
    }
    if (!eq) {
        p.push(c)
    }
    return p
}, [])
end = new Date().getTime()
console.log('获得解' + counter + '个，去重后剩余' + duplicateRemoved.length + '个,随机出题尝试共', times, '次，总用时', end - start, 'ms')

// 洗牌 (随便用了个办法打乱顺序)(可不执行)
duplicateRemoved = duplicateRemoved.sort((a, b) => a[5][1] > b[1][5] ? 1 : (a[5][1] == b[1][5] ? (a[3][3] < b[3][3] ? 1 : -1) : -1))

//输出到文件
const fs = require('fs')
fs.writeFile('./data_formatted.txt', '', () => { })// 清空
// duplicateRemoved.forEach((a, i) => fs.writeFile('./data_formatted.txt', Plate.arrayToFormattedString(a) + ',\r\n', { 'flag': 'a' }, err => console.log(i + '/' + duplicateRemoved.length, err)))
duplicateRemoved.forEach((a, i) => fs.writeFile('./data_formatted.txt', Plate.arrayToFormattedString(a) + ',\r\n', { 'flag': 'a' }, err => {}))

// 编码
const getEncode = (plate, keyBlocks) => {
    binCodeArray = keyBlocks.map(b => {
        const name = b.name
        const position = plate.find(name)
        const x = position[0]
        const y = position[1]
        const direction = (y + b.h <= plate.height && x + b.w - 1 <= plate.width && plate.plateArray[y + b.h - 1][x + b.w - 1] == name) ? 0 : 1
        return BigInt((x << 4) + (y << 1) + direction)
    })
    return binCodeArray.reduce((p, c) => (p << 7n) + c, 0n)
}

// 解码
const decodeToPlate = (targetPlate, code, keyBlocks, otherBlocks) => {
    let tempCode = code // Bigint
    new Array(...keyBlocks).reverse().forEach(e => {
        const inf = parseInt(127n & tempCode)
        tempCode >>= 7n // 每7位是一个图块信息
        const x = (112 & inf) >> 4
        const y = (14 & inf) >> 1
        const direction = 1 & inf
        targetPlate.putBlock(e, x, y, direction)
    })
    targetPlate.putBlocks(otherBlocks)
}

const getEncodeHexString = (plate, keyBlocks, minLen) => {
    const str = getEncode(plate, keyBlocks).toString(16)
    return str.length < minLen ? ('00000000000000' + str).slice(-minLen) : str

}
endoceBlocks = [block_H, block_G, block_E, block_D, block_C, block_A, block_3, block_2] // 方形拼图块不用于编码(3x3 2x2 1x1)
plate.draw()
code = getEncode(plate, endoceBlocks)
console.log('BIG', code.toString(16))

//输出到文件
const singleNumberCodeSize = 30
fs.writeFile('./data.txt', '', () => { })// 清空
const codeStr = duplicateRemoved.map(a => new Plate(width = 8, height = 8).changeTo(a)).reduce((p, c, i) => p + getEncodeHexString(c, endoceBlocks, 14) + (i % singleNumberCodeSize == singleNumberCodeSize - 1 ? '|' : ''), '')
// codeStr.split('|').forEach(s => console.log('0x' +s))
// codeStr.split('|').forEach((s, i) => fs.writeFile('./data.txt', '0x' + s + ',\r\n', { 'flag': 'a' }, err => console.log(i + '/' + duplicateRemoved.length / singleNumberCodeSize, err)))
codeStr.split('|').forEach((s, i) => fs.writeFile('./data.txt', '0x' + s + ',\r\n', { 'flag': 'a' }, err => {}))

const decode = (index, codeBignit) => {
    const codeByteLength = 7 //单个解占的字节数
    const moveStepCount = BigInt(index * codeByteLength * 8)
    decodeBlocks = [block_H, block_G, block_E, block_D, block_C, block_A, block_3, block_2]
    const opr = BigInt('0x' + 'ff'.repeat(codeByteLength)) << moveStepCount
    const code = (opr & codeBignit) >> moveStepCount
    const newPlate = new Plate(width = 8, height = 8)
    decodeToPlate(newPlate, code, decodeBlocks, [block_F, block_B, block_1])
    return newPlate
}

codeNum = BigInt('0x' + codeStr.split('|')[0])
console.log('解码 1:')
console.log(codeNum.toString(16))
decode(3, codeNum).draw()
console.log('解码 2:')
decode(24, BigInt('0x16d4951720bd1197005e0603c191a01982a728bd11b02cbe01e0ab9150c44666b61b91160e697e504886a81a6d106455852e0e6d10c46a9c0e37423ac46367a8c66aa0d10d024b98402228ed61a8b4402228d5fc96086e422a512bac194602322fd2179a4602226907921b028233e92f28b609105e25f4642c8601e09899b0948b81fc011417108eae00b24f36548d10c66c8211408eae05411713120e81e1ef82a8446cd160a27c8a445cb1e0bd5f')).draw()