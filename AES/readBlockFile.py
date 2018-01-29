#Reads byte data from a file and puts it into a list.
#For the hex-file "testBlock"
def getBlock(filename):
	blockDec = []
	with open(filename, 'rb') as file:
		byte = file.read(2);
		while byte:
			blockDec.append(int(byte,16))
			byte = file.read(2)
	return blockDec

#For regular plaintext files
def getBlocks(filename):
	fileAsBlocks = []
	with open(filename, 'rb') as file:
		plainBlock = file.read(16)
		while plainBlock:
			fileAsBlocks.append(list(plainBlock))
			plainBlock = file.read(16)
	return fileAsBlocks