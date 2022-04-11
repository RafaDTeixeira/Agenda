class Contato:

    def __init__(self, nome, celular):
        self.nome = nome
        self.celular = celular

    def __str__(self):
        return f'{self.nome} - Celular: {self.celular}'