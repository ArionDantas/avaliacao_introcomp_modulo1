"""
========
Problema
========

Suponha que daqui a algum tempo, o chefe de uma grande empresa de segurança está precisando de pessoas para trabalharem no seu negócio e abriu
vaga para novos programadores. Entre os candidatos está você, que, como
jáfez o Introcomp, se deu melhor que os outros concorrentes no processo e ganhou a vaga! Para sua primeira tarefa, foi designado que fizesse um sistema
de controle da senha de um cofre, em python, com as seguintes especificações:
Depois de o programa receber a senha do cofre (composta por letras e/ou números) de um banco de dados, ele espera a entrada de uma tentativa. Caso a
tentativa esteja correta, é impresso na tela “Acesso permitido!” e o programa
é finalizado. Caso a tentativa esteja incorreta, é impresso na tela “Senha inválida!”, e uma nova entrada é esperada. Se o usuário digitar a senha errada
três vezes seguidas, deve-se aparecer a mensagem “ERRO: muitas tentativas
inválidas!” e o programa é finalizado.
Obs1.:Considere que a senha seja a primeira coisa lida pelo programa eque
venha, assim como as tentativas, da entrada padrão (teclado) e não de um
banco de dados.
Obs2.: Trate letras minúsculas e maiúsculas como iguais.


Working
Casos de Teste

Lembre-se que as entradas e saídas devem ser idênticas às dos casos de teste.
--------------------------------------------------------------
Exemplo de Entrada       |  Exemplo de Saida
--------------------------------------------------------------
abcd			             |
ABCD                     |  Acesso permitido!
--------------------------------------------------------------
shaulin_matador_de_porco |
123joao456               |  Senha inválida!
senha!!                  |  Senha inválida!
shaulin_matador_de_porco |  Acesso permitido!
--------------------------------------------------------------
SenhaMaisLinda@          |
76544 Senha              |  inválida!
aniversario              |  Senha inválida!
sandy&junior             |  ERRO: muitas tentativas inválidas!
--------------------------------------------------------------
"""
maxTentativas = 3
senha = input()
senhaPadrao = senha.lower()

#  or senhaVerificacao == senhaUpper or senhaVerificacao == senhaLower
for i in range(1, (maxTentativas +1)):
  senhaVerificacao = input()
  senhaVerificacaoPadrao = senhaVerificacao.lower()

  senhaComplemento = senhaVerificacao.upper()

  if senhaVerificacaoPadrao == senhaPadrao:
    print("Acesso permitido!")
    break
  elif i == 3:
    print("ERRO: muitas tentativas inválidas!")
    break
  elif senhaVerificacao != senhaPadrao:
    print("Senha inválida!")



