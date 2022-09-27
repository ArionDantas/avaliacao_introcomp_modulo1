"""
========
Problema
========

Faltam 3 dias para as férias da Milla acabarem e ela quer aproveitar para
ler alguns livros. Ela consegue ler cerca de 300 pa´ginas por dia e quer saber
se vai conseguir terminar os livros que escolheu. Seu programa deve receber
como entrada 3 números inteiros que representam a quantidade de pa´ginas
de cada livro que foi escolhido, e como saída deve informar a quantidade de
livros que ela conseguirá ler até o final das férias.

Casos de Teste

Lembre-se que as entradas e saídas devem ser idênticas às dos casos de teste.
----------------------------------------------------------------
Exemplo de Entrada   |  Exemplo de Saida
----------------------------------------------------------------
352		            |
221                  |  Milla irá conseguir ler todos os livros!
247		            |
----------------------------------------------------------------
951		            |
540                  |  Milla irá conseguir ler dois livros!
229		            |
----------------------------------------------------------------
967		            |
1612                 |  Milla não conseguirá ler nenhum livro :(
1250		            |		
----------------------------------------------------------------
750		            |
964                  |  Milla irá conserguir ler um livro!
821		            |
----------------------------------------------------------------
"""
def removeLista(num):
  if num > limitePaginas:
    listaLivros

#variaveis
limitePaginas = 900
listaLivros = []

livro1 = int(input())
livro2 = int(input())
livro3 = int(input())

listaLivros.append(livro1)
listaLivros.append(livro2)
listaLivros.append(livro3)

if listaLivros[0] + listaLivros[1] + listaLivros[2] > limitePaginas:
  listaLivros.remove(max(listaLivros))

  if listaLivros[0] + listaLivros[1] > limitePaginas:
    listaLivros.remove(max(listaLivros))

    if listaLivros[0] > limitePaginas:
      listaLivros.remove(listaLivros[0])

if len(listaLivros) == 0:
  print("Milla não conseguirá ler nenhum livro :(")
elif len(listaLivros) == 3:
  print("Milla irá conseguir ler todos os livros!")
elif len(listaLivros) == 2:
  print("Milla irá conseguir ler dois livros!")
elif len(listaLivros) == 1:
  print("Milla irá conseguir ler um livro!")