import time

def fibonacci() :
	'''caculate fibonacci sequence using constant storage space 
	'''
	a , b = 1 , 1
	while 1 :
		yield a 
		a , b = b , a+b

if __name__ == "__main__":
	print(__doc__)
	start = time.time()
	f = fibonacci()
	out = 0
	for n in range(10) :
		out = f.next()
	print(out)
	end = time.time()
	print(start,end,end-start)
	
	
