"""
========
Problema
========

Joãozinho é estudante da UFES e gostaria de ter um controle maior do que
os estudantes comem no Restaurante Universitário. Para isso, ele criará
um programa em Python para facilitar sua vida. O programa de Joãozinho
recebe uma fila de alunos e uma pilha de diferentes pratos, lembrando que
o primeiro prato a ser inserido na pilha será o último a ser consumido e o
primeiro aluno que entrar na fila será o primeiro aluno a comer. Quando um
aluno da fila pegar um prato da pilha, estes serão retirados da fila e da pilha,
respectivamente.

Agora você tem um desafio: replicar o programa de Joãozinho. Para ajudar você, abaixo temos as entradas e as saídas do programa dele. Na entrada,
o primeiro número é a quantidade de pratos que serão inseridos na pilha e na
sequência o nome dos pratos. Após os nomes dos pratos, há a quantidade de
alunos que serão inseridos na fila e seus respectivos nomes. Nas saídas temos
os pratos que cada aluno pegou. Caso a fila de alunos finalize junto com a
pilha de pratos, quer dizer que todos os alunos comeram. Sendo assim, seu
programa deverá informar: “Todos os pratos foram consumidos e todos os
alunos almoçaram.”. Caso haja mais pratos que alunos, quando a fila de alunos acabar, seu programa deverá informar quantos pratos sobraram e quais
foram esses pratos. Caso haja mais alunos que pratos, quando acabar a pilha
de pratos, seu programa deverá informar quantos alunos ficaram sem almoço
e os respectivos alunos que ficaram sem almoço.

Boa sorte!


Casos de Teste
Lembre-se que as entradas e saídas devem ser idênticas às dos casos de teste.
------------------------------------------------------------
Exemplo de Entrada  |  Exemplo de Saida
------------------------------------------------------------
5                   |  Lara pegou o prato: Sopa
Pizza               |  Milla pegou o prato: Carne Moída
Hambúrguer          |  Matheus pegou o prato: Macarrão
Macarrão            |  Victoria pegou o prato: Hamburguer
Carne Moída         |  Sobraram 1 pratos
Sopa Pizza	        |
4		              |
Lara                |
Milla 		        |
Matheus		        |
Victoria            |
------------------------------------------------------------
3                   | João pegou o prato: Proteína de soja
Churrasco           |  Bruno pegou o prato: Sushi
Sushi               |  Kevin pegou o prato: Churrasco
Proteína de soja    |  5 ficaram sem almoço:
8 Caio		        |
João Afonso	        |
Bruno Matheus       |
Kevin Thiago        |
Caio Gabriel        |
Afonso              |
Matheus             |
Thiago              |
Gabriel             |
------------------------------------------------------------
"""
def nomesFuncionarios(quantiFun):

    for x in range(1, (quantiFun + 1)):
        nomeFun = input()
        listaNomes.append(nomeFun)

def nomesPratos(quantiPra):

    for x in range(1, (quantiPra + 1)):
        nomePra = input()
        listaPratos.insert(0, nomePra)

# Variáveis
listaPratos = []
compPratos = []
listaNomes = []

#entradas

qPratos = int(input())
nomesPratos(qPratos)

qNomes = int(input())
nomesFuncionarios(qNomes)

if len(listaPratos) == len(listaNomes):

  for i, elemento in enumerate(listaPratos):
      print("{} pegou o prato: {}".format(listaNomes[i], elemento))
  
  print("Todos os pratos foram consumidos e todos os alunos almoçaram.")

elif len(listaPratos) > len(listaNomes):
  for i, elemento in enumerate(listaNomes):
    print("{} pegou o prato: {}".format(elemento, listaPratos[i]))

  sub1 = len(listaPratos) - len(listaNomes)
  print("Sobraram {} pratos:".format(sub1))

  for a in range(len(listaNomes), len(listaPratos)):
    print(f"{listaPratos[a]}")
  
elif len(listaPratos) < len(listaNomes):

    for i, elemento in enumerate(listaPratos):
      print("{} pegou o prato: {}".format(listaNomes[i], elemento))

    sub2 = len(listaNomes) - len(listaPratos)
    print("{} ficaram sem almoço:".format(sub2))

    for a in range(len(listaPratos), len(listaNomes)):
      print(f"{listaNomes[a]}")