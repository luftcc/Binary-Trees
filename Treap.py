import time
import random
import math



class TNode:
    value = None
    priority = None
    leftChild = None
    rightChild = None
    parent = None

    def __init__(self, value, priority, parent):
        self.value = value
        self.priority = priority
        self.parent = parent
class Treap:
    root = None
    empty = True
    counter = 0

    def __init__(self):
        self.empty = True

    def search(self, k):
        results = [None] * 2
        self.counter = 1
        if self.empty:
            results[1] = self.counter
            return results

        node = self.root
        while node is not None:
            self.counter += 1
            if k < node.value:
                node = node.leftChild
            elif k > node.value:
                node = node.rightChild
            else:
                results[0] = node
                break
        results[1] = self.counter
        return results

    def rotate_right(self, parent):
        self.counter += 1
        pp = parent.parent
        if pp is not None:
            lor = parent is not pp.leftChild

        v = parent.leftChild
        parent.leftChild = v.rightChild
        v.rightChild = parent

        if pp is not None:
            v.parent = pp
            if lor:
                pp.rightChild = v
            else:
                pp.leftChild = v
        else:
            self.root = v
            v.parent = None
        parent.parent = v
        if parent.leftChild is not None:
            parent.leftChild.parent = parent

    def rotate_left(self, parent):
        self.counter += 1
        pp = parent.parent
        if pp is not None:
            lor = parent is not pp.leftChild

        v = parent.rightChild
        parent.rightChild = v.leftChild
        v.leftChild = parent

        if pp is not None:
            v.parent = pp
            if lor:
                pp.rightChild = v
            else:
                pp.leftChild = v
        else:
            self.root = v
            v.parent = None
        parent.parent = v
        if parent.rightChild is not None:
            parent.rightChild.parent = parent

    def insert(self, k):
        results = [None] * 2
        self.counter = 1
        new_node = TNode(k, random.random(), None)
        if self.empty:
            self.empty = False
            self.root = new_node
        else:
            node = self.root
            parent = None
            lor = 0
            h1 = True
            while node is not None:
                self.counter += 1
                if k < node.value:
                    parent = node
                    lor = 0
                    node = node.leftChild
                elif k > node.value:
                    parent = node
                    lor = 1
                    node = node.rightChild
                else:
                    h1 = False
                    break
            if h1:
                if lor == 0:
                    parent.leftChild = new_node
                else:
                    parent.rightChild = new_node
                new_node.parent = parent

                v = new_node
                r = 0
                while v.parent is not self.root and v.priority > v.parent.priority:
                    r += 1
                    if v is v.parent.leftChild:
                        self.rotate_right(v.parent)
                    elif v is v.parent.rightChild:
                        self.rotate_left(v.parent)
        results[1] = self.counter
        return results

    def delete(self, k):
        results = [None] * 2
        self.counter = 1
        return_node = self.search(k)
        v = return_node[0]
        if v is not None:
            while v.leftChild is not None or v.rightChild is not None:
                if v.leftChild is None:
                    self.rotate_left(v)
                elif v.rightChild is None or v.leftChild.priority > v.rightChild.priority:
                    self.rotate_right(v)
                else:
                    self.rotate_left(v)
            self.true_delete(v)
        results[1] = self.counter
        return results

    def true_delete(self, node):
        self.counter += 1
        if node is not None and node.parent is not None:
            if node is node.parent.leftChild:
                node.parent.leftChild = None
            else:
                node.parent.rightChild = None
#random element
nums = [1000, 2500, 5000, 10000, 20000]
tests = []
for i, num in enumerate(nums):
    tests.append([])
    for j in range(num):
        tests[i].append(math.floor(random.uniform(0, 0xFFFFFFFF)))

for j, test in enumerate(tests):
    print("Number of elements inserted(containing duplicate): ", nums[j])

    t0 = time.process_time()
    BT = Treap()
    for i in test:
        BT.insert(i)
    print("Treap:")
    print("Running time:", time.process_time() - t0)


#sequential
nums = [1000, 2500, 5000, 10000, 20000]
tests = []
for i, num in enumerate(nums):
    tests.append([])
    for j in range(num):
        tests[i].append(j)

for j, test in enumerate(tests):
    print("Number of elements inserted(containing duplicate): ", nums[j])
    t0 = time.process_time()
    BT = Treap()
    for i in test:
        BT.insert(i)
    print("Treap:")
    print("Sequential Running time:", time.process_time() - t0)


#search
nums = [1000, 2500, 5000, 10000, 20000]
tests = []
for i, num in enumerate(nums):
    tests.append([])
    for j in range(num):
        tests[i].append(math.floor(random.uniform(0, 0xFFFFFFFF)))
for j, num in enumerate(nums):
    print("# of searching keys:", num)

    print("Treap:")
    t0 = time.process_time()
    for i in range(num):
        BT.search(test[i])
    print("Running time:", time.process_time() - t0)


#deletion
nums = [1000, 2500, 5000, 10000, 20000]
tests = []
for i, num in enumerate(nums):
    tests.append([])
    for j in range(num):
        tests[i].append(math.floor(random.uniform(0, 0xFFFFFFFF)))

    print("Treap:")
    t0 = time.process_time()
    for i in range(num):
        BT.delete(i)
    print("Deletion Running time:", time.process_time() - t0)