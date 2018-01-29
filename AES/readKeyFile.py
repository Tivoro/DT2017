#Reads the encryption key from a file.
def getKey(filename):
	keyDec = []
	with open(filename, 'rb') as file:
		byte = file.read(2)
		while byte:
			keyDec.append(int(byte,16))
			byte = file.read(2)	
	return keyDec