
import turtle

from sistema_solar import SistemaSolar, Sol


MASSA_SOL = 10_000_000
TAMANHO_SOL = 100
LARGURA_TELA = 1000
ALTURA_TELA = 700


sistema_solar = SistemaSolar(largura=LARGURA_TELA, altura=ALTURA_TELA)

sol = Sol(sistema_solar=sistema_solar, massa=MASSA_SOL, tamanho=TAMANHO_SOL, velocidade=(0.1,0.1))

while True:
    sistema_solar.atualiza_posicao()
