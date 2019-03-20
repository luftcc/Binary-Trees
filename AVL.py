import time
import random
import math

class AVLNode:
    value = None
    leftChild = None
    rightChild = None
    height = None

    def __init__(self, value):
        self.value = value
        self.height = 1

class AVLTree:
    root = None
    empty = True
    counter = 0

    def __init__(self):
        self.empty = True

    def search(self, k):
        results = [None] * 2
        self.counter = 1
        if self.root is None:
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

    def insert(self, k):
        results = [None] * 2
        self.counter = 1
        node = self.inserting(self.root, k)
        if self.root is None:
            self.root = node
        results[1] = self.counter
        return results

    def inserting(self, node, k):
        self.counter += 1
        if node is None:
            node = AVLNode(k)
        elif k < node.value:
            node.leftChild = self.inserting(node.leftChild, k)
            if self.height(node.leftChild) == self.height(node.rightChild) + 2:
                if k < node.leftChild.value:
                    node = self.ll(node)
                else:
                    node = self.lr(node)
        elif k > node.value:
            node.rightChild = self.inserting(node.rightChild, k)
            if self.height(node.rightChild) == self.height(node.leftChild) + 2:
                if k > node.rightChild.value:
                    node = self.rr(node)
                else:
                    node = self.rl(node)
        node.height = max(self.height(node.leftChild), self.height(node.rightChild)) + 1
        return node

    def height(self, node):
        return node.height if node is not None else 0

    def ll(self, k2):
        self.counter += 1
        k1 = k2.leftChild
        k2.leftChild = k1.rightChild
        k1.rightChild = k2
        k2.height = max(self.height(k2.leftChild), self.height(k2.rightChild)) + 1
        k1.height = max(self.height(k1.leftChild), self.height(k1.rightChild)) + 1
        return k1

    def rr(self, k1):
        self.counter += 1
        k2 = k1.rightChild
        k1.rightChild = k2.leftChild
        k2.leftChild = k1
        k1.height = max(self.height(k1.leftChild), self.height(k1.rightChild)) + 1
        k2.height = max(self.height(k2.leftChild), self.height(k2.rightChild)) + 1
        return k2

    def lr(self, k3):
        self.counter += 1
        k3.leftChild = self.rr(k3.leftChild)
        return self.ll(k3)

    def rl(self, k1):
        self.counter += 1
        k1.rightChild = self.ll(k1.rightChild)
        return self.rr(k1)

    def delete(self, k):
        results = [None] * 2
        self.counter = 1
        return_node = self.search(k)
        if return_node[0] is not None:
            self.deleting(self.root, return_node[0])
        results[1] = self.counter
        return results

    def deleting(self, root, node):
        self.counter += 1
        if root is None or node is None:
            return None
        if node.value < root.value:
            root.leftChild = self.deleting(root.leftChild, node)
            if self.height(root.rightChild) == self.height(root.leftChild) + 2:
                r = root.rightChild
                if self.height(r.leftChild) > self.height(r.rightChild):
                    root = self.rl(root)
                else:
                    root = self.rr(root)
        elif node.value > root.value:
            root.rightChild = self.deleting(root.rightChild, node)
            if self.height(root.leftChild) == self.height(root.rightChild) + 2:
                l = root.leftChild
                if self.height(l.rightChild) > self.height(l.leftChild):
                    root = self.lr(root)
                else:
                    root = self.ll(root)
        else:
            if root.leftChild is not None and root.rightChild is not None:
                if self.height(root.leftChild) > self.height(root.rightChild):
                    maxNode = self.findMax(root.leftChild)
                    root.value = maxNode.value
                    root.leftChild = self.deleting(root.leftChild, maxNode)
                else:
                    minNode = self.findMin(root.rightChild)
                    root.value = minNode.value
                    root.rightChild = self.deleting(root.rightChild, minNode)
            else:
                root = root.leftChild if root.leftChild is not None else root.rightChild
        return root

    def findMax(self, node):
        self.counter += 1
        if node is None:
            return None
        while node.rightChild is not None:
            self.counter += 1
            node = node.rightChild
        return node

    def findMin(self, node):
        self.counter += 1
        if node is None:
            return None
        while node.leftChild is not None:
            node = node.leftChild
            self.counter += 1
        return node

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
    BT = AVLTree()
    for i in test:
        BT.insert(i)
    print("AVL:")
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
    BT = AVLTree()
    for i in test:
        BT.insert(i)
    print("AVL:")
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

    print("AVL:")
    t0 = time.process_time()
    BT = AVLTree()
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

    print("AVL:")
    t0 = time.process_time()
    BT = AVLTree()
    for i in range(num):
        BT.delete(i)
    print("Deletion Running time:", time.process_time() - t0)