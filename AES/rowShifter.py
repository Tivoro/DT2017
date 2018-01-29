import timeit

#Shifts the rows in the block
def shiftRows(block):
	matrix = [[],[],[],[]]
	shiftedBlock = []
	
	#Populate the matrix with the correct values
	for count in range(0, len(block)):
		row = count % 4
		matrix[row].append(block[count])
	
	#Shift the matrix rows
	matrix[1] = matrix[1][1:] + matrix[1][:1]
	matrix[2] = matrix[2][2:] + matrix[2][:2]
	matrix[3] = matrix[3][3:] + matrix[3][:3]
	
	#Join the matrix to a correct block
	# Old method
	# for count in range(0, len(block)):
		# col = int(count/4)
		# row = count % 4
		# shiftedBlock.append(matrix[row][col])
	for count in range(0, len(matrix)):
		shiftedBlock.append(matrix[0][count])
		shiftedBlock.append(matrix[1][count])
		shiftedBlock.append(matrix[2][count])
		shiftedBlock.append(matrix[3][count])
	
	return shiftedBlock

#Returns a shifted block to its original state
def shiftRowsInv(block):
	matrix = [[],[],[],[]]
	unshiftedBlock = []
	
	#Populate the matrix with the correct values
	for count in range(0, len(block)):
		row = count % 4
		matrix[row].append(block[count])
	
	#Shift the matrix rows
	matrix[1] = matrix[1][-1:] + matrix[1][:-1]
	matrix[2] = matrix[2][-2:] + matrix[2][:-2]
	matrix[3] = matrix[3][-3:] + matrix[3][:-3]
	
	#Join the matrix to a correct block
	for count in range(0, len(matrix)):
		unshiftedBlock.append(matrix[0][count])
		unshiftedBlock.append(matrix[1][count])
		unshiftedBlock.append(matrix[2][count])
		unshiftedBlock.append(matrix[3][count])
		
	return unshiftedBlock