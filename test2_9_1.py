import time

def fanta_recursive(n, from_p,tmp_p,to_p ):
	''' recursive  fanta '''
	if n == 1 :
		print("%s --> %s" %(from_p , to_p) )
		return
	else :
		fanta_recursive(n-1 , from_p , to_p , tmp_p)
		print("%s --> %s" %(from_p, to_p) )
		fanta_recursive(n-1 , tmp_p , from_p, to_p) 


if __name__ == '__main__' :
	start = time.time()
	fanta_recursive(15,'X','Y','Z')
	end = time.time()
	print (start,end,end - start)
	
