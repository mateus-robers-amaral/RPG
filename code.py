import random
import csv

class Personagem():
    def __init__(self, classe, nome, poderes):
        self.classe = classe
        self.nome = nome
        self.poderes = poderes

    def criar_personagem():
        classes = {"Guerreiro": "Força: 10 | Magia: 0 | Coragem: 8 | Furtilidade: 2",
                "Mago": "Força: 2 | Magia: 10 | Coragem: 4 | Furtilidade: 6",
                "Gatuno": "Força: 4 | Magia: 4 | Coragem: 8 | Furtilidade: 10",
                "Orc": "Força: 10 | Magia: 0 | Coragem: 10 | Furtilidade: 0",}
        
        print("Este é o início de sua aventura! Que tal começarmos montando o seu herói?!")
        print("O primeiro passo é escolher a classe!")
        while True:
            classe = int(input("Explore as classes disponíveis:\n[1] Guerreiro\n[2] Mago\n[3] Gatuno\n[4] Orc\n-> "))
            if classe == 1:
                print(classes["Guerreiro"])
                escolha = int(input("[1] Escolher Guerreiro\n[2] Ver outras classes\n-> "))
                if escolha == 1:
                    return "Guerreiro"
                elif escolha == 2:
                    continue

            elif classe == 2:
                print(classes["Mago"])
                escolha = int(input("[1] Escolher Mago\n[2] Ver outras classes\n-> "))
                if escolha == 1:
                    return "Mago"
                elif escolha == 2:
                    continue

            elif classe == 3:
                print(classes["Gatuno"])
                escolha = int(input("[1] Escolher Gatuno\n[2] Ver outras classes\n-> "))
                if escolha == 1:
                    return "Gatuno"
                elif escolha == 2:
                    continue

            elif classe == 4:
                print(classes["Orc"])
                escolha = int(input("[1] Escolher Orc\n[2] Ver outras classes\n-> "))
                if escolha == 1:
                    return "Orc"
                elif escolha == 2:
                    continue
    
    def salvar_personagem(classe):

        novo_personagem = classe

        with open("/Users/rober/Desktop/Estudos/SOLYD/banco/contas.csv", mode='a', newline="") as arquivo:
            escritor_csv = csv.writer(arquivo)
            escritor_csv.writerow(novo_personagem)

    def rolar_dado():
        d20 = random.randint(1, 20)
        print(d20)