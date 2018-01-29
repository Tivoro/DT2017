from keyManager import *
from addRoundKey import *
from subBytes import *
from rowShifter import *
from columnMixer import *
import timeit
#Encrypts each block block by: (https://en.wikipedia.org/wiki/Advanced_Encryption_Standard#High-level_description_of_the_algorithm)
# 1. Creating an expanded key
# 2. Round 0: XOR the block with a round key
# 3. Round 1-13:
#	3.1 Apply the sbox (subBytes)
#	3.2 Shift the rows (rowShifter)
#	3.3 Mix the columns (columnMixer)
#	3.4 XOR the block with a round key
# 4. Round 14
#	4.1 Apply the sbox (subBytes)
#	4.2 Shift the rows (rowShifter)
#	4.3 XOR the block with a round key

def getExpKey(key):
	return expandKey(key)

def encrypt(block,expKey):	
	#Generate exp. key (old)
	#expKey = expandKey(key)
	
	iterNum = 0
	while iterNum < len(expKey)/16:
	
		#round 0-14
		rKey = createRoundKey(expKey,iterNum)
		#round 1-14
		if iterNum > 0:
			block = subBytes(block)
			block = shiftRows(block)
			#round 1-13
			if iterNum != len(expKey)/16 - 1:
				block = mixColumns(block)
		block = addRoundKey(rKey, block)
		iterNum += 1
	return block

#Here we decrypt the block, this is the inverse of the encrypt function:
# 1. Create an expanded key
# 2. Round 0: XOR the block with a round key
# 3. Round 1-13:
#	3.1 XOR the block with a round key
#	3.2 Mix the columns (mixColumnsInv)
#	3.3 Shift the rows (shiftRowsInv)
#	3.4 Apply the sbox (subBytesInv)
# 4. Round 14:
#	4.1 XOR the block with a round key
#	4.2 Shift the rows (shiftRowsInv)
#	4.3 Apply the sbox (subBytesInv)
def decrypt(block,expKey):
	#Generate exp. key (old)
	#expKey = expandKey(key)
	
	iterNum = 14
	while iterNum >= 0:
		#round 14-0
		rKey = createRoundKey(expKey,iterNum)
		block = addRoundKey(rKey,block)
		#round 14-1
		if iterNum > 0:
			#Round 13-1
			if iterNum != len(expKey)/16 - 1:
				block = mixColumnsInv(block)
			block = shiftRowsInv(block)
			block = subBytesInv(block)
		iterNum -= 1
	return block