#open("caminho","r")

# Mode
# r - Leitura
# a - Append / Incrementar
# w - Escrita
# x - Criar arquivo
# r+ - Leitura + Escrita

arquivo = open('text.txt','w')

arquivo.write('Ola Mundo')

arquivo.close()

print('Hello World')

