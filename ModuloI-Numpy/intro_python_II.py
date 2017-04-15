###############################################################################
### JEST - Junior Enterprise for Science and Technology #######################
###############################################################################
### Workshop de Python - Introdução ao Python II ############################## 
### Importação e manipulação de dados usando os packages NumPy e pandas #######
###############################################################################

# Importar o package NumPy
import numpy as np
# Importar o package pandas
import pandas as pd

## Manipulação de dados
# Cria listas
list1 = [6, 4, -1, 12]
list2 = [2, -3, 10, 0]

# Juntar duas listas numa
list_merge = list1 + list2
print('\nJuntar duas listas numa: ', list_merge)

# Em Python, o primeiro elemento de uma lista corresponde ao índice 0
print('\nPrimeiro elemento de list1 (índice 0): ', list1[0])

# Selecionar alguns elementos da lista
# Imprime o valor do índice 1 até ao 3 exclusive!
print('\nValores de list1 entre os índices 1 e 2', list1[1:3]) 

# Soma dos valores de uma lista
print('\nSoma de list1: ', sum(list1))

## Manipulação de dados usando o NumPy
# Converte uma lista para um NumPy array - np.array()
np_list1 = np.array(list1)
np_list2 = np.array(list2)

# Tamanho de list1
print('\nTamanho de list1: ', np_list1.shape)

# Operações matemáticas com NumPy arrays que não seriam possíveis com listas "tradicionais"
# Soma de dois vetores
np_sum = np_list1 + np_list2 
print('\nlist1 + list2 = ', np_sum)

# Subtração de dois vetores
np_sub = np_list1 - np_list2 
print('\nlist1 - list2 = ', np_sub)

# Multiplicação de dois vetores (Diferente da multiplicação algébrica de vetores!)
np_mult = np_list1 * np_list2 # Multiplica elemento a elemento
print('\nlist1 * list2 = ', np_mult)

# Divisão de dois vetores
np_div = np_list1 / np_list2 
print('\nlist1 / list2 = ', np_div)

# Potência dos elementos das listas
np_list1_square = np_list1 ** 2
print('\nElevar a 2 = ', np_list1_square)
np_list1_cube = np_list1 ** 3
print('\nElevar a 3 = ', np_list1_cube)

# Análise estatística
print('\nMédia: ', np.mean(list1))
print('\nDesvio padrão: ', np.std(list1))
print('\nMediana: ', np.median(list1))
print('\nCorrelação entre list1 e list2:\n', np.corrcoef(list1,list2))

# Matrizes
np_matrix = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                      [65.4, 59.2, 63.6, 88.4, 68.7]])
print('\nMatriz:\n', np_matrix)

# Tamanho da matriz
print('\nTamanho da matriz: ', np_matrix.shape, ' - duas linhas, cinco colunas')

# Acessar os diferentes elementos da matriz
print('\nPrimeira coluna: ', np_matrix[0])
print('\n1. Elemento (0,2):', np_matrix[0][2])
print('\n2. Elemento (0,2):', np_matrix[0,2]) # Semelhante ao comando anterior
print('\nTodas as linhas, colunas 1 a 3:\n', np_matrix[:,1:4])
print('\nLinha 1, todas as colunas: ', np_matrix[1,:])

# Alterar um elemento da matriz
np_matrix[1,3] = 75.9
print(np_matrix)

## Gerar dados aleatórios (np.random)
# Gera 50 exemplos de acordo com a lei normal com média 1.75 e desvio padrão 0,20
height = np.round(np.random.normal(1.75, 0.20, 50),2)

# Gera 50 exemplos de acordo com a lei normal com média 60.32 e desvio padrão 15
weight = np.round(np.random.normal(60.32, 15, 50),2)

# Juntar os dois arrays anteriores numa tabela
data = np.column_stack((height, weight))
print('\nJunta os arrays com dados aleatórios\n', data)

###############################################################################

## Importar dados de ficheiros
# Mostrar os ficheiros que estão na diretoria - ls

# Ler um ficheiro de texto
filename = 'sales_comma.txt'
file = open(filename, mode = 'r') # Abre o ficheiro para leitura - 'r' (read)
text = file.read()
file.close() # Fechar o ficheiro 

# Verificar se o ficheiro está fechado
print('\nFicheiro fechado? ', file.closed)

filename = 'sales_comma.txt'
file = open(filename, mode = 'r')
print('\nPrimeira linha\n', file.readline()) # Lê a primeira linha do ficheiro
print('\nSegunda linha\n', file.readline()) # Lê a segunda linha do ficheiro, e assim sucessivamente
file.close()

# Escrever num ficheiro
filename_write = 'teste.txt'
file = open(filename_write, mode = 'w') # Abre o ficheiro para escrita - 'w' (write)
file.write('\tEscrita em ficheiros \n\n')
file.write(text) # Escreve no novo ficheiro o texto lido no ficheiro 
                 # sales_comma.txt - text
