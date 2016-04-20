class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            tmp = self.head
            while tmp.next != None:
                tmp = tmp.next
            tmp.next = Node(data)

    def toString(self):
        tmp = self.head
        res = ""
        while tmp != None:
            res += " " +  str(tmp.data)
            tmp = tmp.next
        return res

    def reverse(self):
        self.head = self.reverseHelper(self.head)

    def reverseHelper(self, head):
        if head == None or head.next == None:
            return head

        next = head.next
        reversed_list = self.reverseHelper(head.next)
        next.next = head
        head.next = None

        return reversed_list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


list = LinkedList()
list.add(5)
list.add(6)
list.add(7)

print(list.toString())
list.reverse()
print(list.toString())