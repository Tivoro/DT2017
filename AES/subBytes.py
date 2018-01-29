from sbox import *
from sboxInv import *

#Substitues the values in the block with the values in sbox
def subBytes(block):
	subBlock = []
	for byte in block:
		subBlock.append(sbox[byte])
	return subBlock

#Reverses the sbox substitutions
def subBytesInv(block):
	invSubBlock = []
	for byte in block:
		invSubBlock.append(sboxInv[byte])
	return invSubBlock