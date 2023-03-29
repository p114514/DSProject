import numpy as np
import time

a = np.mat([[0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1],
            [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1],
            [0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
            [0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1],
            [1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 1],
            [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1],
            [0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1],
            [0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0],
            [0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1],
            [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1],
            [1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
            [0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0],
            [0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0]])
#b=1-a


def gs(i, j):
    return abs(i - startx) + abs(j - starty)
def h1(i, j):
    return 10*(abs(i - endx) + abs(j - endy))
def h2(i, j):
    return pow(i - endx, 2) + pow(j - endy, 2)

startx, starty, endx, endy=map(int, input().split())

for l in range(len(a)):
    for m in range(a[0].size):
        print(a[l, m], end=' ')
    print('')
print('')

#for l in range(len(b)):
    #for m in range(b[0].size):
        #print(b[l, m], end=' ')
    #print('')
#print('')

if a[startx - 1, starty - 1] == 1:
    print("起点%s为墙，寻找失败！" % ([startx, starty]))
else:
    Close = [[startx, starty]]
    Opens = [[startx, starty]]
    crossings = []
    road = 100
    start = time.time()
    rows, cols = a.shape
    while True:
        if Close[-1] != [endx, endy]:
            Open = []
            i, j = Close[-1][0] - 1, Close[-1][1] - 1
            for ni, nj in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i + 1, j + 1), (i + 1, j - 1), (i - 1, j + 1), (i - 1, j - 1)]:
                if [ni + 1, nj + 1] not in Opens and 0 <= ni < rows and 0 <= nj < cols and a[ni, nj] == 0:
                    Open.append([ni + 1, nj + 1])
            a[i, j] = road
            road = road + 1
            if Open:
                Open = sorted(Open, key=lambda x: gs(x[0], x[1]) + h2(x[0], x[1]), reverse=True)
                Opens.extend(Open)
                Close.append(Open.pop())
                if Open:
                    crossings.extend(Open)
            elif crossings:
                next_way = crossings.pop()
                road -= 1
                Close.pop()
                Close.append(next_way)
            else:
                print("寻找失败，失败位置为：%s，路径为：" % Close[-1])
                break
        else:
            a[endx - 1, endy - 1] = road
            print("最短路径寻找成功，路径为：")
            break
    for r in range(rows):
        for c in range(cols):
            print("{0: >4}".format(a[r, c]), end='')
        print('')
    end = time.time()
    #print("\n扩展节点数为：%d, 生成节点数为：%d, 用时为 %.8f" % (len(Opens), len(Close), float(end - start)))
    #print('Close表为：%s' % Close)
    print("点的移动轨迹为：")
    for k in range(len(Close)):
        print(Close[k], end='')  ##决定下一步怎么走的话就把坐标变成下一个Close
        if k < len(Close) - 1:
            print("-->", end='')
