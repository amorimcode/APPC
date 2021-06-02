# Nome: Bruno Amorim da Silva RA: 20630380

""" 1. Descrição do problema:
Fazer um programa que exibe o mapa de lugares de um Teatro, o cliente escolhe o lugar e gera
o ingresso. O ingresso é individual e para mais ingressos repetir o processo. O processo deve ser
repetido até que seja digitado algo para parar. Depois de imprimir o Ingresso, perguntar se
deseja fazer nova reserva: Sim (S) ou Não (N).
Mapa_Lugares – iniciar toda com ZERO
• Zero significa lugar vazio;
• Quando um lugar for escolhido, mudar a posição para 1.
O programa deve apresentar o mapa de lugares, como mostrado abaixo. Observe que no lugar
das linhas devem aparecer LETRAS e os números das colunas começam em UM e estão na
parte debaixo da matriz """

# Programa principal
def main():
    Mapa_Lugares = [[0,0,0], [0,0,0], [0,0,0]]
    for linha in range(0, 3):
        for coluna in range(0, 3):
            Mapa_Lugares[linha] [coluna] = int(input(f"Digite um valor para [{linha}, {coluna}] "))
    print('-=' * 30)
    for linha in range(0, 3):
        for coluna in range(0, 3):
            print(f'[{Mapa_Lugares[linha] [coluna]}]', end='')
        print()
main()