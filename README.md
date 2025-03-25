# Projeto Ouvidoria

### criar um sistema que acolhe manifestações dos seus clientes



## Menu
### O sistema deve apresentar um menu com 5 opções:
1. Listagem das Manifestações
2. Criar uma nova Manifestação
3. Exibir quantidade de manifestações
4. Pesquisar uma manifestação por código
5. Sair do Sistema

## REGRAS
> O sistema deve funcionar por meio de listas, exemplo:
>```
>manifestacao = [ ]
>```

> A primeira opção (Listagem das Manifestações), deve listar as manifestações **no seguinte formato**: 
>> * Manifestação 1) Não possui papel no banheiro 
>> * Manifestação 2) A porta não está fechando

> A segunda opção (Criar uma nova Manifestação), deve solicitar ao usuário
a descrição da Manifestação e adicioná-la a uma lista. Ao final, deve informar ao usuário
final a seguinte mensagem :
> ``` Manifestação cadastrada com sucesso. O seu código é 12 ```.
Note que, o 12 se refere ao código do item, de modo que, o primeiro item da lista (índice
0), corresponderá ao código 1, enquanto que, o segundo item da lista (índice 1),
corresponderá ao código 2. (Dica: Lembre-se do len) 

> A terceira opção (Exibir quantidade de manifestações), exibe apenas a quantidade de
Manifestações, no seguinte estilo: 
>```
>Até o momento, o sistema possui exatas 13 manifestações. 
>```

> A opção 4 (Pesquisar uma manifestação por código)
solicita ao usuário o código da manifestação ```Por favor, informe o código da
manifestação``` e exibe o conteúdo da manifestação. Traduzindo em código, se o código
informado for 123, estou me referindo a lista na posição 122, enquanto que, se o código
for 1, estou me referindo a lista na posição 0. 

> A última opção, como se é de esperar, encerra o sistema. Se quiser, agradeça o uso, pois
é o seu primeiro sistema e é importante agradecer a quem estiver usando. 

###### Abra a folha de esplicação [clicando aqui](https://www.daniel-abella.com/unifacisa/p1/atividades/python-projeto-etapa1.pdf).

#
