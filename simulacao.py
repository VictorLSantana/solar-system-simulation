
import turtle

from sistema_solar import SistemaSolar, Sol, Planeta

LARGURA_TELA = 1000
ALTURA_TELA = 700

MASSA_SOL = 10_000_000
TAMANHO_SOL = 100

MASSA_PLANETA = MASSA_SOL/10**6
TAMANHO_PLANETA = TAMANHO_SOL/10

sistema_solar = SistemaSolar(largura=LARGURA_TELA, altura=ALTURA_TELA)

sol = Sol(sistema_solar=sistema_solar, massa=MASSA_SOL, tamanho=TAMANHO_SOL)

planeta = Planeta(
    sistema_solar=sistema_solar,
    massa=MASSA_PLANETA,
    tamanho=TAMANHO_PLANETA,
    posicao=(-350, 0),
    velocidade=(0.01, 0.01)
    )

while True:
    sistema_solar.atualiza_posicao()