file.close()

###############################################################################
## Importar ficheiros usando o pandas

filename = 'elections.csv'

# Lê um ficheiro .csv - df_elections será do tipo DataFrame
df_elections = pd.read_csv(filename)

# Converte um DataFrame para um NumPy array (útil para as manipulações através 
# das funções deste package)
df_electionsNP = df_elections.values

# Mostrar apenas as primeiras cinco linhas da tabela
print('\nPrimeiras cinco linhas:\n\n', df_elections.head())

# nrows = 2 : Lê as primeiras dez linhas
df_elections10 = pd.read_csv(filename, nrows = 10)
print('\nPrimeiras dez linhas:\n\n', df_elections10)

# Leitura a partir de ficheiros que não sejam do tipo csv e com diferentes 
# separadores (por exemplo, vírgula e tabulação)
filename_comma = 'sales_comma.txt'
filename_tab = 'sales_tab.txt'

df_salesComma = pd.read_table(filename_comma, sep = ',', index_col = 'month')
df_salesTab = pd.read_table(filename_tab, sep = '\t', index_col = 'month')

## Manipulação de dados usando o pandas
# Indexação de DataFrames
df = pd.read_csv('sales.csv', index_col = 'month')
print('\nDataFrame sales\n\n', df)

# Acessar os elementos da tabela

# Desta forma, deve inserir-se primeiro o label da coluna e só depois o label 
# da linha
print('\n1. (Jan,salt):', df['salt']['Jan'])

# Semelhante ao comando anterior
print('\n2. (Jan,salt):', df.salt['Jan']) 

# iloc: acessar a partir da posição na tabela
# loc: acessar a partir dos labels. Em ambos os casos será [linha,coluna]
print('\n3. (Jan,salt):', df.iloc[0,1])
print('\n4. (Jan,salt):', df.loc['Jan','salt'])

# Apresentar apenas algumas colunas na ordem desejada
print('\nColunas salt e eggs:\n\n', df[['salt','eggs']])

# Apresentar todas as linhas (:) e apenas algumas colunas (Ex: a:d)
print(df.loc[:,'eggs':'salt'])
print(df.iloc[:,0:2]) # Inclui as colunas 0 até 2 exclusive!

# Apresentar todas as colunas (:) e apenas algumas linhas (Ex: a:d)
print(df.loc['Jan':'Apr',:])
print(df.iloc[1:4,:]) # Inclui as linhas 1 até 4 exclusive!

# Inverter a ordem das linhas de a até b: df.loc['b':'a':-1]
print(df.loc['Jun':'Mar':-1])

# Filtrar os dados
# Devolve um boolean para cada condição
print('\nNúmero de ovos maior ou igual a 132 (True ou False)\n', df.eggs >= 132)

# Mostra as linhas que satisfazem aquela condição
print('\nLinhas que satisfazem a condição eggs >= 132\n', df[df.eggs >= 132])

# Combinar filtros: & - interseção (e); | - união (ou)
print(df[(df.salt >= 50) & (df.eggs < 200)])
print(df[(df.salt >= 50) | (df.eggs < 200)])

# Criar uma nova coluna com label 'bacon'
df['bacon'] = [0, 0, 50, 60, 70, 80]
print(df)

# Seleciona as colunas com NaN's
print(df.loc[:,df.isnull().any()])

# Exclui as colunas com NaN's
print(df.loc[:,df.notnull().all()])

# Exclui as linhas com NaN's
print(df.dropna(how = 'any')) 

# Trata, por exemplo, os valores 20 e 47 como um NaN - na_values = []
data = pd.read_csv('sales.csv', index_col = 'month', sep = ',', na_values = [20, 47])
print('\nDataFrame que considera os valores 20 e 47 como NaN\n',data)

# Operações matemáticas com dígitos
df.eggs += 5 # Soma 5 a todos os valores da coluna 'eggs'
df.apples *= 2 # Multiplica por 2 todos os valores da coluna 'apples'

df.eggs -= 5 # Subtrai 5 a todos os valores da coluna 'eggs'
df.apples /= 2 # Divide por 2 todos os valores da coluna 'apples'

df.eggs[df.salt > 55] += 10 # Soma 10 a todos os valores da coluna 'eggs' cujas
                            # linhas satisfazem aquela condição 

# Alterar os labels
df.columns = ['eggs','sugar','pears','bacon']

# Transforma todos os labels correspondentes à variável indexada ('month') para
# strings com maiúsculas
df.index = df.index.str.upper()

# Transforma todos os labels correspondentes à variável indexada ('month') para
# strings com minúsculas
df.index = df.index.map(str.lower)

# No caso de colunas cujos valores são do tipo string, podemos aplicar os 
# comandos anteriores. Por exemplo, no caso da tabela das eleições dos USA:
df_elections.state = df_elections.state.str.upper() 
print(df_elections)

