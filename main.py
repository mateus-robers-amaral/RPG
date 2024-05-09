from code import Personagem

print("Bem vindo à aventura!")
start = int(input("[1] Começar novo jogo\n[2] Continuar jogo existente\n-> "))

if start == 1:
    Personagem.criar_personagem()
    Personagem.salvar_personagem()