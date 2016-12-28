def lin_conf():
    b = 15
    def line(x):
        return 2*x+b
    return line
b = 5
my_line = lin_conf()
print(my_line.__closure__)
print(my_line.__closure__[0].cell_contents)

def line_conf(a,b):
    def line(x):
        return a*x+b
    return line

line1 = line_conf(1,2)
line2 = line_conf(4,5)
print(line1(5),line2(3))

class MaxHeap(object):
    def __init__(self):
        self.heap = []
        self.length = 0

    def add(self, elem):
        #interface add new data
        if not self.heap:
            self.heap.append(elem)
            self.length += 1
        else:
            self.heap.append(elem)
            self.length += 1
            position = self.length - 1
            self._adjust(elem, position)

    def _adjust(self, elem, position):
        #adjust heap when add new data
        parent = (position - 1) // 2
        if position == 0:
            return

        elif elem > self.heap[parent]:
            self.heap[position], self.heap[parent]  = self.heap[parent], self.heap[position]
            self._adjust(elem, parent)
        else:
            return

    def pop(self):
        self.length -= 1
        #pop the max data
        return self.heap.pop(0)


class MinHeap(object):
    def __init__(self):
        self.heap = []
        self.length = 0

    def add(self, elem):

        if not self.heap:
            self.heap.append(elem)
            self.length += 1
        else:
            self.heap.append(elem)
            self.length += 1
            position = self.length - 1
            self._adjust(elem, position)

    def _adjust(self, elem, position):
        # adjust heap when add new data
        parent = (position - 1) // 2
        if position == 0:
            return

        elif elem < self.heap[parent]:
            self.heap[position], self.heap[parent] = self.heap[parent], self.heap[position]
            self._adjust(elem, parent)
        else:
            return

    def pop(self):
        self.length -= 1
        # pop the min data
        return self.heap.pop(0)


def finder(mlist):
    #维护中位数
    maxHeap = MaxHeap()
    minHeap = MinHeap()
    #保存中位数
    middle = mlist[0]
    target_length = len(mlist)
    odd = 1
    if not target_length & 1:
        odd = 0

    for x in mlist[1:]:
        #判断大小两个堆维护的数的差

        if x > middle:
            minHeap.add(x)
        elif x <= middle:
            maxHeap.add(x)
        #如果差大于1，则需要调整
        if maxHeap.length - minHeap.length > 1:
            #如果大顶堆存放数量大于小顶堆存放数量
            minHeap.add(middle)
            #获得大顶堆中最大的数
            middle = maxHeap.pop()

        if minHeap.length - maxHeap.length > 1:
            maxHeap.add(middle)
            middle = minHeap.pop()

    if odd:
        print(maxHeap.heap)
        print(minHeap.heap)
        return middle

    elif maxHeap.length < minHeap.length:
        return middle, minHeap.pop()

    elif maxHeap.length > minHeap.length:
        return middle, maxHeap.pop()


if __name__ == "__main__":
    import random
    mlist = []
    for i in range(100001):
        data = random.randint(1,9999)
        mlist.append(data)
#    print(mlist)

    print(finder(mlist))

matrix = [[1,2,3], [4,5,6], [7,8,9]]
def display(matrix):
    return matrix.pop(0), display(list(zip(*matrix))[::-1]) if matrix else []

print(display(matrix))

#
class Stack(object):
    def __init__(self):
        self.data = []
        self.max = []

    def push(self, elem):
        self.data.append(elem)
        if not self.max:
            self.max.append(elem)
        elif self.max[-1] < elem:
            self.max.append(elem)
        else:
            self.max.append(self.max[-1])

    def pop(self):
        #123212
        #123333
        self.data.pop()
        self.max.pop()

    def get_max(self):
        return self.max[-1]

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(2)
stack.push(1)
stack.push(2)
stack.pop()
stack.pop()
stack.pop()

print(stack.get_max())

import random
from collections import namedtuple

def get(times):
    result = {}
    result["notIn"] = 0
    result["In"] = 0
    for i in range(times):
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        # Point = namedtuple('Point', ["x", "y"])
        # p = Point(x, y)

        if pow(x, 2) + pow(y, 2) > 10000:
            result["notIn"] += 1
        else:
            result["In"] += 1

    data = 4 * result['In'] / times
    return data

print(get(100000))
#namedtupe是一个函数，创建tuple对象，消耗性能，在量大大时候不要使用





