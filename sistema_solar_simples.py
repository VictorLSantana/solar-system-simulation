
import turtle

from sistema_solar import SistemaSolar, Sol


MASSA_SOL = 10_000_000
TAMANHO_SOL = 100
LARGURA_TELA = 800
ALTURA_TELA = 550


sistema_solar = SistemaSolar(largura=LARGURA_TELA, altura=ALTURA_TELA)

sol = Sol(sistema_solar=sistema_solar, massa=MASSA_SOL, tamanho=TAMANHO_SOL)

sol.draw()
turtle.done()

