class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# def print_forward(self):
# def print_backward(self):
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head, None)
        if self.head is not None:
            self.head.prev = node
        self.head = node

    def print_forward(self):
        if self.head is None:
            print("Doubly linked list is empty.")
            return

        itr = self.head
        dllstr = ""
        while itr:
            dllstr += str(itr.data) + "--> "
            itr = itr.next

        print(dllstr)
    
    def print_backward(self):
        if self.head is None:
            print("Doubly linked list is empty.")
            return

        itr = self.head
        dllstr = ""
        while itr:
            dllstr = str(itr.data) + "--> " + dllstr
            itr = itr.next

        print(dllstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None, itr)

    def insert_values(self, data_list):
        self.head = None

        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                node = itr.next.next
                itr.next = node
                node.prev = itr
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)

        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next:
                    itr.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.get_length() == 0:
            raise Exception("Doubly linked list is empty.")
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next, itr)
                itr.next.prev = node
                itr.next = node
                return
            itr = itr.next
        raise Exception("Data not found in Doubly linked list")

    def remove_by_value(self, data):
        if self.get_length() == 0:
            raise Exception("Doubly linked list is empty.")
        itr = self.head

        while itr:
            if itr.data == data:
                if itr.prev is None:
                    self.head = itr.next
                elif itr.next is None:
                    itr.prev.next = itr.next
                else:
                    itr.next.prev = itr.prev
                    itr.prev.next = itr.next

                return
            itr = itr.next

        raise Exception("Data not found in Doubly linked list")


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_begining(2)
    dll.print_forward()
    dll.insert_at_begining(78)
    dll.print_forward()
    dll.insert_at_end(43)
    dll.print_forward()
    dll.insert_values([1, 34, 21, 45, 12])
    dll.print_forward()
    dll.print_backward()
    print(f"length: {dll.get_length()}")
    dll.remove_at(1)
    dll.print_forward()
    dll.insert_at(3, 20)
    dll.print_forward()
    dll.insert_after_value(21, 22)
    dll.print_forward()
    dll.remove_by_value(12)
    dll.print_forward()
    dll.remove_by_value(1)
    dll.print_forward()
    dll.remove_by_value(21)
    dll.print_forward()
    
