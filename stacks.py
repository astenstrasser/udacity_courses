class Element:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        current_element = self.head
        try:
            for _ in range(1, position):
                current_element = current_element.next
            return current_element
        except:
            return None

    def insert_first(self, new_element):
        current = self.head
        self.head = new_element
        new_element.next = current

    def delete_first(self):
        poped_item = self.head
        self.head = self.head.next
        return poped_item


class Stack(LinkedList):
    def __init__(self, top=None):
        self.linkedlist = LinkedList(top)

    def push(self, new_element):
        self.linkedlist.insert_first(new_element)

    def pop(self):
        self.linkedlist.delete_first()
