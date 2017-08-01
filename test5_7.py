import test5_4

def CircleSort (lst):
	''' greed circle sort '''
	v = lst.index(min(lst) )
	a = list(  lst[v:] )
	a.extend(lst[:v])
	print(lst)
	print(a)
	for i in range(2,max(a)):
		ind = a.index(i)
		if ind != i-1 :
			a = test5_4.rev(a,i,ind+1)
			print(a)


if __name__ == '__main__':
	CircleSort([5,3,1,8,2,4,7,6])
