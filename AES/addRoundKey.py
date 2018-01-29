def addRoundKey(rKey, block):
	keyBlock = []
	for n in range(0,len(rKey)):
		keyBlock.append(rKey[n] ^ block[n])
	return keyBlock