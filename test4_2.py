import math
import itertools
import test4_1

def pdp(lst):
	''' partial digest problem'''
	l= len(lst)
	n = int((1+ math.sqrt(1+8*l))/2)
	max_v = max(lst)
	uniq = {}.fromkeys(lst).keys()
	uniq.remove(max_v)
#itertools.permutations, itertools.combinations
	for x in itertools.combinations(uniq,n-2):
		x = list(x)
		x.extend([0,max_v])
		x.sort()
		y = test4_1.multiple_set(x)
#		print("%s\t%s" %(x,y)  )
		if lst == y :
			print(x)

if __name__ == "__main__":
	pdp([1,1,1,2,2,3,3,3,4,4,5,5,6,6,6,9,9,10,11,12,15])
