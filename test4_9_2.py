
def rank(lst):
	set0 = set()
	out = []
	select(lst,out,set0)
	lst1 = list(set0)
	lst1.sort()
	return(lst1)
	
def select(lst,out,set0):
	if len(lst) == 0 :
		rank=[]
		tmp=0
		for i in out:
			tmp += i
			rank.append(tmp)
		rank = tuple(rank)
		set0.add(rank)
		return
	for i in range(0,len(lst) ):
		v = lst[i]
		del(lst[i])
		out.append(v)
		select(lst,out,set0)
		lst.insert(i,v)
		out.pop()

def ddp( A,B,C):
	''' double digest problem '''
	A = list(A)
	B = list(B)
	rank1 = rank(A)
	rank2 = rank(B)
	c = list(C)
	c.sort()
	for t1 in rank1:
		for t2 in rank2 :
			lst = list(t1)
			lst.extend(t2)
			lst.sort()
			lst.pop()
			before = 0
			out = []
			for i in lst:
				out.append(i-before)
				before = i
			out.sort()
			if out == c :
				lst.insert(0,0)
				print(t1,t2)

if __name__ == '__main__':
#	ddp([4,4,4,4,5],[3,4,4,5,5],[1,1,2,2,2,3,3,3,4])
	print(rank([3,4,4,5,5]))
