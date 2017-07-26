import test4_3
import time

def ppdp_brute_force( lst ):
	''' probe partial digest problem'''
	min_v = min(lst)
	max_v = max(lst)
	length = len(lst)
	for x in range(1,length):
		if length/x * x != length :
			continue
		for y in  range(length/x ,0,-1  ):
			if x * y != length :
				continue
			left =  [min_v - i for i in lst]
			left = list( set(left) )
			right = list( set(lst) )
			for A in test4_3.subset(left,x) :
				for B in test4_3.subset(right,y):
					out = []
					for i in A :
						for j in B :
							out.append(j-i)
					out.sort()
					if out ==  lst :
						print(A,B)


if __name__ == '__main__':
#	ppdp_brute_force([1,2,5,6])
	start = time.time()
	ppdp_brute_force([1,2,2,3,4,5,8,9,9,10,11,12])
	end = time.time()
	print(start,end,end-start)
