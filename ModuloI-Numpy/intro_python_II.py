###############################################################################
### JEST - Junior Enterprise for Science and Technology #######################
###############################################################################
### Workshop de Python - Python Introduction II ###############################
### Import and data manipulation using pandas and NumPy packages ##############
###############################################################################

# Import the NumPy package
import numpy as np
# Import the pandas package
import pandas as pd

## Data manipulation
# List creation
list1 = [6, 4, -1, 12]
list2 = [2, -3, 10, 0]

# Join two lists into one
list_merge = list1 + list2
print('\nJoin the two lists into one: ', list_merge)

# In Python, the first ellement of a list corresponds to the index 0
print('\nFirst element of the list1 (index 0): ', list1[0])

# Select only some ellements from the list
# Prints the value of the index 1 to the index 3, but index 3 is not included
print('\nValues of list1 between indexes 1 and 2', list1[1:3])

# Sum of the values inside a list
print('\nSum of list1: ', sum(list1))

####################################
######### Problem 1 ################
####################################
# - Doing sums on Python only concatenates the two list. Create a function that sums the elements from two lists one by one.

## Data Manipulation using NumPy
# Change a list to a NumPy Array - np.array()
np_list1 = np.array(list1)
np_list2 = np.array(list2)

# Mathematical operations in NumPy don't work with 'traditional' lists
# Sum of two vectors
np_sum = np_list1 + np_list2
print('\nlist1 + list2 = ', np_sum)

# Subtraction of two vectors
np_sub = np_list1 - np_list2
print('\nlist1 - list2 = ', np_sub)

# Multiplication of two vectors (Different from the algebraic multiplication of two vectors!)
np_mult = np_list1 * np_list2 # Multiplies element by element
print('\nlist1 * list2 = ', np_mult)

# Division of two vectos
np_div = np_list1 / np_list2
print('\nlist1 / list2 = ', np_div)

# Power of list elements
np_list1_square = np_list1 ** 2
print('\nTo the power of 2 = ', np_list1_square)
np_list1_cube = np_list1 ** 3
print('\nTo the power of 3 = ', np_list1_cube)


# Statistical Analysis
print('\nMean: ', np.mean(list1))
print('\nStandart Deviation: ', np.std(list1))
print('\nMedian: ', np.median(list1))
print('\nCorrelation Coeficient between list1 and list2:\n', np.corrcoef(list1,list2))

####################################
######### Problem 2 ################
####################################
#Create a function that acepts a list as an argument and that calculates the mean, median, standart deviation and returns the values nicely presented

##Matrices
np_matrix = np.array([[1.73, 1.68, 1.71, 1.89, 1.79],
                      [65.4, 59.2, 63.6, 88.4, 68.7]])
print('\Matrix:\n', np_matrix)

# Size of the matrix
print('\nSize of the matrix: ', np_matrix.shape, ' - two lines, five columns')

# Access different elements inside the matrix
print('\nFirst line: ', np_matrix[0])
print('\n1. Element in the first line, third column:', np_matrix[0][2])
print('\n2. The same element but accessed in a different way:', np_matrix[0,2]) # Semelhante ao comando anterior
print('\nAll the lines, columns one to three:\n', np_matrix[:,1:4])
print('\nLinha 1, All the columns: ', np_matrix[1,:],'\n')

# Change an element inside a matrix
np_matrix[1,3] = 75.9
print(np_matrix)

## Create random data (np.random)
# Creates 50 values that follow a normal rule with the mean 1.74 and standart deviation .20
height = np.random.normal(1.75, 0.20, 50)
height = np.round(height, 2)

# Creates 50 values that follow a normal rule with the mean 60.32 and standart deviation 15
weight = np.round(np.random.normal(60.32, 15, 50),2)


# Join two arrays in a table
data = np.column_stack((height, weight))
print('\nJunta os arrays com dados aleatórios\n', data)

####################################
######### Problem 3 ################
####################################
# - Create a function that calculates the BMMI. To create the values for weight and height use the lines given previously.

## Import data from files

# Read a text file
filename = 'sales_comma.txt'
file = open(filename, mode = 'r') # opens the file for reading - 'r' (read)
text = file.read()
file.close() # closes the file

# Check if the file is closed
print('\nFicheiro fechado? ', file.closed)

filename = 'sales_comma.txt'
file = open(filename, mode = 'r')
print('\nPrimeira linha\n', file.readline()) # Reads the first line of the file
print('\nSegunda linha\n', file.readline()) # reads the second line of the file, and so on
file.close()

# Write a file
filename_write = 'teste.txt'
file = open(filename_write, mode = 'w') # opens the file for writing - 'w' (write)
file.write('\tEscrita em ficheiros \n\n')
file.write(text) # Writes the text in the new file
file.close()

