import timeit

def fibonacci(n) :
	'''caculate fibonacci sequence using constant storage space 
	'''
	def generate() :
		a , b = 1 , 1
		while 1 :
			yield a 
			a , b = b , a+b

	f = generate()
	out = 0
	for i in range(n):
		out = f.next()
	return(out)


if __name__ == "__main__":
	t = timeit.Timer( "test2_5_1.fibonacci(10)","import test2_5_1" )
	print(t.repeat(3,1000))
	
