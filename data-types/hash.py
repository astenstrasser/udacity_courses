#Escreva uma classe HashTable que armazene strings em uma tabela de hash,
# na qual as chaves sejam calculadas utilizando as duas primeiras letras
# da string.


class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        hash_value = self.calculate_hash_value(string)
        if self.table[hash_value] == None:
            self.table[hash_value] = string
        else:
            self.table[hash_value].append(string)

    def lookup(self, string):
        hash_value = self.calculate_hash_value(string)
        if self.table[hash_value] == None:
            return -1
        else:
            return hash_value

    def calculate_hash_value(self, string):
        hash_value = (ord(string[0])*100) + ord(string[1])
        return hash_value
