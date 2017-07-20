
def get_missing_num (lst,n):
	''' get one missing num in 1 .. n'''
	arr = range(1,n+1)
	for i in lst :
		arr.remove(i)
	return arr[0]


if __name__ == '__main__' :
	lst = (1,5,4,3)
	n = len(lst) +1
	print( get_missing_num(lst,n) )
