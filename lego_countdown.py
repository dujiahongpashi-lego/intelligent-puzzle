import json
from mindstorms import Motor
from mindstorms.control import Timer
from time import sleep_ms
from hub import port

# 【自定义】初始化器件端口
ones_motor = port.B.motor
tens_motor = port.D.motor
Motors = [Motor('B'), Motor('D')]

# 【自定义，微调】校准值
ones_initial = 915# 数越小越靠下
tens_initial = -920# 绝对值越小越靠下

# 【自定义】校准观察时间
CALIBRATE_TIME_MS = 10000

# 【无需蓝牙】秒表玩法(优先级1)
is_stopwatch_mode = False

# 【无需蓝牙】伪时钟玩法，需手动自定义开始时间(优先级2)
is_localclock_mode = False
localclock_init_time = 1138# 11点38分

# 【无需蓝牙】允许伪数据(优先级3)
allow_mock = True

# 预留（数字切换的）运转时间。取决于电机速度和数字更新频率
MOVING_TIME_MS = 200

# 基于平均最短路径的转动方式的数字顺号
digits_position = [0, 3, 7, 11, 1, 6, 8, 2, 9, 10]


def set_digit_one(digit):
    ones_motor.run_to_position(
        digits_position[digit] * 72 + ones_initial)


def set_digit_ten(digit):
    tens_motor.run_to_position(
        digits_position[digit] * -72 + tens_initial)


def motors_return_to_zero():
    # 电机转回0点
    ones_motor.run_to_position(0)
    tens_motor.run_to_position(0)
    sleep_ms(3000)


def reset_motors():
    # 电机重置 位置回正并重设位置0点
    Motors[0].run_to_position(0)
    Motors[1].run_to_position(0)
    print('---check motors---')
    print('-Before-')
    speed, relative_degrees, absolute_degrees, pwm = ones_motor.get()
    print('ones_motor position', relative_degrees, absolute_degrees)
    speed, relative_degrees, absolute_degrees, pwm = tens_motor.get()
    print('tens_motor position', relative_degrees, absolute_degrees)
    ones_motor.preset(0)
    tens_motor.preset(0)
    print('-After-')
    speed, relative_degrees, absolute_degrees_0, pwm = ones_motor.get()
    print('ones_motor position', relative_degrees, absolute_degrees_0)
    speed, relative_degrees, absolute_degrees_00, pwm = tens_motor.get()
    print('tens_motor position', relative_degrees, absolute_degrees_00)
    ones_motor.preset(absolute_degrees_0)
    tens_motor.preset(absolute_degrees_00)


def init_digital_motors():
    # 设备初始化，并进入校准观察（持续时间CALIBRATE_TIME_MS）
    reset_motors()
    sleep_ms(3000)
    set_digit_one(0)
    set_digit_ten(0)
    sleep_ms(CALIBRATE_TIME_MS)


def set_digit(num):
    one = num % 10# 个位
    ten = num//10 % 10# 十位
    hundred = num//100 % 10# 百位
    thousand = num//1000 % 10# 千位
    print(thousand, hundred, ten, one)
    set_digit_one(one)
    set_digit_ten(ten)
    sleep_ms(MOVING_TIME_MS)


timer = Timer()
# 初始化校准
init_digital_motors()

counter = 60
set_digit(counter)

while counter > 0:
    sleep_ms(1000)
    counter = counter -1
    set_digit(counter)

motors_return_to_zero()
