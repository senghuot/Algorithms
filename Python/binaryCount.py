def countBinary(num):
	if num == 0: return 0
	return num%2 + countBinary(num/2)

def arrayCount(num):
	for i in range(0, num+1):
		print i, "=", countBinary(i)
	
arrayCount(10)
assert(countBinary(3) == 2)
