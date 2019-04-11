class Element:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
            current_element = self.head
            if self.head:
                while current_element.next:
                    current_element = current_element.next
                current_element.next = new_element
            else:
                self.head = new_element

    def get_position(self, position):
        current_element = self.head
        try:
            for _ in range(1,position):
                current_element = current_element.next
            return current_element
        except:
            return None

    def insert(self, new_element, position):
        replaced_item = self.get_position(position)
        new_element.next = replaced_item.next
        last_item = self.get_position(position-1)
        last_item.next = new_element


def delete(self, value):
    """Exclua o primeiro node que contenha um valor determinado."""
    pass
    