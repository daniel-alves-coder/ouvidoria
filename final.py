from operacoesbd import *

opcao = 0
barra = "-" * 50

conexao = criarConexao('localhost','root','danielfera','ouvidoria')

while opcao != 7:
    print(barra)
    print("1) Listagem das Manifestações "
          "\n2) Listagem das Manifestações por tipo"
          "\n3) Criar uma nova Manifestação "
          "\n4) Exibir quantidade de Manifestações "
          "\n5) Pesquisar uma manifestação por código "
          "\n6) Excluir Manifestção por código "
          "\n7) Sair do Sistema")
    print(barra)

    opcao = int(input("Digite o código da opção: "))
    print(barra)

    if opcao == 1:  # Listagem das Manifestações
        sql = "select * from manifestacoes;"
        retorno = listarBancoDados(conexao,sql)

        print(barra*2)
        for item in retorno:
            print("CÓDIGO:",item[0],"|","NOME:",item[1],"|","MANIFESTAÇÃO:",item[2],"|","TIPO:",item[3],"|")
        print(barra * 2)

    elif opcao == 2: # Listagem das Manifestações por tipo
        print("ESCOLHA UM TIPO DE MANIFESTAÇÃO \n1) Elogio \n2) Sugestão \n3) Reclamação")
        print(barra)
        tipo = int(input("Digite o codigo: "))
        sql = "select * from manifestacoes where tipo = %s"

        if tipo == 1:
            dados = ["Elogio"]
        elif tipo == 2:
            dados = ["Sugestão"]
        elif tipo == 3:
            dados = ["Reclamação"]
        else:
            print("TIPO INVALIDO")

        retorno = listarBancoDados(conexao,sql,dados)

        print(barra * 2)
        for item in retorno:
            print("CODIGO:", item[0], "|", "NOME:", item[1], "|", "MANIFESTAÇÃO:", item[2], "|", "TIPO:", item[3], "|")
        print(barra * 2)

    elif opcao == 3: # Criar uma nova manifestação
        sql = "insert into manifestacoes (nome_usuario,manifestacao,tipo) values (%s,%s,%s);"

        nomeUsuario = input("Digite o nome do usuario que inseriu a manifestação:")
        print(barra)

        print("ESCOLHA UM TIPO DE MANIFESTAÇÃO \n1) Elogio \n2) Sugestão \n3) Reclamação")
        print(barra)
        tipo = int(input("Digite o codigo: "))
        print(barra)

        if tipo == 1:
            tipo = "elogio"
        elif tipo == 2:
            tipo = "Sugestão"
        elif tipo == 3:
            tipo = "Reclamação"
        else:
            print("TIPO INVALIDO")

        manifestacao = input("Digite sua manifestação: ")

        dados = [nomeUsuario,manifestacao,tipo]
        insertNoBancoDados(conexao,sql,dados)

        print("Manifestação inserida com sucesso!")

    elif opcao == 4: # Exibir quantidade de manifestações
        sql = "select count(*) from manifestacoes;"
        retorno = listarBancoDados(conexao,sql)

        if retorno == 0:
            print("Nenhuma manifestação até o momento!")
        elif retorno == 1:
            print("Até o momento, o sistema possui somente 1 manifestação")
        else:
            for item in retorno:
                print("Até o momento, o sistema possui exatas " + str(item[0]) + " manifestações")

    elif opcao == 5: # Pesquisar uma manifestação por código
        sql = "select * from manifestacoes where código = %s"
        codigo = int(input("Digite o codigo da manifestação: "))
        print(barra)
        dados = [codigo]

        retorno = listarBancoDados(conexao, sql, dados)

        print(barra*2)
        for item in retorno:
            print("CÓDIGO:",item[0],"|","NOME:",item[1],"|","MANIFESTAÇÃO:",item[2],"|","TIPO:",item[3],"|")
        print(barra*2)

    elif opcao == 6:
        sql = "delete from manifestacoes where codigo = %s"
        codigo = int(input("Digite o código da Manifestação: "))
        dados = [codigo]
        retorno = excluirBancoDados(conexao,sql,dados)

        if retorno > 0:
            print("Manifestação excluida com sucesso!")
        else:
            print("Não existe manifestação com esse código!")

    elif opcao != 7:
        print("OPÇÃO INVALIDA!!")

encerrarConexao(conexao)