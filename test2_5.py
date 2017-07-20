
def fibonacci(n) :
	'''caculate fibonacci sequence using constant storage space 
	'''
	if n==1 or n==2 :
		return 1 
	(first,second,third)=(1,1,0)
	for i in range(3,n+1):
		third = first + second
		(first,second)=(second,third)
	return third

if __name__ == "__main__":
	print(__doc__)
	
	
