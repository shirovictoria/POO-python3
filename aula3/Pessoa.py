from random import randint 
class Pessoa:
    ano_atual = 2019

    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
        

    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)
    @classmethod
    def por_ano_de_nascimento(classe,nome,ano_de_nascimento):
        idade = classe.ano_atual - ano_de_nascimento
        return classe(nome, idade)
    @staticmethod
    def gerar_id():
        rand = randint(1000, 19999)
        return rand