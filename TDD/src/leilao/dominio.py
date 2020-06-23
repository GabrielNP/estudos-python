import sys


class Usuario:

    def __init__(self, nome):
        self.__nome = nome

    def __str__(self):
        return f'{self.__nome}'

    @property
    def nome(self):
        return self.__nome


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor

    def __str__(self):
        return f'{self.valor}'


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.__lances = []

    @property
    def lances(self):
        return self.__lances[:]

    def propoe(self, lance: Lance):
        self.__lances.append(lance)


class Avaliador:

    def __init__(self):
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max

    def __str__(self):
        return f'Maior lance: {self.maior_lance}; Menor lance: {self.menor_lance}'

    def avalia(self, leilao: Leilao):
        for lance in leilao.lances:
            if lance.valor > self.maior_lance:
                self.maior_lance = lance.valor
            if lance.valor < self.menor_lance:
                self.menor_lance = lance.valor
