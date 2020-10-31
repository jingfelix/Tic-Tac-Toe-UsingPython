# coding : utf-8
# This programe is used for playing a chess game.
# Coder : jingfelix
# updatetime : 2020.10.22
# dct = {11: -1, 12: -1, 13: 0, 22: 0, 21: 0, 23: 0, 31: 0, 32: 0, 33: 0}

# 导入模块用于关闭程序
import sys

# 打印棋盘的函数
def printbd(d):
    print('\\', ' 1  2  3 \n')
    print('1 ', d[11], d[12], d[13], '\n', sep='  ')
    print('2 ', d[21], d[22], d[23], '\n', sep='  ')
    print('3 ', d[31], d[32], d[33], '\n', sep='  ')


# 根据value寻找key的函数,返回一个列表
def get_keys(d, value):
    return [k for (k, v) in d.items() if v == value]


# 胜局/平局测试函数
def fair_test(d, line_all):
    # 通过line的value和判断是否胜出
    # 首先判断是否胜出
    for line_ in line_all:
        # 需要重写一个求和函数，不要怕麻烦
        line_sum = sum(list(line_.values()))  # 求和函数

        if line_sum == 3:
            print('Computer win!')  # 电脑胜出
            init()

        elif line_sum == -3:
            print('Human win!')  # 人类胜出
            init()
    # 平局测试
    zero_count = (list(d.values())).count(0)  # 判断是否还有空余位置
    if zero_count == 0:
        print('Fair game!')  # 平局
        init()


# 核心算法 终于改完了！！！
def main(d):
    global change_key_list  # 在main()函数内的全局变量
    printbd(d)  # 打印棋盘
    human_place = int(input('Choose the place you want to put your chess:'))  # 玩家布置棋子
    d[human_place] = -1

    # 核心数据结构：用字典来存储，方便寻找value对应的key
    line1 = {11: d[11], 21: d[21], 31: d[31]}  # 类型为字典，方便按照棋盘值参数寻找位置参数
    line2 = {12: d[12], 22: d[22], 32: d[32]}
    line3 = {13: d[13], 23: d[23], 33: d[33]}
    line4 = {11: d[11], 12: d[12], 13: d[13]}
    line5 = {21: d[21], 22: d[22], 23: d[23]}
    line6 = {31: d[31], 32: d[32], 33: d[33]}
    line7 = {11: d[11], 22: d[22], 33: d[33]}
    line8 = {13: d[13], 22: d[22], 31: d[31]}

    line_all_1 = [line1, line2, line3, line4, line5, line6, line7, line8]
    # 平局测试；在测试前必须更新棋盘值
    fair_test(d, line_all_1)
    # 设立用于记录需改变的行（类型为字典）
    ergent = []  # 三缺一，必须要封堵的位置
    less_ergent = []  # 三缺二，可选择封堵的位置

    print('Calculating...')  # 分割位置
    print('*' * 40)

    for line in line_all_1:

        line_sum = sum(list(line.values()))  # 求每一行/列的位置算术和

        if line_sum == 2:  # 和为2，即其中有两个为电脑放置的棋子，一个为空
            change_key_list = get_keys(line, 0)
            d[change_key_list[0]] = 1  # 直接选取空的位置放置棋子
            print('Computer win!')
            init()  # 重新开始游戏

        elif line_sum == -2:  # 和为-2，即有两个为玩家放置的棋子，另一个为空
            ergent.append(line)  # 将这一列加入到ergent列表中，方便进行判断
            break

        elif line_sum == -1:  # 两种情况，-2+1或-1+0+0
            change_key_list = get_keys(line, 0)  # 求空位置的个数
            if len(change_key_list) == 2:  # 如果有两个空位置
                less_ergent.append(line)

    if len(ergent) != 0:  # 必须要围堵的列

        change_key_list = get_keys(ergent[0], 0)
        d[change_key_list[0]] = 1

    elif len(less_ergent) != 0:  # 没有必须围堵的列，但是有和为-1，空为2的列
        keys = []  # 考察在less_ergent列表中出现2次及以上的列，这一类列需要优先处理
        times = []  # 用于存储是否有出现次数大于等于2的位置
        for dictn in less_ergent:
            zero_list = get_keys(dictn, 0)
            keys.extend(zero_list)  # extend方法用于在列表后添加一个序列的新元素
        for key in keys:  # 上一步已经将所有less_ergent列中value为0的位置加入keys列表中
            if keys.count(key) >= 2:  # 如果出现两次及以上，优先处理
                d[key] = 1
                times.append(key)
                break
        if times == []:  # 如果没有出现次数大于等于2的位置
            change_key_list = get_keys(less_ergent[0], 0)
            d[change_key_list[0]] = 1

    # change_key_list = get_keys(less_ergent[0], 0)
    # d[change_key_list[0]] = 1

    else:  # 其他情况：必定平局
        print('Fair game!')
        init()

    printbd(d)
    print('*' * 40)
    # 更新棋盘
    line1 = {11: d[11], 21: d[21], 31: d[31]}
    line2 = {12: d[12], 22: d[22], 32: d[32]}
    line3 = {13: d[13], 23: d[23], 33: d[33]}
    line4 = {11: d[11], 12: d[12], 13: d[13]}
    line5 = {21: d[21], 22: d[22], 23: d[23]}
    line6 = {31: d[31], 32: d[32], 33: d[33]}
    line7 = {11: d[11], 22: d[22], 33: d[33]}
    line8 = {13: d[13], 22: d[22], 31: d[31]}
    line_all_1 = [line1, line2, line3, line4, line5, line6, line7, line8]
    fair_test(d, line_all_1)
    main(d)


# 开始：初始化
def init():
    dct = {11: 0, 12: 0, 13: 0, 22: 0, 21: 0, 23: 0, 31: 0, 32: 0, 33: 0}
    print('*' * 40)
    print('Start a new game?')
    start_order = input('Input "yes" to start:')
    if start_order == 'yes':
        fr = input('First hand or not?')  # 玩家先手or后手
        if fr == 'yes':
            main(dct)
        else:
            # 需要选取一个点位下
            dct[22] = 1
            main(dct)
    else:
        print('OK.Goodbye!')
        sys.exit()


init()
