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

    def insert_first(self, new_element):
        # "Acrescente um novo elemento como título da lista vinculada"
        pass

    def delete_first(self):
        # "Exclua o primeiro elemento (título) na lista vinculada e o retorne"
        pass


class Stack(LinkedList):
    def __init__(self, top=None):
        self.linkedllist = LinkedList(top)

    def push(self, new_element):
        self.insert_first(new_element)

    def pop(self):
        self.delete_first()
