from operacoesbd import *

opcao = 0
barra = "-" * 50
itemsMenu = ["1","2","3","4","5","6","7"]
conexao = criarConexao('localhost','root','danielfera','ouvidoria')

while opcao != 7:
    # --------------MENU---------------
    print(barra)
    print("1) Listagem das Manifestações "
          "\n2) Listagem das Manifestações por tipo"
          "\n3) Criar uma nova Manifestação "
          "\n4) Exibir quantidade de Manifestações "
          "\n5) Pesquisar uma manifestação por código "
          "\n6) Excluir Manifestção por código "
          "\n7) Sair do Sistema")
    print(barra)

    opcao = input("Digite o código da opção: ")
    print(barra)

    if opcao in itemsMenu: # Transforma a opção em inteiro caso ela seja um dos numeros presentes no menu
        opcao = int(opcao)

    # --------------OPÇÕES---------------
    # 1) Listagem das Manifestações
    if opcao == 1:  
        sql = "select * from manifestacoes;"
        retorno = listarBancoDados(conexao,sql)

        if len(retorno) == 0:
            print("Não existe nunhuma manifestação até o momento")
        else:
            print(barra*2)
            for item in retorno:
                print("CÓDIGO:",item[0],"|","NOME:",item[1],"|","MANIFESTAÇÃO:",item[2],"|","TIPO:",item[3],"|")
            print(barra * 2)

    # 2) Listagem das Manifestações por tipo
    elif opcao == 2: 
        sql = "select * from manifestacoes where tipo = %s"

        while True: # verifica se o codigo do tipo de manifestação é valido
            print("ESCOLHA UM TIPO DE MANIFESTAÇÃO \n1) Elogio \n2) Sugestão \n3) Reclamação")
            print(barra)
            tipo = input("Digite o codigo: ")
            print(barra)

            if tipo in itemsMenu: # Transforma a opção em inteiro caso ela seja um dos numeros presentes no menu
                tipo = int(tipo)


            if tipo == 1:
                tipo = "Elogio"
                break
            elif tipo == 2:
                tipo = "Sugestão"
                break
            elif tipo == 3:
                tipo = "Reclamação"
                break
            else:
                print("CÓDIGO INVALIDO")
                print(barra)

        dados = [tipo]
        retorno = listarBancoDados(conexao,sql,dados)

        if len(retorno) == 0:
            print("Não existe nunhum", tipo)
        else:
            print(barra * 2)
            for item in retorno:
                print("CODIGO:", item[0], "|", "NOME:", item[1], "|", "MANIFESTAÇÃO:", item[2], "|", "TIPO:", item[3], "|")
            print(barra * 2)

    # 3) Criar uma nova manifestação
    elif opcao == 3: 
        sql = "insert into manifestacoes (nome_usuario,manifestacao,tipo) values (%s,%s,%s);"

        while True: # Verifica se o nome tem 3 caracteres
            nomeUsuario = input("Digite o nome do usuario que inseriu a manifestação:")
            print(barra)

            if len(nomeUsuario) >= 3:
                break
            else:
                print(barra)
                print("O nome tem que conter no minimo 3 caracteres")
                print(barra)

        while True:
            print("ESCOLHA UM TIPO DE MANIFESTAÇÃO \n1) Elogio \n2) Sugestão \n3) Reclamação")
            print(barra)
            tipo = input("Digite o codigo: ")
            print(barra)

            if tipo in itemsMenu: # Transforma a opção em inteiro caso ela seja um dos numeros presentes no menu
                tipo = int(tipo)


            if tipo == 1:
                tipo = "Elogio"
                break
            elif tipo == 2:
                tipo = "Sugestão"
                break
            elif tipo == 3:
                tipo = "Reclamação"
                break
            else:
                print("CÓDIGO INVALIDO")
                print(barra)

        while True: # Verifica se a manifestação tem 3 caracteres
            manifestacao = input("Digite sua manifestação: ")

            if len(manifestacao) >= 3:
                break
            else:
                print(barra)
                print("A manifestação tem que conter no minimo 3 caracteres")
                print(barra)

        dados = [nomeUsuario,manifestacao,tipo]
        codigoManifestacao = insertNoBancoDados(conexao,sql,dados)

        print(barra)
        print("Manifestação inserida com sucesso! Seu código é",codigoManifestacao)

    # 4) Exibir quantidade de manifestações
    elif opcao == 4: 
        sql = "select count(*) from manifestacoes;"
        retorno = listarBancoDados(conexao,sql)

        if retorno == 0:
            print("Nenhuma manifestação até o momento!")
        elif retorno == 1:
            print("Até o momento, o sistema possui somente 1 manifestação")
        else:
            print("Até o momento, o sistema possui exatas " + str(retorno[0][0]) + " manifestações")

    # 5) Pesquisar uma manifestação por código
    elif opcao == 5: 
        sql = "select * from manifestacoes where codigo = %s"
        codigo = int(input("Digite o codigo da manifestação: "))
        print(barra)
        dados = [codigo]
        retorno = listarBancoDados(conexao, sql, dados)

        if len(retorno) == 0:
            print("Não existe nunhuma manifestação com esse código")
        else:
            print(barra*2)
            for item in retorno:
                print("CÓDIGO:",item[0],"|","NOME:",item[1],"|","MANIFESTAÇÃO:",item[2],"|","TIPO:",item[3],"|")
            print(barra*2)

    # 6) Delete manifestação por codigo
    elif opcao == 6: 
        sql = "delete from manifestacoes where codigo = %s"
        codigo = int(input("Digite o código da Manifestação: "))
        dados = [codigo]
        retorno = excluirBancoDados(conexao,sql,dados)

        if retorno > 0:
            print("Manifestação excluida com sucesso!")
        else:
            print("Não existe manifestação com esse código!")

    # OPÇÃO INVALIDA
    elif opcao != 7:
        print("OPÇÃO INVALIDA!!")

print("Agradecemos por nos ajudar a melhorar! Seu feedback é fundamental para o nosso sucesso!")
encerrarConexao(conexao)