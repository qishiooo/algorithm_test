import test4_3
import time

def ppdp( lst ):
	''' another probe partial digest problem solution '''
	max_v = max(lst)
	min_v = min(lst)
	length = len(lst)
	lst.remove(min_v)
	A = [0]
	B = [min_v]
	place(lst,A,B,min_v)
	
def A_in_B (A,B):
	a = list(A)
	b =list(B)
	if len(a) == 0 :
		return(True,B)
	for i in a :
		if b.count(i) == 0 :
			return(False,B) 
		b.remove(i)
	return (True,b)

def place(lst,A ,B,min_v):
	if len(lst) == 0 :
		print(sorted(A),sorted(B) )
		return 
	min_dist = min(lst)
	lst.remove(min_dist)
	v1 = min_v - min_dist
	dist1 = [ B[i] - v1 for i in range(1,len(B)) ]
	(flag1,lst1) = A_in_B( dist1, lst )
	if v1 not in A and flag1 :
		A.append(v1)
		place(lst1,A,B,min_v)
		A.pop()
	v2 = min_dist
	dist2 = [ v2 - A[i] for i in range(1,len(A)) ]
	(flag2,lst2) = A_in_B( dist2 ,lst )
	if v2 not in B and flag2 :
		B.append(v2)
		place(lst2,A,B,min_v)
		B.pop()
	return
	

	
if __name__ == '__main__':
	start =time.time()
	ppdp([1,2,2,3,4,5,8,9,9,10,11,12])
	end = time.time()
	print(start,end,end-start)
