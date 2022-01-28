import os
from turingmachine import *

local_maquina = "mts/"
local_teste = "inputs/"

maquina = str(input("Digite o nome do arquivo da maquina (deve estar no diretorio mts/)\nEnter para usar nome padrao (mt_soma.txt):"))
teste = str(input("\nDigite o nome do arquivo de teste (deve estar no diretorio inputs/)\nEnter para usar nome padrao (ex1-soma.in):"))

if maquina == "":
    maquina = "mt_soma.txt"
print (local_maquina + maquina)
load (local_maquina + maquina)

if teste == "":
    teste = "ex1-soma.in"
print (local_teste + teste)
test (local_teste + teste)

maquina = maquina[:-4] #tira a extensao .txt

print ("\nGerando " + maquina + ".sgv")

if os.system("ruby tm_to_dot.rb mts/" + maquina+ ".txt > dots/" + maquina+ ".dot && dot -Tsvg dots/" + maquina+ ".dot -o svgs/" + maquina+ ".svg") == 0:
    print ("Graficos gerados com sucesso")
else:
    print ("Aconteceu algum problema ao gerar o .sgv, cheque se o diretorio contem as pastas '/mts' e '/dots'")