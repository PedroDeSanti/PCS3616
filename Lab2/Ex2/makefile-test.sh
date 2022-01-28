# Todos os targets possiveis deste Makefile

# Comando principal que checa se existem os arquivos dependentes e gera o groceries.txt
make
#ou
make groceries.txt

# Checa se existe um arquivo fruits.txt no diretorio
make fruits.txt

# Checa se existe um arquivo vegetables.txt no diretorio
make vegetables.txt

# Imprime o arquivo groceries.txt gerado, e se nao tiver sido gerado, gera e imprime
make print

# Apaga se arquivo groceries.txt gerado
make clean

