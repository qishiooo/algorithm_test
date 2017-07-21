import time
import math

def fanta_iteration(n, from_p,tmp_p,to_p,lst1,lst2,lst3 ):
	''' iteration   fanta '''
	
	clockwise ={
	for i in ( range(1 ,2**n ):
		m = i ^ (i-1)
		m =  math.log(m)/math.log(2) +1
		if lst1[-1] == m :
			from_plate = from_p
			from_list = lst1
		elif lst2[-1] == m :
			from_plate = tmp_p
			from_list = lst2
		else :
			from_plate = to_p
			from_list = lst3
		if (n+m)%2 :
			to_plate =  
			to_list =
		else :
			to_plate =
			to_list =
		print ("plate %d : %s --> %s" %(m,from_plate,to_plate) )
		plate = from_plate.pop()
		to_list.append(plate)
	
				


if __name__ == '__main__' :
	start = time.time()
	N = 2
	fanta_recursive( N,'X','Y','Z',[1:N+1],[],[] )
	end = time.time()
	print (start,end,end - start)
	
