import os
import platform
import time
from jogadorClass import Jogador
from tabuleiroClass import Tabuleiro

def jogo():
    sistema_operacional = platform.system()

    while True:
        # Verificando o sistema operacional para limpar o terminal
        if sistema_operacional == "Windows":
            os.system('cls')
        else:
            os.system('clear')

        print("Batalha de Submarinos - 2 Jogadores\n")
        # Recolhendo nome dos dois jogadores
        nome_jogador1 = input("Nome do Jogador 1: ")
        nome_jogador2 = input("Nome do Jogador 2: ")

        # Instanciando as classes de jogador e tabuleiro
        tabuleiro1 = Tabuleiro()
        tabuleiro2 = Tabuleiro()
        jogador1 = Jogador(nome_jogador1)
        jogador2 = Jogador(nome_jogador2)

        print(f"{nome_jogador1}, posicione seus 3 submarinos (linha e coluna de 0 a 4):")
        # Considerando que são 3 submarinos, estou fazendo um loop com range 3
        for _ in range(3):
            # O loop infinito é quebrado com break, portanto quando encontrada uma condição satisfatória, ele quebra o loop
            while True:
                # Tratando o erro de validade de posição
                try:
                    # Recebendo a linha e a coluna escolhida pelo jogador
                    linha = int(input(f"Posição do submarino {_ + 1} (linha): "))
                    coluna = int(input(f"Posição do submarino {_ + 1} (coluna): "))
                    # Se a linha e a coluna forem satisfatórias, ele dá um break e sai do while
                    if tabuleiro1.posicionar_submarino(linha, coluna):
                        break
                    else:
                        # Caso a condição do if não satisfaça, ele bate no else e pede para escolher uma linha e/ou coluna válidas
                        print("Posição inválida ou ocupada. Tente novamente.")
                except ValueError:
                    print("Entrada inválida. Digite um número de 0 a 4.")


        # Faz a mesma coisa do explicado acima
        if sistema_operacional == "Windows":
            os.system('cls')
        else:
            os.system('clear')

        input(f"{nome_jogador2}, pressione ENTER para continuar.")
        if sistema_operacional == "Windows":
            os.system('cls')
        else:
            os.system('clear')

        print(f"{nome_jogador2}, posicione seus 3 submarinos (linha e coluna de 0 a 4):")
        for _ in range(3):
            while True:
                try:
                    linha = int(input(f"Posição do submarino {_ + 1} (linha): "))
                    coluna = int(input(f"Posição do submarino {_ + 1} (coluna): "))
                    if tabuleiro2.posicionar_submarino(linha, coluna):
                        break
                    else:
                        print("Posição inválida ou ocupada. Tente novamente.")
                except ValueError:
                    print("Entrada inválida. Digite um número de 0 a 4.")

        if sistema_operacional == "Windows":
            os.system('cls')
        else:
            os.system('clear')

        # Aqui é onde são impressos os tabuleiros
        while True:
            print(f"{nome_jogador1}'s Tabuleiro:")
            tabuleiro1.imprimir()
            print("\n")
            print(f"{nome_jogador2}'s Tabuleiro:")
            tabuleiro2.imprimir()
            # Irá esperar 5 segundos antes de limpar o terminal
            time.sleep(5)
            if sistema_operacional == "Windows":
                os.system('cls')
            else:
                os.system('clear')

            # O jogador 1 escolhe o tiro que irá dar
            jogador1.atirar(tabuleiro2)

            # Caso acerte todos ele recebe a mensagem de que venceu
            if jogador2.submarinos_afundados == 3:
                print(f"{nome_jogador2} venceu! {nome_jogador1}'s submarinos foram afundados.")
                break

            # Mesma coisa do acima, porém para o jogador 2
            input(f"{nome_jogador2}, pressione ENTER para continuar.")
            if sistema_operacional == "Windows":
                os.system('cls')
            else:
                os.system('clear')

            print(f"{nome_jogador1}'s Tabuleiro:")
            tabuleiro1.imprimir()
            print("\n")
            print(f"{nome_jogador2}'s Tabuleiro:")
            tabuleiro2.imprimir()
            time.sleep(5)
            if sistema_operacional == "Windows":
                os.system('cls')
            else:
                os.system('clear')
                
            jogador2.atirar(tabuleiro1)

            if jogador1.submarinos_afundados == 3:
                print(f"{nome_jogador1} venceu! {nome_jogador2}'s submarinos foram afundados.")
                break

        # Imprime a quantidade de tiros
        print(f"{nome_jogador1} fez {jogador1.tiros} tiros.")
        print(f"{nome_jogador2} fez {jogador2.tiros} tiros.")

        # Pergunta se quer jogar novamente
        jogar_novamente = input("Deseja jogar novamente? (S/N): ")
        if jogar_novamente.lower() != 's':
            break

if __name__ == "__main__":
    jogo()