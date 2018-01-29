from mixColTables import *

#Assigns values from the tables in mixColTables according to the specifications in https://en.wikipedia.org/wiki/Rijndael_MixColumns#MixColumns
#The values are then XORed with eachother and returned
def mixColumn(column):
	a = column
	b = [0,0,0,0]
	
	# Not sure how this works, need to delve deeper.
	# TODO: Make prettier
	b[0] = table_2[a[0]] ^ table_3[a[1]] ^ a[2] ^ a[3]
	b[1] = a[0] ^ table_2[a[1]] ^ table_3[a[2]] ^ a[3]
	b[2] = a[0] ^ a[1] ^ table_2[a[2]] ^ table_3[a[3]]
	b[3] = table_3[a[0]] ^ a[1] ^ a[2] ^ table_2[a[3]]
	
	return b

#Splits the block into smaller size 4 blocks and sends them to mixColumn
def mixColumns(block):
	mixedBlock = []
	for count in range(0,int(len(block)/4)):
		mixedCol = mixColumn(block[count*4:(count*4)+4])
		mixedBlock += mixedCol
		
	return mixedBlock

#The inverse function for mixColumn according to the specifications in https://en.wikipedia.org/wiki/Rijndael_MixColumns#MixColumns
def mixColumnInv(column):
	a = column
	b = [0,0,0,0]
	
	b[0] = table_14[a[0]] ^ table_11[a[1]] ^ table_13[a[2]] ^ table_9[a[3]]
	b[1] = table_9[a[0]] ^ table_14[a[1]] ^ table_11[a[2]] ^ table_13[a[3]]
	b[2] = table_13[a[0]] ^ table_9[a[1]] ^ table_14[a[2]] ^ table_11[a[3]]
	b[3] = table_11[a[0]] ^ table_13[a[1]] ^ table_9[a[2]] ^ table_14[a[3]]
	
	return b

#Works the same as mixColumns
def mixColumnsInv(block):
	unmixedBlock = []
	for count in range(0, int(len(block)/4)):
		unmixedCol = mixColumnInv(block[count*4:(count*4)+4])
		unmixedBlock += unmixedCol
		
	return unmixedBlock