
def PrefixReversalSort( lst ):
	''' prefix reversal sort '''
	max_v = max(lst)
	print(lst)
	for v in range(max_v,1,-1):
		i = lst.index(v)
		if i == 0:
			lst = reversal(lst,v)
		else :
			lst = reversal(lst,i+1)
			lst = reversal(lst,v)

def reversal(lst, i):
	a = lst[0:i]
	b = lst[i:]
	a.reverse()
	a.extend(b)
	print(a)
	return(a)


if __name__ == '__main__' :
	PrefixReversalSort( [3,4,6,5,8,1,7,2])
