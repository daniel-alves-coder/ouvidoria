'''
Darlison Davi Moura Valdivino - RA:2515050008
Allef Soares do Espírito Santo Oliveira - RA:2515050023
José Eduardo Pereira da Silva - RA:2515050040
Eduardo Matias de Oliveira Eufrásio - RA:2515050007
Daniel Alves da Costa - RA:2515050057
Eduardo Araújo Gomes neto - RA:2515050045
Victor Valentim de Carvalho - RA:2515050028
'''

manifestacoes = [ ]
opcao = 0
barra = "-" * 50

while opcao != 5:
    print(barra)
    print("1) Listagem das Manifestações "
          "\n2) Criar uma nova Manifestação "
          "\n3) Exibir quantidade de manifestações "
          "\n4) Pesquisar uma manifestação por código "
          "\n5) Sair do Sistema")
    print(barra)

    opcao = int(input("Digite o codigo da opção: "))

    print(barra)

    if opcao == 1: #Listagem das Manifestações
        if len(manifestacoes) == 0:
            print("Nenhuma manifestação até o momento!")
        else:
            print("MANIFESTAÇÕES:")
            for index in range(len(manifestacoes)):
                print("manifestação " + str(index + 1) + ") " + manifestacoes[index])

    elif opcao == 2: #Criar uma nova Manifestação
        novaManifestacao = input("Digite a sua manifestação: ")
        manifestacoes.append(novaManifestacao)
        print("Manifestação cadastrada com sucesso o seu codigo é " + str(len(manifestacoes)))

    elif opcao == 3: #Exibir quantidade de manifestações
        if len(manifestacoes) == 0:
            print("Nenhuma manifestação até o momento!")
        elif len(manifestacoes) == 1:
            print("Até o momento, o sistema possui somente 1 manifestação")
        else:
            print("Até o momento, o sistema possui exatas " + str(len(manifestacoes)) + " manifestações")

    elif opcao == 4: #Pesquisar uma manifestação por código
        codigo = int(input("Digite o codigo da manifetação: "))

        if codigo < 1 or codigo > len(manifestacoes): #verifica se o codigo é valido
            print("CODIGO DE MANIFESTAÇÃO INVALIDO")
        else:
            print(barra)
            print("Manifestação de codigo " + str(codigo) + ": ")
            print(manifestacoes[codigo - 1])

    elif opcao != 5: #Caso o usuario digite uma opção que não existe
        print("OPÇÃO INVALIDA")


print("Agradecemos por nos ajudar a melhorar! Seu feedback é fundamental para o nosso sucesso!")