# Nome: Bruno Amorim da Silva       RA: 20630380
# Nome: Cícero Matheus Cabral       RA: 20630406
# Nome: Carlos Antony Bletcha Pires RA: 20630414
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

def Main():

    Mapa_Lugares = dict()
    Mapa_Lugares = {'A1': 1, 'A2': 0, 'A3': 0, 'A4': 0, 'A5': 0, 'A6': 0, 'A7': 0, 'A8': 0, 'A9': 0, 'A10': 0, 'A11': 0, 'A12': 0, 'A13': 0, 'A14': 0, 'A15': 0, 'A16': 0, 'A17': 0, 'A18': 0, 'A19': 0, 'A20': 0, 'B1': 0, 'B2': 0, 'B3': 0, 'B4': 0, 'B5': 0, 'B6': 0, 'B7': 0, 'B8': 0, 'B9': 0, 'B10': 0, 'B11': 0, 'B12': 0, 'B13': 0, 'B14': 0, 'B15': 0, 'B16': 0, 'B17': 0, 'B18': 0, 'B19': 0, 'B20': 0, 'C1': 0, 'C2': 0, 'C3': 0, 'C4': 0, 'C5': 0, 'C6': 0, 'C7': 0, 'C8': 0, 'C9': 0, 'C10': 0, 'C11': 0, 'C12': 0, 'C13': 0, 'C14': 0, 'C15': 0, 'C16': 0, 'C17': 0, 'C18': 0, 'C19': 0, 'C20': 0, 'D1': 0, 'D2': 0, 'D3': 0, 'D4': 0, 'D5': 0, 'D6': 0, 'D7': 0, 'D8': 0, 'D9': 0, 'D10': 0, 'D11': 0, 'D12': 0, 'D13': 0, 'D14': 0, 'D15': 0, 'D16': 0, 'D17': 0, 'D18': 0, 'D19': 0, 'D20': 0, 'E1': 0, 'E2': 0, 'E3': 0, 'E4': 0, 'E5': 0, 'E6': 0, 'E7': 0, 'E8': 0, 'E9': 0, 'E10': 0, 'E11': 0, 'E12': 0, 'E13': 0, 'E14': 0, 'E15': 0, 'E16': 0, 'E17': 0, 'E18': 0, 'E19': 0,
                    'E20': 0, 'F1': 0, 'F2': 0, 'F3': 0, 'F4': 0, 'F5': 0, 'F6': 0, 'F7': 0, 'F8': 0, 'F9': 0, 'F10': 0, 'F11': 0, 'F12': 0, 'F13': 0, 'F14': 0, 'F15': 0, 'F16': 0, 'F17': 0, 'F18': 0, 'F19': 0, 'F20': 0, 'G1': 0, 'G2': 0, 'G3': 0, 'G4': 0, 'G5': 0, 'G6': 0, 'G7': 0, 'G8': 0, 'G9': 0, 'G10': 0, 'G11': 0, 'G12': 0, 'G13': 0, 'G14': 0, 'G15': 0, 'G16': 0, 'G17': 0, 'G18': 0, 'G19': 0, 'G20': 0, 'H1': 0, 'H2': 0, 'H3': 0, 'H4': 0, 'H5': 0, 'H6': 0, 'H7': 0, 'H8': 0, 'H9': 0, 'H10': 0, 'H11': 0, 'H12': 0, 'H13': 0, 'H14': 0, 'H15': 0, 'H16': 0, 'H17': 0, 'H18': 0, 'H19': 0, 'H20': 0, 'I1': 0, 'I2': 0, 'I3': 0, 'I4': 0, 'I5': 0, 'I6': 0, 'I7': 0, 'I8': 0, 'I9': 0, 'I10': 0, 'I11': 0, 'I12': 0, 'I13': 0, 'I14': 0, 'I15': 0, 'AI6': 0, 'I17': 0, 'I18': 0, 'I19': 0, 'I20': 0, 'J1': 0, 'J2': 0, 'J3': 0, 'J4': 0, 'J5': 0, 'J6': 0, 'J7': 0, 'J8': 0, 'J9': 0, 'J10': 0, 'J11': 0, 'J12': 0, 'J13': 0, 'J14': 0, 'J15': 0, 'J16': 0, 'J17': 0, 'J18': 0, 'J19': 0, 'J20': 0, }


    # print the contents using zip format.
    









                           
                            
    # status = False
    
    # print('A', Mapa_Lugares.values())
    print("A ","|",Mapa_Lugares.get("A1"),"|","|",Mapa_Lugares.get("A2"),"|","|",Mapa_Lugares.get("A3"),"|","|",Mapa_Lugares.get("A4"),"|","|",Mapa_Lugares.get("A5"),"|","|",Mapa_Lugares.get("A6"),"|","|",Mapa_Lugares.get("A7"),"|","|",Mapa_Lugares.get("A8"),"|","|",Mapa_Lugares.get("A9"),"|","|",Mapa_Lugares.get("A10"),"|","|",Mapa_Lugares.get("A11"),"|","|",Mapa_Lugares.get("A12"),"|","|",Mapa_Lugares.get("A13"),"|","|",Mapa_Lugares.get("A14"),"|","|",Mapa_Lugares.get("A15"),"|","|",Mapa_Lugares.get("A16"),"|","|",Mapa_Lugares.get("A17"),"|","|",Mapa_Lugares.get("A18"),"|","|",Mapa_Lugares.get("A19"),"|","|",Mapa_Lugares.get("A20"),"|" +"\n")
    print("B ","|",Mapa_Lugares.get("B1"),"|","|",Mapa_Lugares.get("B2"),"|","|",Mapa_Lugares.get("B3"),"|","|",Mapa_Lugares.get("B4"),"|","|",Mapa_Lugares.get("B5"),"|","|",Mapa_Lugares.get("B6"),"|","|",Mapa_Lugares.get("B7"),"|","|",Mapa_Lugares.get("B8"),"|","|",Mapa_Lugares.get("B9"),"|","|",Mapa_Lugares.get("B10"),"|","|",Mapa_Lugares.get("B11"),"|","|",Mapa_Lugares.get("B12"),"|","|",Mapa_Lugares.get("B13"),"|","|",Mapa_Lugares.get("B14"),"|","|",Mapa_Lugares.get("B15"),"|","|",Mapa_Lugares.get("B16"),"|","|",Mapa_Lugares.get("B17"),"|","|",Mapa_Lugares.get("B18"),"|","|",Mapa_Lugares.get("B19"),"|","|",Mapa_Lugares.get("B20"),"|" +"\n")
    print("C ","|",Mapa_Lugares.get("C1"),"|","|",Mapa_Lugares.get("C2"),"|","|",Mapa_Lugares.get("C3"),"|","|",Mapa_Lugares.get("C4"),"|","|",Mapa_Lugares.get("C5"),"|","|",Mapa_Lugares.get("C6"),"|","|",Mapa_Lugares.get("C7"),"|","|",Mapa_Lugares.get("C8"),"|","|",Mapa_Lugares.get("C9"),"|","|",Mapa_Lugares.get("C10"),"|","|",Mapa_Lugares.get("C11"),"|","|",Mapa_Lugares.get("C12"),"|","|",Mapa_Lugares.get("C13"),"|","|",Mapa_Lugares.get("C14"),"|","|",Mapa_Lugares.get("C15"),"|","|",Mapa_Lugares.get("C16"),"|","|",Mapa_Lugares.get("C17"),"|","|",Mapa_Lugares.get("C18"),"|","|",Mapa_Lugares.get("C19"),"|","|",Mapa_Lugares.get("C20"),"|" +"\n")
    print("D ","|",Mapa_Lugares.get("D1"),"|","|",Mapa_Lugares.get("D2"),"|","|",Mapa_Lugares.get("D3"),"|","|",Mapa_Lugares.get("D4"),"|","|",Mapa_Lugares.get("D5"),"|","|",Mapa_Lugares.get("D6"),"|","|",Mapa_Lugares.get("D7"),"|","|",Mapa_Lugares.get("D8"),"|","|",Mapa_Lugares.get("D9"),"|","|",Mapa_Lugares.get("D10"),"|","|",Mapa_Lugares.get("D11"),"|","|",Mapa_Lugares.get("D12"),"|","|",Mapa_Lugares.get("D13"),"|","|",Mapa_Lugares.get("D14"),"|","|",Mapa_Lugares.get("D15"),"|","|",Mapa_Lugares.get("D16"),"|","|",Mapa_Lugares.get("D17"),"|","|",Mapa_Lugares.get("D18"),"|","|",Mapa_Lugares.get("D19"),"|","|",Mapa_Lugares.get("D20"),"|" +"\n")
    print("E ","|",Mapa_Lugares.get("E1"),"|","|",Mapa_Lugares.get("E2"),"|","|",Mapa_Lugares.get("E3"),"|","|",Mapa_Lugares.get("E4"),"|","|",Mapa_Lugares.get("E5"),"|","|",Mapa_Lugares.get("E6"),"|","|",Mapa_Lugares.get("E7"),"|","|",Mapa_Lugares.get("E8"),"|","|",Mapa_Lugares.get("E9"),"|","|",Mapa_Lugares.get("E10"),"|","|",Mapa_Lugares.get("E11"),"|","|",Mapa_Lugares.get("E12"),"|","|",Mapa_Lugares.get("E13"),"|","|",Mapa_Lugares.get("E14"),"|","|",Mapa_Lugares.get("E15"),"|","|",Mapa_Lugares.get("E16"),"|","|",Mapa_Lugares.get("E17"),"|","|",Mapa_Lugares.get("E18"),"|","|",Mapa_Lugares.get("E19"),"|","|",Mapa_Lugares.get("E20"),"|" +"\n")
    print("F ","|",Mapa_Lugares.get("F1"),"|","|",Mapa_Lugares.get("F2"),"|","|",Mapa_Lugares.get("F3"),"|","|",Mapa_Lugares.get("F4"),"|","|",Mapa_Lugares.get("F5"),"|","|",Mapa_Lugares.get("F6"),"|","|",Mapa_Lugares.get("F7"),"|","|",Mapa_Lugares.get("F8"),"|","|",Mapa_Lugares.get("F9"),"|","|",Mapa_Lugares.get("F10"),"|","|",Mapa_Lugares.get("F11"),"|","|",Mapa_Lugares.get("F12"),"|","|",Mapa_Lugares.get("F13"),"|","|",Mapa_Lugares.get("F14"),"|","|",Mapa_Lugares.get("F15"),"|","|",Mapa_Lugares.get("F16"),"|","|",Mapa_Lugares.get("F17"),"|","|",Mapa_Lugares.get("F18"),"|","|",Mapa_Lugares.get("F19"),"|","|",Mapa_Lugares.get("F20"),"|" +"\n")
    print("G ","|",Mapa_Lugares.get("G1"),"|","|",Mapa_Lugares.get("G2"),"|","|",Mapa_Lugares.get("G3"),"|","|",Mapa_Lugares.get("G4"),"|","|",Mapa_Lugares.get("G5"),"|","|",Mapa_Lugares.get("G6"),"|","|",Mapa_Lugares.get("G7"),"|","|",Mapa_Lugares.get("G8"),"|","|",Mapa_Lugares.get("G9"),"|","|",Mapa_Lugares.get("G10"),"|","|",Mapa_Lugares.get("G11"),"|","|",Mapa_Lugares.get("G12"),"|","|",Mapa_Lugares.get("G13"),"|","|",Mapa_Lugares.get("G14"),"|","|",Mapa_Lugares.get("G15"),"|","|",Mapa_Lugares.get("G16"),"|","|",Mapa_Lugares.get("G17"),"|","|",Mapa_Lugares.get("G18"),"|","|",Mapa_Lugares.get("G19"),"|","|",Mapa_Lugares.get("G20"),"|" +"\n")
    print("H ","|",Mapa_Lugares.get("H1"),"|","|",Mapa_Lugares.get("H2"),"|","|",Mapa_Lugares.get("H3"),"|","|",Mapa_Lugares.get("H4"),"|","|",Mapa_Lugares.get("H5"),"|","|",Mapa_Lugares.get("H6"),"|","|",Mapa_Lugares.get("H7"),"|","|",Mapa_Lugares.get("H8"),"|","|",Mapa_Lugares.get("H9"),"|","|",Mapa_Lugares.get("H10"),"|","|",Mapa_Lugares.get("H11"),"|","|",Mapa_Lugares.get("H12"),"|","|",Mapa_Lugares.get("H13"),"|","|",Mapa_Lugares.get("H14"),"|","|",Mapa_Lugares.get("H15"),"|","|",Mapa_Lugares.get("H16"),"|","|",Mapa_Lugares.get("H17"),"|","|",Mapa_Lugares.get("H18"),"|","|",Mapa_Lugares.get("H19"),"|","|",Mapa_Lugares.get("H20"),"|" +"\n")
    print("I ","|",Mapa_Lugares.get("I1"),"|","|",Mapa_Lugares.get("I2"),"|","|",Mapa_Lugares.get("I3"),"|","|",Mapa_Lugares.get("I4"),"|","|",Mapa_Lugares.get("I5"),"|","|",Mapa_Lugares.get("I6"),"|","|",Mapa_Lugares.get("I7"),"|","|",Mapa_Lugares.get("I8"),"|","|",Mapa_Lugares.get("I9"),"|","|",Mapa_Lugares.get("I10"),"|","|",Mapa_Lugares.get("I11"),"|","|",Mapa_Lugares.get("I12"),"|","|",Mapa_Lugares.get("I13"),"|","|",Mapa_Lugares.get("I14"),"|","|",Mapa_Lugares.get("I15"),"|","|",Mapa_Lugares.get("I16"),"|","|",Mapa_Lugares.get("I17"),"|","|",Mapa_Lugares.get("I18"),"|","|",Mapa_Lugares.get("I19"),"|","|",Mapa_Lugares.get("I20"),"|" +"\n")
    print("J ","|",Mapa_Lugares.get("J1"),"|","|",Mapa_Lugares.get("J2"),"|","|",Mapa_Lugares.get("J3"),"|","|",Mapa_Lugares.get("J4"),"|","|",Mapa_Lugares.get("J5"),"|","|",Mapa_Lugares.get("J6"),"|","|",Mapa_Lugares.get("J7"),"|","|",Mapa_Lugares.get("J8"),"|","|",Mapa_Lugares.get("J9"),"|","|",Mapa_Lugares.get("J10"),"|","|",Mapa_Lugares.get("J11"),"|","|",Mapa_Lugares.get("J12"),"|","|",Mapa_Lugares.get("J13"),"|","|",Mapa_Lugares.get("J14"),"|","|",Mapa_Lugares.get("J15"),"|","|",Mapa_Lugares.get("J16"),"|","|",Mapa_Lugares.get("J17"),"|","|",Mapa_Lugares.get("J18"),"|","|",Mapa_Lugares.get("J19"),"|","|",Mapa_Lugares.get("J20"),"|" +"\n")


    status = False

    
    # while status == False:
    #     print("Escolha uma fileira <de A a J>")
    #     fileira=str(input("Digite uma Letra: "))

    #     print('')

    #     print("Escolha um assento <de 1 a 20>")
    #     assento = input("Digite um número: ")

    #     print('')

    #     nome = input("Digite seu nome: ")
    #     print(f'Olá {nome}!')
    #     cadeira = fileira + assento

    #     #verifica se o assento está ocupado
    #     if Mapa_Lugares[cadeira] == 1:
    #         print('Assento Ocupado! Escolha outro.')
    #     elif Mapa_Lugares[cadeira] == 0:
    #         Mapa_Lugares[cadeira] = 1
    #         status = True
    #         print("Lugar reservado com sucesso!")

    
    # print("Digite o seu nome: ")
    # nome=str(input("Digite uma Letra: "))

    # print(Mapa_Lugares[cadeira])
    
Main()
