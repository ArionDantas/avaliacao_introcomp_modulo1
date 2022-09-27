"""
========
Problema
========
Crie um programa que receba uma lista de preços separados por ponto e
vírgula e crie uma lista com esses preços. Após criar a lista, imprima o
tamanho da lista, a lista em ordem crescente com os valores separados por “
; ”, a lista em ordem decrescente com os valores separados por “ ; “, a soma
dos valores da lista, a média dos valores da lista e a quantidade de preços
acima da média.

Casos de Teste
Lembre-se que as entradas e saídas devem ser idênticas às dos casos de teste.
----------------------------------------------------------------
Exemplo de Entrada    |  Exemplo de Saida
----------------------------------------------------------------
2;2;2;2;2;2;2         | tamanho = 7
		                |	lista em ordem crescente:
		                |	2.0 ; 2.0 ; 2.0 ; 2.0 ; 2.0 ; 2.0 ; 2.0
		                |	lista em ordem decrescente:
		                |	2.0 ; 2.0 ; 2.0 ; 2.0 ; 2.0 ; 2.0 ; 2.0
		                |	soma = 14.0
		                |	media = 2.0
		                |	Existem 0 preços acima da média
----------------------------------------------------------------
2.5;5.5;7.9;3.1       |	tamanho = 4
		                |	lista em ordem crescente:
		                |	2.5 ; 3.1 ; 5.5 ; 7.9
		                |	lista em ordem decrescente:
		                | 7.9 ; 5.5 ; 3.1 ; 2.5
		                |	soma = 19.0
		                |	media = 4.7
		                |	Existem 2 preços acima da média
----------------------------------------------------------------

"""
entrada = input().split(";")
listaInt = []
listaStr = []
listaStr1 = []
contador = 0
contadorAcimaMedia = 0



for x in entrada:
  x = float(x)
  listaInt.append(x)

for x in listaInt:
    contador = x + contador

media = contador / len(listaInt)
for i in listaInt:
  if i > media:
    contadorAcimaMedia += 1


print("tamanho = {}".format(len(listaInt)))
listaInt.sort()
for s in listaInt:
  s = str(s)
  listaStr.append(s)
print("lista em ordem crescente:\n{}".format(" ; ".join(listaStr)))
listaInt.sort(reverse=True)
for si in listaInt:
  si = str(si)
  listaStr1.append(si)
print("lista em ordem decrescente:\n{}".format(" ; ".join(listaStr1)))
print("soma = {:.1f}".format(contador))
print("media = {}".format(media))
print("Existem {} preços acima da média".format(contadorAcimaMedia))