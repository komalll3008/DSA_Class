def solution():
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        def append(self, data):
            new_node = Node(data)
            if self.head is None:
                self.head = new_node
                return

            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

        def display(self):
            temp = self.head
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
            print()

        def insert(self, position, data):
            new_node = Node(data)

            if position == 0:
                new_node.next = self.head
                self.head = new_node
                return

            temp = self.head
            for _ in range(position - 1):
                if temp is None:
                    return
                temp = temp.next

            if temp is None:
                return

            new_node.next = temp.next
            temp.next = new_node

        def middle(self):
            slow = self.head
            fast = self.head

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next

            if slow:
                print(slow.data)

        def delete(self, data):
            temp = self.head

            if temp and temp.data == data:
                self.head = temp.next
                return

            while temp and temp.next:
                if temp.next.data == data:
                    temp.next = temp.next.next
                    return
                temp = temp.next

        def reverse(self):
            prev = None
            curr = self.head

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            self.head = prev

        def consecutive_sums(self):
            temp = self.head
            while temp and temp.next:
                print(temp.data + temp.next.data, end=" ")
                temp = temp.next
            print()

    ll = LinkedList()

    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n):
        ll.append(arr[i])

    ll.display()
    ll.insert(1, 99)
    ll.display()
    ll.middle()
    ll.delete(99)
    ll.display()
    ll.reverse()
    ll.display()
    ll.consecutive_sums()


solution()
