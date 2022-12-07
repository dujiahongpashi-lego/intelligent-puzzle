import React from 'react';
import './App.css';
import exchange from './exchange.svg';

const color_map = {
  '1': 'blue',
  '2': 'blue',
  '3': 'blue',
  'A': 'red',
  'B': 'yellow',
  'C': 'white',
  'D': 'red',
  'E': 'red',
  'F': 'yellow',
  'G': 'white',
  'H': 'white'
}

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
    this.plateArray = []
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

  putBlock(block, x = 0, y = 0, direction = 0) {
    //position start from (0, 0) (x, y)
    // 目前仅支持规则矩形
    //direction 0 for 正常角度
    //direction 1 for 转90度放入该位置
    const h = direction === 0 ? block.h : block.w
    const w = direction === 0 ? block.w : block.h
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

  erasureBlock(block, x = 0, y = 0, direction = 0) {
    // 擦除具体Block
    const h = direction === 0 ? block.h : block.w
    const w = direction === 0 ? block.w : block.h
    this._updateSubBlock(x, y, w, h, 0)
  }

  erasurePlace(x = 0, y = 0, width, height) {
    // 擦除指定区域
    for (let i = 0; i < height; i++) {
      for (let j = 0; j < width; j++) {
        this.plateArray[y + i][x + j] = 0
      }
    }
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

  erasureAreas(n) {
    // 擦除指定内容
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        if (this.plateArray[i][j] === n) {
          this.plateArray[i][j] = 0
        }
      }
    }
  }

  have(name) {
    // 发现指定内容
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        if (this.plateArray[i][j] === name) {
          return true
        }
      }
    }
    return false
  }

  find(name) {
    // 查找指定内容，返回坐标
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        if (this.plateArray[i][j] === name) {
          return [j, i, name]
        }
      }
    }
    return [-1, -1, name]
  }

  _isEmptySubBlock(x = 0, y = 0, width, height) {
    const subBlock = [] // 中转变量，可以不要
    let valueChecker = 0
    for (let i = 0; i < height; i++) {
      subBlock[i] = new Array(width)
      for (let j = 0; j < width; j++) {
        const currentPotValue = this.plateArray[y + i][x + j]
        subBlock[i][j] = currentPotValue
        if (currentPotValue !== 0) {
          valueChecker = currentPotValue
        }
      }
    }

    return valueChecker === 0
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

  randomInitAs123() {
    // 随机出题
    this._init()
    const block1 = new Block(1, 1, '1')
    const block2 = new Block(1, 2, '2')
    const block3 = new Block(1, 3, '3')
    this._putRandom(block1)
    this._putRandom(block2)
    this._putRandom(block3)
  }
  
  // 以种子包生成随机种子
  randomInit(seed) {
    this._init()
    seed.forEach(e => this._putRandom(e))
  }

  // 随机出题--种子HGF1
  randomInitAsHFA() {
    this.randomInit([new Block(3, 3, 'F'), new Block(1, 4, 'A'), new Block(3, 4, 'H')])
  }

  putBlocks(blocks) {
    // 深度优先递归
    const b = blocks[0]
    const directions = b.w === b.h ? [0] : [0, 1]
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        for (let dir in directions) {
          // 尝试在ji位置放置一块
          if (this.putBlock(b, j, i, dir)) {
            const currenBlockCount = blocks.length
            if (currenBlockCount === 1) {
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


class App extends React.Component {
  constructor(props) {
    super(props);

    const block_H = new Block(3, 4, 'H')// 白 12
    const block_G = new Block(2, 5, 'G')// 白 10
    const block_F = new Block(3, 3, 'F')// 黄 9
    const block_E = new Block(2, 4, 'E')// 红 8
    const block_D = new Block(2, 3, 'D')// 红 6
    const block_C = new Block(1, 5, 'C')// 白 5
    const block_B = new Block(2, 2, 'B')// 白 4
    const block_A = new Block(1, 4, 'A')// 红 4
    const block1 = new Block(1, 1, '1')
    const block2 = new Block(1, 2, '2')
    const block3 = new Block(1, 3, '3')
    const blocks = [block_H, block_G, block_F, block_E, block_D, block_C, block_B, block_A]
    const restBlocks = [block_G, block_E, block_D, block_C, block_B, block3, block2, block1]
    const plate = new Plate(8, 8)
    this.plate = plate
    this.blocks = blocks
    this.restBlocks = restBlocks
    this.leftblocks = blocks.slice(0, 4)
    this.rightblocks = blocks.slice(4, 8)
    this.state = {}
  }

  componentDidMount() {
    this.newPuzzle()
  }

  newPuzzle() {
    this.setState({ ...this.state, haveTip: false, puzzleDone: false })
    const that = this
    setTimeout(() => {
      // 随机出题/解密模式
      console.log('开始随机出题并解密...')
      let counter = 1
      const start = new Date().getTime()
      const puzzlePlate = new Plate(8, 8)
      puzzlePlate.randomInitAsHFA()
      while (!puzzlePlate.putBlocks(that.restBlocks)) {
        counter++
        puzzlePlate.randomInitAsHFA()
      }
      const end = new Date().getTime()
      console.log('随机出题尝试共', counter, '次，总用时', end - start, 'ms')

      that.plate.erasurePlace(0, 0, 8, 8)
      that.plate.update([1, 2, 3, '1', '2', '3'], puzzlePlate)
      that.puzzlePlate = puzzlePlate
      that.setState({ ...that.state, puzzleDone: true })
    }, 10)
  }

  tip(names) {
    if (!this.state.haveTip) {
      this.plate.erasurePlace(0, 0, 8, 8)
      this.plate.update([1, 2, 3, '1', '2', '3'], this.puzzlePlate)
      this.plate.update(names, this.puzzlePlate)
      this.setState({ ...this.state, haveTip: true })
    }
    else {
      names.forEach(n => this.plate.erasureAreas(n))
      this.setState({ ...this.state, haveTip: false })
    }
  }


  drawBlock(w, h, name, dir = 0) {
    const plate = new Plate(w, h)
    const block = new Block(w, h, name)
    plate.putBlock(block, 0, 0, dir)
    return plate.plateArray.map(line => <div className={this.plate.have(name) ? 'SmallLine Used' : 'SmallLine NotUsed'}>
      {line.map(p =>
        <div className='SmallArea' style={{ backgroundColor: color_map[p] }} />
      )}
    </div>)
  }

  clickArea(p, x, y) {
    if (p === 0) {
      if (!this.state.currentSelect) {
        return
      }
      if (this.plate.putBlock(this.state.currentSelect, x, y, 0)) {
        this.setState({ ...this.state, currentSelect: undefined })
        return
      }
    }
    else if ([1, 2, 3, '1', '2', '3'].includes(p)) {
      return
    }
    else {
      this.plate.erasureAreas(p)
    }
    this.setState(this.state)
  }

  selectOneBlock(b) {
    this.setState({ ...this.state, currentSelect: b })
  }

  turn90_L(b, i) {
    this.leftblocks[i] = new Block(b.h, b.w, b.name)
    this.selectOneBlock(this.leftblocks[i])
  }
  turn90_R(b, i) {
    this.rightblocks[i] = new Block(b.h, b.w, b.name)
    this.selectOneBlock(this.rightblocks[i])
  }

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <div className="Main">
            {this.state.puzzleDone ? <div><button className='Button MainButton' onClick={() => this.newPuzzle()} >随机出题</button>
              {this.state.haveTip ? '答案只能看一次' : <button className='Button' onClick={() => this.tip(['A'])} >一点提示</button>}
              {this.state.haveTip ? '' : <button className='Button' onClick={() => this.tip(['H', 'G', 'F'])}  >很多提示</button>}
              {this.state.haveTip ? '' : <button className='Button' onClick={() => this.tip(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])} >使用魔法</button>}
            </div> : <div>出题中...</div>}
            <div className="Plate">
              {
                this.plate.plateArray.map((line, i) => <div className='Line'>
                  {line.map((p, j) =>
                    <div onClick={() => this.clickArea(p, j, i)} className='Area' style={{ backgroundColor: color_map[p] }} />
                  )}
                </div>)
              }
            </div>
            <div className='SelectedBlocks'>
              {
                this.leftblocks.map((b, i) => <div className='OneSelectedBlock '>
                  <div className={this.state.currentSelect && b.name === this.state.currentSelect.name ? 'Selected' : 'NotSelected'} onClick={() => (this.plate.have(b.name) ? 1 == 2 : this.selectOneBlock(b))}>
                    {this.drawBlock(b.w, b.h, b.name, 0)}
                  </div>
                  {this.state.currentSelect && b.name === this.state.currentSelect.name ? <span onClick={() => this.turn90_L(b, i)}><img src={exchange} className="App-logo" alt="logo" /></span> : <span />}
                </div>)
              }
            </div>
            <div className='SelectedBlocks'>
              {
                this.rightblocks.map((b, i) => <div className='OneSelectedBlock '>
                  <div className={this.state.currentSelect && b.name === this.state.currentSelect.name ? 'Selected' : 'NotSelected'} onClick={() => (this.plate.have(b.name) ? 1 == 2 : this.selectOneBlock(b))}>
                    {this.drawBlock(b.w, b.h, b.name, 0)}
                  </div>
                  {this.state.currentSelect && b.name === this.state.currentSelect.name ? <span onClick={() => this.turn90_R(b, i)}><img src={exchange} className="App-logo" alt="logo" /></span> : <span />}
                </div>)
              }
            </div>
          </div>
        </header >
      </div >
    );
  }

}

export default App;
