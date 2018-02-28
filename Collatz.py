#checked iterations 4mil-5mil in <3.36 seconds (minus whatever my reaction time is... not effective way need to add timing)
#checked iterations 20mil - 30mil in <29.51 seconds
try:
	f = open('CMax.txt', 'r')
	CMax = int(f.read())
	f.close()
except FileNotFoundError:
	print("ERROR: CMax file not found, starting from 0")
	CMax = 0

k = int(input("Current largest number found: %s\nEnter how many additional numbers you want to test (in millions): " % CMax)) * 1000000
#if num drops below max, all numbers below max have
#already been confirmed as reducing to 4 (found to pass the Collatz Conjecture
#(Therefore the program only needs to store 1 number: the higest tested number, CMax)

#checks the next k million numbers	
for j in range(0,k):
	CTest = CMax + 1
	
	if CTest <= 4:
		CMax+=1
		continue
	
	while (CTest > CMax):	#if this is an infinite loop, we've solved the problem!
		#print("CMax: {0}, CTest {1}".format(CMax, CTest))
		if (CTest % 2 == 0):	#even
			CTest = CTest / 2
		else:
			CTest = (CTest * 3 + 1) / 2		#odd
			
	CMax+=1
	
f = open('CMax.txt', 'w')
f.write(str(CMax))
f.close

print("Finished! Numbers up to %s all trace back to 4!" % CMax)