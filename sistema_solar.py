
import turtle
import itertools

class SistemaSolar:
    def __init__(self, largura, altura):
        self.sistema_solar = turtle.Screen() # criando a tela
        self.sistema_solar.title("Nosso Sistema Solar") # título da tela
        self.sistema_solar.tracer(0) # delay para atualizar o desenho na tela
        self.sistema_solar.setup(largura, altura) # tamanho da tela
        self.sistema_solar.bgcolor("black") # cor de fundo da tela
        
        self.corpos = []
        
    def adicionar_corpo(self, corpo):
        self.corpos.append(corpo)
        
    def remove_corpo(self, corpo):
        self.corpos.remove(corpo) 
        
    def atualiza_posicao(self):
        for corpo in self.corpos:
            corpo.movimento()
            corpo.desenha_na_tela()
            self.sistema_solar.update()

class CorpoCeleste(turtle.Turtle):
    
    def __init__(self, sistema_solar, massa, tamanho, posicao=(0, 0), velocidade=(0, 0)):
        super().__init__()
        self.massa = massa
        self.setposition(posicao)
        self.velocidade = velocidade
        self.tamanho = tamanho
        
        self.penup()
        self.hideturtle()
        
        sistema_solar.adicionar_corpo(self) # adicionando o corpo ao sistema solar
        
    def desenha_na_tela(self):
        self.clear()
        self.dot(self.tamanho)
        

    def movimento(self):
        self.setx(self.xcor() + self.velocidade[0])
        self.sety(self.ycor() + self.velocidade[1])
    
    
    
class Sol(CorpoCeleste):
    def __init__(self, sistema_solar, massa, tamanho, posicao=(0, 0), velocidade=(0, 0)):
        super().__init__(sistema_solar, massa, tamanho, posicao, velocidade)
        self.color("yellow")





class Planeta(CorpoCeleste):
    cores = itertools.cycle(["red", "green", "blue"])
    def __init__(self, sistema_solar, massa, tamanho, posicao=(0, 0), velocidade=(0, 0)):
        super().__init__(sistema_solar, massa, tamanho, posicao, velocidade)
        self.color(next(Planeta.cores))

