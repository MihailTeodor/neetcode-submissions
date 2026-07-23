class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:

        if index < 0 or index >= self.size:
            return -1

        dummy = self.head
        while index > 0:
            dummy = dummy.next
            index -= 1

        return dummy.val


    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)

        if not self.head:
            self.head = newNode
            self.size += 1
            return

        dummy = self.head

        while dummy.next:
            dummy = dummy.next

        dummy.next = newNode
        self.size += 1

        

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)

        if index == 0:
            newNode.next = self.head.next
            self.head = newNode
            self.size += 1
            return

        dummy = self.head
        if index == self.size:
            while dummy.next:
                dummy = dummy.next
            
            dummy.next = newNode
            self.size += 1
            return


        if index < 0 or index > self.size:
            return

        index -= 1

        while index > 0:
            dummy = dummy.next
            index -= 1

        newNode.next = dummy.next
        dummy.next = newNode
        self.size += 1

        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        dummy = self.head
        index -= 1
        
        while index > 0:
            dummy = dummy.next
            index -= 1

        dummy.next = dummy.next.next
        self.size -= 1

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)