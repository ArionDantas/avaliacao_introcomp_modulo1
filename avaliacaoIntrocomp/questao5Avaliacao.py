"""
========
Problema
========

Timmy sonha em ter padrinhos mágicos que realizam seus pedidos. A sua
atividade é criar um programa que realize 3 desejos, de acordo com uma palavra mágica em cada frase digitada. Sendo assim, escreva um programa que
receba 3 entradas e que realize a operação indicada pelo comando presente
em cada uma. Vale ressaltar que cada frase apresentará apenas um comando,
ou seja, uma palavra mágica. O programa deve conter uma função para cada
desejo (comando) de Timmy.
Os três comandos possíveis são:
• Trocar os espaços de uma frase por traços (-), ativado pela palavra
“traços”;
• Converter todas as letras da frase em maiúsculas, ativado pela palavra “maiúsculo”;
• Converter todas as letras da frase em minúsculas, ativado pela palavra “minúsculo”;
Observação 1: a palavra mágica na frase poderá estar escrita com letras
maiúsculas e minúsculas.
Observação 2: caso a frase digitada não apresente nenhum comando, o seu
programa deverá imprimí-la sem alterações


Casos de Teste
Lembre-se que as entradas e saídas devem ser idênticas às dos casos de teste.
-----------------------------------------------------------------------------------------------------
Exemplo de Entrada                            |  Entrada Exemplo de Saida
----------------------------------------------|-------------------------------------------------------
sempre quis ser maiúsculo SEMPRE              |  QUIS SER MAIÚSCULO
----------------------------------------------|-------------------------------------------------------
as vezes eu queria ser o Michael Jackson      |  as vezes eu queria ser o Michael Jackson
----------------------------------------------|-------------------------------------------------------
eu queria ser o Michael maiúsculo Jackson     |  EU QUERIA SER O MICHAEL MAIÚSCULO JACKSON
----------------------------------------------|-------------------------------------------------------
Eu desejo trocar todos os espaços por trAÇOS  |  Eu-desejo-trocar-todos-os-espaços-por-trAÇOS
----------------------------------------------|-------------------------------------------------------
meu desejo é tornar tudo MAIÚSCULO            |  MEU DESEJO É TORNAR TUDO MAIÚSCULO
----------------------------------------------|-------------------------------------------------------
espaços virem TRAços imediatamente            |  espaços-virem-TRAços-imediatamente
----------------------------------------------|-------------------------------------------------------
"""
def desejo(frase):
  comando1 = "traços"
  comando2 = "maiúsculo"
  comando3 = "minúsculo"

  fraseLower = frase.lower()

  if comando1 in fraseLower:
    print("-".join(frase.split(" ")))
  elif comando2 in fraseLower:
    print(frase.upper())
  elif comando3 in fraseLower:
    print(frase.lower())
  else:
    print(frase)


for i in range(1, 4):
  frase = input()
  desejo(frase)