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

# Pessoa escolhe 1 lugar, este se vazio, muda o valor para 1#
# Pedir Nome da pessoa #
# Emitir a Nota #
# Perguntar se quer reservar mais (s) ou (n) #

def main():
    Mapa_Lugares = dict()
    Mapa_Lugares = {'A1': 1, 'A2': 0, 'A3': 0, 'A4': 0, 'A5': 0, 'A6': 0, 'A7': 0, 'A8': 0, 'A9': 0, 'A10': 0, 'A11': 0, 'A12': 0, 'A13': 0, 'A14': 0, 'A15': 0, 'A16': 0, 'A17': 0, 'A18': 0, 'A19': 0, 'A20': 0, 'B1': 0, 'B2': 0, 'B3': 0, 'B4': 0, 'B5': 0, 'B6': 0, 'b7': 0, 'b8': 0, 'b9': 0, 'B10': 0, 'b11': 0, 'b12': 0, 'b13': 0, 'b14': 0, 'b15': 0, 'b16': 0, 'b17': 0, 'b18': 0, 'b19': 0, 'b20': 0, 'C1': 0, 'C2': 0, 'C3': 0, 'C4': 0, 'C5': 0, 'C6': 0, 'C7': 0, 'C8': 0, 'C9': 0, 'C10': 0, 'C11': 0, 'C12': 0, 'C13': 0, 'C14': 0, 'C15': 0, 'C16': 0, 'C17': 0, 'C18': 0, 'C19': 0, 'C20': 0, 'D1': 0, 'D2': 0, 'D3': 0, 'D4': 0, 'D5': 0, 'D6': 0, 'D7': 0, 'D8': 0, 'D9': 0, 'D10': 0, 'D11': 0, 'D12': 0, 'D13': 0, 'D14': 0, 'D15': 0, 'D16': 0, 'D17': 0, 'D18': 0, 'D19': 0, 'D20': 0, 'E1': 0, 'E2': 0, 'E3': 0, 'E4': 0, 'E5': 0, 'E6': 0, 'E7': 0, 'E8': 0, 'E9': 0, 'E10': 0, 'E11': 0, 'E12': 0, 'E13': 0, 'E14': 0, 'E15': 0, 'E16': 0, 'E17': 0, 'E18': 0, 'E19': 0,
                    'E20': 0, 'F1': 0, 'F2': 0, 'F3': 0, 'F4': 0, 'F5': 0, 'F6': 0, 'F7': 0, 'F8': 0, 'F9': 0, 'F10': 0, 'F11': 0, 'F12': 0, 'F13': 0, 'F14': 0, 'F15': 0, 'F16': 0, 'F17': 0, 'F18': 0, 'F19': 0, 'F20': 0, 'G1': 0, 'G2': 0, 'G3': 0, 'G4': 0, 'G5': 0, 'G6': 0, 'G7': 0, 'G8': 0, 'G9': 0, 'G10': 0, 'G11': 0, 'G12': 0, 'G13': 0, 'G14': 0, 'G15': 0, 'G16': 0, 'G17': 0, 'G18': 0, 'G19': 0, 'G20': 0, 'H1': 0, 'H2': 0, 'H3': 0, 'H4': 0, 'H5': 0, 'H6': 0, 'H7': 0, 'H8': 0, 'H9': 0, 'H10': 0, 'H11': 0, 'H12': 0, 'H13': 0, 'H14': 0, 'H15': 0, 'H16': 0, 'H17': 0, 'H18': 0, 'H19': 0, 'H20': 0, 'I1': 0, 'I2': 0, 'I3': 0, 'I4': 0, 'I5': 0, 'I6': 0, 'I7': 0, 'I8': 0, 'I9': 0, 'I10': 0, 'I11': 0, 'I12': 0, 'I13': 0, 'I14': 0, 'I15': 0, 'AI6': 0, 'I17': 0, 'I18': 0, 'I19': 0, 'I20': 0, 'J1': 0, 'J2': 0, 'J3': 0, 'J4': 0, 'J5': 0, 'J6': 0, 'J7': 0, 'J8': 0, 'J9': 0, 'J10': 0, 'J11': 0, 'J12': 0, 'J13': 0, 'J14': 0, 'J15': 0, 'J16': 0, 'J17': 0, 'J18': 0, 'J19': 0, 'J20': 0, }

    status = False
    
    print('A', Mapa_Lugares.values())

    
    while status == False:
        print("Escolha uma fileira <de A a J>")
        fileira=str(input("Digite uma Letra: "))

        print('')

        print("Escolha um assento <de 1 a 20>")
        assento = input("Digite um número: ")

        print('')

        nome = input("Digite seu nome: ")
        print(f'Olá {nome}!')
        cadeira = fileira + assento

        #verifica se o assento está ocupado
        if Mapa_Lugares[cadeira] == 1:
            print('Assento Ocupado! Escolha outro.')
        elif Mapa_Lugares[cadeira] == 0:
            Mapa_Lugares[cadeira] = 1
            status = True
            print("Lugar reservado com sucesso!")

    
    # print("Digite o seu nome: ")
    # nome=str(input("Digite uma Letra: "))

    # print(Mapa_Lugares[cadeira])
    
main()
