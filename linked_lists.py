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
        try:
            for _ in range(1, position+1):
                current_element = current.next
            return current_element.value
        except:
            return None

def insert(self, new_element, position):
    """Acrescente um novo node na posição determinada.
    Suponha que a primeira posição seja "1".
    Inserir na posição 3 significa estar localizado entre o 2º e 3º elementos."""
    pass


def delete(self, value):
    """Exclua o primeiro node que contenha um valor determinado."""
    pass
    