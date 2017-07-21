import time
import math

def fanta_iteration(n, from_p,tmp_p,to_p,lst1,lst2,lst3 ):
	''' iteration   fanta '''
	clockwise ={ 'from_p' : 'tmp_p' , 'tmp_p' : 'to_p', 'to_p' : 'from_p'}
	counterclockwise = { 'from_p' : 'to_p', 'to_p' : 'tmp_p' , 'tmp_p' : 'from_p' }
	clockwise_lst = { 'lst1' : 'lst2' , 'lst2' : 'lst3' , 'lst3' : 'lst1' }
	counterclockwise_lst = { 'lst1' : 'lst3' , 'lst3' : 'lst2' , 'lst2' : 'lst1' }
	for i in ( range(1 ,2**n ) ):
		m = i ^ (i-1)
		m = int( math.log(m)/math.log(2) +1)
		flag1 = 0
		flag2 = 0
		if len(lst1)>0 and lst1[-1] == m :
			print('a')
			from_plate = from_p
			from_list = lst1
			flag1 = 'from_p'
			flag2 = 'lst1'
		elif len(lst2)>0 and lst2[-1] == m :
			print('b')
			from_plate = tmp_p
			from_list = lst2
			flag1 = 'tmp_p'
			flag2 = 'lst2'
		else :
			print('c')
			from_plate = to_p
			from_list = lst3
			flag1 = 'to_p'
			flag2 = 'lst3'
		if (n+m)%2 :
			to_plate =  eval(clockwise[flag1])
			to_list =   eval(clockwise_lst[flag2] )
		else :
			to_plate = eval(counterclockwise[flag1])
			to_list =  eval(counterclockwise_lst[flag2])
		print ("plate %d : %s --> %s" %(m,from_plate,to_plate) )
		
		plate = from_list.pop()
		to_list.append(plate)
	
				


if __name__ == '__main__' :
	start = time.time()
	N = 15
	fanta_iteration( N,'X','Y','Z',range(N,0,-1),[],[] )
	end = time.time()
	print (start,end,end - start)
	
