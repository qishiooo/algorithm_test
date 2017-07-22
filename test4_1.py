
def  multiple_set(lst):
	''' caculate multiple set from a list'''
	length = len(lst)
	multiple=[]
	for i in range(0,length):
		for j in range(i+1,length):
			multiple.append(lst[j]-lst[i])
	multiple.sort()
	return multiple


if __name__ == '__main__' :
	print( multiple_set([0,2,4,7,10] ))
	