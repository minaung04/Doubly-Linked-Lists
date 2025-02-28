class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def DoubleLinkedlistInsert(self, data, index):
        new_node = Node(data)
        if index == 0:  # Insert at head
            if self.head is not None:
                new_node.next = self.head
                self.head.prev = new_node
            self.head = new_node
            return
        
        temp = self.head
        for _ in range(index - 1):
            if temp is None:
                print("Index out of range")
                return
            temp = temp.next
        
        if temp is None:
            print("Index out of range")
            return
        
        new_node.next = temp.next
        if temp.next is not None:
            temp.next.prev = new_node
        temp.next = new_node
        new_node.prev = temp

    def DoubleLinkedlistDelete(self, index):
        if self.head is None:
            print("List is empty")
            return
        
        temp = self.head
        if index == 0:  # Delete head node
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
            return
        
        for _ in range(index):
            temp = temp.next
            if temp is None:
                print("Index out of range")
                return
        
        if temp.next is not None:
            temp.next.prev = temp.prev
        if temp.prev is not None:
            temp.prev.next = temp.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

# Example Usage
dll = DoublyLinkedList()
dll.DoubleLinkedlistInsert(10, 0)
dll.DoubleLinkedlistInsert(20, 1)
dll.DoubleLinkedlistInsert(30, 2)
dll.display()

dll.DoubleLinkedlistDelete(1)
dll.display()
