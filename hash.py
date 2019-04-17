#Escreva uma classe HashTable que armazene strings em uma tabela de hash,
# na qual as chaves sejam calculadas utilizando as duas primeiras letras
# da string.


class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Submeta uma string que esteja armazenada na tabela."""
        pass

    def lookup(self, string):
        """Retorne o valor hash caso a string já esteja na tabela.
        Caso contrário, retorne -1."""
        return -1

    def calculate_hash_value(self, string):
        hash_value = (ord(string[0])*100) + ord(string[1])
        return hash_value