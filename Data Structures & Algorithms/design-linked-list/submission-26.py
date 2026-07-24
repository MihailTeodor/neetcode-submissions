class ListNode:

    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)    
        self.tail = ListNode(0)   
        self.head.next = self.tail
        self.tail.prev = self.head 

    def get(self, index: int) -> int:
        cur = self.head.next

        if cur == self.tail:
            return -1

        for _ in range(index):
            cur = cur.next
            if cur == self.tail:
                return -1
            
        return cur.val
        

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)        

    def addAtTail(self, val: int) -> None:
        cur = self.tail

        newNode = ListNode(val)

        newNode.prev = cur.prev
        newNode.next = cur
        cur.prev.next = newNode
        cur.prev = newNode



    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head

        while index > 0:
            if cur.next == self.tail and index > 0:
                return
            cur = cur.next
            index -= 1

        newNode = ListNode(val)

        newNode.prev = cur
        newNode.next = cur.next
        cur.next.prev = newNode
        cur.next = newNode
        

    def deleteAtIndex(self, index: int) -> None:

        cur = self.head

        while index > 0:
            if cur.next == self.tail:
                return

            cur = cur.next
            index -= 1

        node_to_delete = cur.next

        if node_to_delete == self.tail:
            return

        cur.next = node_to_delete.next
        node_to_delete.next.prev = cur
    
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)