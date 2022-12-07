# 智能拼图

- `web/` 网页版智能拼图[源码](./web/)。基于`znpt.js`，界面用React，托管于Gitee Pages，[点此访问](https://djhps.gitee.io/intelligent-puzzle/)。
- `znpt.js` JS版智能拼图基础类以及种子验证、编解码、整理输出等。
- `znpt.py` 对znpt.js的核心内容的Python版翻译
- `lego_random_puzzle_0.1.py` 乐高（SPIKE HUB），随机出题版。在固件直接运行（使用Thonny实现）几分钟才能验证一题。在MINDSTORM APP运行会崩溃。
- `lego_selected_seed_0.2.py` 乐高（SPIKE HUB），优选种子800倍优化版。在MINDSTORM APP运行堆栈耗尽。
- `lego_preseted_puzzle_0.3.py` 乐高（SPIKE HUB），写死千题版。在MINDSTORM APP运行异常。
- `lego_znpt_1.0.py` 乐高（SPIKE HUB），4x4脑补点阵显示版，支持不到70题。
- `lego_countdown.py` 乐高（SPIKE HUB），基于自制计数器的倒计时。
- `lego_znpt_2.0.py` 乐高（SPIKE HUB），写死压缩后的数据版，支持多达1500题。亲测成功。
- `lego_znpt_2.1.py` 乐高（SPIKE HUB），半自动拼搭版（不附乐高搭建图纸）。

自问：为什么没有采用读文件的处理方式？读文件不是既能规避性能问题、又能无限扩展题目数吗？

自答：不是不能实现，但实现方式对大部分乐高编程爱好者不友好。

首先，乐高官方并没有为SPIKE HUB提供读文件API，对于SPIKE玩家或者机器人发明家玩家来说，不能通过正常渠道编程实现对HUB内文件的读写。

但其实SPIKE HUB支持大部分micropython的API，所以其实可以用“黑科技手段”调用到读写文件的API：即查询micropython的文档。

然后，将文件预置入HUB中也是有多种方式，但同样不常规，也是“黑科技”。一是可以执行程序，创建文件并写入，但是这样效率并不高。二是使用非官方工具，直接访问HUB的文件系统，这种方式更接近于操作底层固件。但是乐高HUB的固件有某种保护机制，某些情况下会触发还原（文件系统到出厂设置）。而使用非官方工具是否会对HUB本身造成破坏也是未知的。

所以，这些骚操作我认为是对乐高编程玩家不友好的，因此没有采用这种办法。

能通过官方的常规方式，自己深入优化代码能完成的事情，为啥要另辟蹊径呢？
