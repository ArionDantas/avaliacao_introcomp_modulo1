"""
========
Problema
========

Faça um programa que receba o nome de um país e sua área total em km2 e
retorne a porcentagem da área total do planeta que o país ocupa. Leve em
consideração que o planeta Terra tem uma área total de 149.000.000 km2.
A entrada consiste em um número N indicando a quantidade de países a
serem lidos e em seguida N linhas, cada uma contendo o nome de um país e
sua área total em km2. Seu programa deve imprimir a porcentagem de área
que cada país ocupa em relação ao planeta Terra e indicar qual país ocupa
mais área.

Casos de Teste
Lembre-se que as entradas e saídas devem ser idênticas às dos casos de teste.
-------------------------------------------------------------
Exemplo de Entrada    |    Exemplo de Saida
-------------------------------------------------------------
3		                |
Brasil                |   Brasil ocupa 5.72% da terra
8516000               |   Argentina ocupa 1.87% da terra
Argentina             |   Itália ocupa 0.20% da terra
2780000               |   O país que ocupa mais área é Brasil
Itália		          |	
301230		          |
-------------------------------------------------------------
2		                |
Rússia                |  Rússia ocupa 11.48% da terra
17100000              |  Japão ocupa 0.25% da terra
Japão                 |  O país que ocupa mais área é Rússia
377975		          |			
-------------------------------------------------------------
"""
lista = []
listaMetrosPais = []
listasCon = []

quant = int(input())

for i in range(0, quant):
  entrada = input()
  entradaInt = float(input())
  mundo = float(149000000)
  multi = entradaInt * 100
  divi = multi / mundo
  lista.append(entrada)
  listaMetrosPais.append(divi)

for x, z in enumerate(lista): 
  print("{} ocupa {:.2f}% da terra".format(z, listaMetrosPais[x]))

maxi = max(listaMetrosPais)
indice = listaMetrosPais.index(maxi)


print("O país que ocupa mais área é {}".format(lista[indice]))