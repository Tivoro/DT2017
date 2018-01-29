import AES256
import time
from readBlockFile import *
from readKeyFile import *

startExec = time.time()
#Read blocks and key from files
print("-- Reading plaintext --")
start = time.time()
blocks = getBlocks("tWotW.txt")
key = getKey("testKey")
encBlocks = []
readPlainTime = time.time() - start

## Encrypt
print("-- Encrypting --")
start = time.time()
expKey = AES256.getExpKey(key)
for block in blocks:
	#Add filler bytes in the last block
	while len(block) != 16:
		block.append(0)
	encBlocks.append(AES256.encrypt(block, expKey))
encTime = time.time() - start
	
#The real MVP: https://stackoverflow.com/questions/17349918/python-write-string-of-bytes-to-file
## Write encrypted data to file
print("-- Writing encrypted data to file --")
start = time.time()
with open("encFile", 'wb') as file:
	for eBlock in encBlocks:
		file.write(bytearray(eBlock))
	file.close()
writeEncTime = time.time() - start

## Read encrypted file	
print("-- Reading encrypted file --")
start = time.time()
blocks = getBlocks("encFile")
decBlocks = []
readEncTime = time.time() - start

## Decrypt
print("-- Decrypting --")
start = time.time()
expKey = AES256.getExpKey(key)
for block in blocks:
	decBlocks.append(AES256.decrypt(block, expKey))

## Clean filler bytes in last block
for count in range(15,-1,-1):
	if decBlocks[len(decBlocks)-1][count] == 0:
		decBlocks[len(decBlocks)-1].pop(count)
	else:
		break
decTime = time.time() - start
		
## Write decrypted data to file
start = time.time()
with open("decFile", 'wb') as file:
	for dBlock in decBlocks:
		file.write(bytearray(dBlock))
	file.close()
writeDecTime = time.time() - start
execTime = time.time() - startExec

#https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
print("Total execution time: %s seconds"  % (execTime))
print("Read plaintext time: %s seconds\nWrite encrypted time: %s seconds\nRead encrypted time: %s seconds\nWrite decrypted time: %s seconds" % (readPlainTime, writeEncTime, readEncTime, writeDecTime))
print("Encryption time: %s seconds\nDecryption time: %s seconds" % (encTime, decTime))