from sbox import *
from rcon import *

#Here we generate a 256-bit expanded key.
#This module works according to https://en.wikipedia.org/wiki/Rijndael_key_schedule#Key_schedule_description

#Rotates and applies sbox and rcon the the key
def keyScheduleCore(word, iterNum):
	#rotate 8-bits left
	word = word[1:] + word[:1]
	#Apply sbox and rcon
	word[0] = sbox[word[0]] ^ rcon[iterNum]
	word[1] = sbox[word[1]]
	word[2] = sbox[word[2]]
	word[3] = sbox[word[3]]
	return word

#Generator function
def expandKey(n):
	b = n[:] #Clones the key
	i = 1
	
	while len(b) < 240:
		#Generate 4-bytes of expKey
		t = keyScheduleCore(b[-4:],i)
		i += 1
		for x in range(0,4):
			t[x] = t[x] ^ b[len(b) - len(n) + x]
		b += t
		
		#Generate 12-bytes of expKey
		for x in range(0,3):
			t = b[-4:]
			for y in range(0,4):
				t[y] = t[y] ^ b[(len(b) - len(n)) + y]
			b += t
			
		#Generate 4-bytes if 256-bit key
		t = b[-4:]
		for x in range(0,4):
			t[x] = sbox[t[x]]
			t[x] = t[x] ^ b[len(b) - len(n) + x]
		b += t
		
		#Generate 8-bytes if 192 and 12-bytes if 256
		for x in range(0,3):
			t = b[-4:]
			for y in range(0,4):
				t[y] = t[y] ^ b[len(b) - len(n) + y]
			b += t
	#I generate a key lenght of 256 bytes, so we must trim it.
	return b[0:240]
	
#Returns 16-bit sub keys from the expanded key
def createRoundKey(expKey, rNum):
	return expKey[rNum*16:(rNum+1)*16]