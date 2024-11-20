class Estudante:
    def __init__(self, nome, curso, media):
        self.nome = nome
        self.curso = curso
        self.media = media

    def Estar_no_quadro_de_honra(self):
        if self.media >= 14:
            return "Sim"
        else:
            return "Não"