class Pessoa: # Para criar uma classe.
    def __init__(self,nome, idade,comendo=False,falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self,comendo):
        if self.comendo:
            print(f'{self.nome} já está comendo!')
            return 
        print(f'{self.nome} está comendo {comendo}!')
        self.comendo = True
    def pararDeComer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False
    def falar (self, assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return 
        if self.falando:
            print(f'{self.nome} já está falando .')
            return
        print(f'{self.nome} está falando sobre {assunto}!')
    def pararDeFalar(self):
        if not self.falando:
            print(f'{self.nome} não está falando!')
            return
        print(f'{self.nome} parou de falar.')
        self.falando = False