###############################################################################
## Import files using pandas

filename = 'elections.csv'

# Reads the file .csv - df_elections will be a DataFrame object
df_elections = pd.read_csv(filename)

# Converts the DataFrame to a NumPy array (useufull to manipulate data with the
#functions from this package)
df_electionsNP = df_elections.values

# Only show the first five lines of the table
print('\nPrimeiras cinco linhas:\n\n', df_elections.head())

# nrows = 10 : shows the first 10 lines
df_elections10 = pd.read_csv(filename, nrows = 10)
print('\nPrimeiras dez linhas:\n\n', df_elections10)

####################################
######### Problem 4 ################
####################################
# - Create a program that opens df_elections and counts the number of times that Hillary Clinton is named

# read files that are not csv type and have different 
# separators (for example, commas or tabs)
filename_comma = 'sales_comma.txt'
filename_tab = 'sales_tab.txt'

df_salesComma = pd.read_table(filename_comma, sep = ',', index_col = 'month')
df_salesTab = pd.read_table(filename_tab, sep = '\t', index_col = 'month')

## Data manipulation using pandas
# indexation of DataFrames
df = pd.read_csv('sales.csv', index_col = 'month')
print('\nDataFrame sales\n\n', df)

# Access elements in the table

# This way, we must first call the label of the column and after the label of
# the line
print('\n1. (Jan,salt):', df['salt']['Jan'])

# Similar to the previous command
print('\n2. (Jan,salt):', df.salt['Jan'])

# iloc: access from the position in the table
# loc: access through the labels. In both cases we should use [line, column]
print('\n3. (Jan,salt):', df.iloc[0,1])
print('\n4. (Jan,salt):', df.loc['Jan','salt'])

####################################
######### Problem 5 ################
####################################
# - Do the mean of the shopping values for each month. If in one of those appears a null value, remove that line.

# Show only some columns in the desired order
print('\nColumns salt and eggs:\n\n', df[['salt','eggs']])

# Show all the lines (:) and only some columns (Ex: a:d)
print(df.loc[:,'eggs':'salt'])
print(df.iloc[:,0:2]) # Inclues columns 0 and 1.

# Show all the columns (:) and just some lines (Ex: a:d)
print(df.loc['Jan':'Apr',:])
print(df.iloc[1:4,:]) # Show lines 1, 2 and 3.

# Invert the order of the lines from a to b: df.loc['b':'a':-1]
print(df.loc['Jun':'Mar':-1])

# Filter the data
# Returns a boolean for each condition
print('\nNumber of eggs equal or superior of 132 (True ou False)\n', df.eggs >= 132)

# Mostra as linhas que satisfazem aquela condição
print('\nLLines that satisfy the condition >= 132\n', df[df.eggs >= 132])

# Combine filters: & - intersection (e); | - reunion (ou)
print(df[(df.salt >= 50) & (df.eggs < 200)])
print(df[(df.salt >= 50) | (df.eggs < 200)])

# Create a new list with the label 'bacon'
df['bacon'] = [0, 0, 50, 60, 70, 80]
print(df)

# Select the columns with NaN's
print(df.loc[:,df.isnull().any()])

# Excludes the columns with NaN's
print(df.loc[:,df.notnull().all()])

# Excludes the lines with NaN's
print(df.dropna(how = 'any'))

# Considers the values 20 and 47 as NaN - na_values = []
data = pd.read_csv('sales.csv', index_col = 'month', sep = ',', na_values = [20, 47])
print('\nDataFrame with 20 and 47 as NaN\n',data)

# Mathematical operations with digits
df.eggs += 5 # Sums 5 to all values in the columns 'eggs'
df.apples *= 2 # Multiplies all values in the columns 'apples' by 2

df.eggs -= 5 # Subtracts 5 to all values in column 'eggs'
df.apples /= 2 # divides by 2 all the values in the column 'apples'

df.eggs[df.salt > 55] += 10 # sums 10 to all values in the column 'eggs' in
                            # the lines that satisfy the condition

#  Change the labels
df.columns = ['eggs','sugar','pears','bacon']

# Changes all the values indexed to the label ('month') to
# strings with uppercase
df.index = df.index.str.upper()

# Changes all the values indexed to the label ('month') to
# strings with lowercase
df.index = df.index.map(str.lower)

# In the columns in which the values are strings, we can apply the previous
# commands. For example, in the elections dataset from the USA:
df_elections.state = df_elections.state.str.upper()
print(df_elections)

####################################
######### Problem 6 ################
####################################
# - Open the Titanic dataset and create a program that calculates:
# - the average value of the age of the people in the Titanic
# - % of men who survived the disaster
# - % of women who survived the disaster