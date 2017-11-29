# -*- coding:utf-8 -*-
# Filename: perceptron primer

import copy
from matplotlib import pyplot as plt
from matplotlib import animation

training_set = [[(3, 3), 1], [(4, 3), 1], [(2, 2), 1], [(0, 4), 1],
                [(1, 1), -1], [(0, 0), -1], [(-1, 2), -1]]
w = [0, 0]
b = 0
history = []


def cal_distance(item):
    # 判断 y_i(w*x_i+b) <= 0
    # y_i = item[1]
    # x_i = item[0]
    res = 0
    for i in range(len(item[0])):
        res += item[0][i] * w[i]

    res += b
    res *= item[1]
    return res


def update_para(item):
    # 更新参数
    global w, b, history
    w[0] += 1 * item[1] * item[0][0]
    w[1] += 1 * item[1] * item[0][1]
    b += 1 * item[1]
    print('w=', w, 'b=', b)
    history.append([copy.copy(w), b])
    return


def check_conver(iteration):
    # 检查是否收敛
    flag = False
    for item in training_set:
        if cal_distance(item) <= 0:
            flag = True
            print(iteration, "th iteration:")
            update_para(item)
    if not flag:
        print('Result: w=', w, 'b=', b)
    return flag


if __name__ == '__main__':
    for i in range(100):
        if not check_conver(i): break
    fig = plt.figure()
    ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
    line, = ax.plot([], [], 'g', lw=2)
    label = ax.text([], [], '')


    def init():
        # 初始化背景、画出样本点
        line.set_data([], [])
        x, y, x_, y_ = [], [], [], []
        for p in training_set:
            if p[1] > 0:
                x.append(p[0][0])
                y.append(p[0][1])
            else:
                x_.append(p[0][0])
                y_.append(p[0][1])
        plt.plot(x, y, 'bo', x_, y_, 'r+')
        plt.axis([-6, 6, -6, 6])
        plt.grid(True)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Perceptron Algorithm')
        return line, label


    def animate(i):
        # 对于每一帧，更新分割线位置，画出分割线
        w = history[i][0]
        b = history[i][1]
        if w[1] == 0:
            x1 = x2 = -b / w[0]
            y1 = 7
            y2 = -7
            print([x1, y1], [x2, y2])
            line.set_data([x1, x2], [y1, y2])
            return line, label
        x1 = -7
        y1 = -(b + w[0] * x1) / w[1]
        x2 = 7
        y2 = -(b + w[0] * x2) / w[1]
        line.set_data([x1, x2], [y1, y2])
        return line, label


    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=len(history), interval=500,
                                   repeat=False, blit=True)
    print(history)
    plt.show()
