class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self): return self.head == None
    def isFull(self): return False

    def getNode(self, pos):
        if pos < 0 : return None
        node = self.head;
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node
    
    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None : return None
        else : return node.data

    def insert(self, pos, elem):
        before = self.getNode(pos-1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            node = Node(elem, before.link)
            before.link = node
        
    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link

    @property
    def size(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.link
        return count

    def __str__(self):
        result = []
        node = self.head
        while node:
            result.append(str(node.data))
            node = node.link
        return '[' + ' -> '.join(result) + ']'
