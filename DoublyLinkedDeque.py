class DNode:
    def __init__(self, elem, prev = None, next = None):
        self.data = elem
        self.prev = prev
        self.next = next

class DoublyLinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front is None
    
    def isFull(self):
        return False    

    def addFront(self, item):
        node = DNode(item, None, self.front)
        if(self.isEmpty()):
            self.front = self.rear = node
        else:
            self.front.prev = node
            self.front = node

    def addRear(self, item):
        node = DNode(item, self.rear, None)
        if(self.isEmpty()):
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def deleteFront(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            return data
        
    def deleteRear(self):
        if not self.isEmpty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:
                self.front = None
            else:
                self.rear.next = None
            return data 
        
    def size(self):
        count = 0
        node = self.front
        while node:
            count += 1
            node = node.next
        return count

    def __str__(self):
        result = []
        node = self.front
        while node:
            result.append(str(node.data))
            node = node.next
        return '[' + ' <-> '.join(result) + ']'