import re

class Telefones_br:

    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número incorreto!")

    def __str__(self):
        return self.format_numero()

    def valida_telefone(self, telefone):
        padrao = "(\d{2,3})?(\d{2})(\d{4,5})(\d{4})"
        resposta = re.findall(padrao, telefone)
        if resposta:
            return True
        else:
            return False

    def format_numero(self):
        padrao = "(\d{2})?(\d{2})(\d{4,5})(\d{4})"
        resposta = re.search(padrao, self.numero)
        return f"{resposta.group(1)} ({resposta.group(2)}){resposta.group(3)}-{resposta.group(4)}"
