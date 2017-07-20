
def find_min_max(lst):
	''' get min and max value from a list'''
	min_v = float('inf')
	max_v = float('-inf')
	n = 0
	for v in lst:
		if v < min_v : 
			min_v = v
			n += 1
		elif v > max_v : 
			max_v = v
			n += 2
		else :
			n+=2
	return(min_v,max_v,len(lst),n)

if __name__ == '__main__' :
#	print ( find_min_max.__doc__)
	lst = (1,5,4,9,3,8,7,2)
	print ( find_min_max(lst) )
