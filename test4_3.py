
def nextvertex(lst,i):
	lst.append(1)
	return(lst,i+1)	

def bypass(lst,i,k):
	for j in range(i-2,-1,-1):
		if lst[j] < k :
			lst[j] += 1
			out = [ lst[x] for x in range(0,j+1) ]
			return(out,j+1)
	return(lst,0)


def subset(lst,m):
	''' get m element subset from  n element lst'''
	lst.sort()
	n = len(lst)
	i = 1
	score = 0
	s = [1]
	result=[]
	while( True ):
		score = s.count(2)
		dist  = s.count(1)
		if score < m and dist < n-m+1 :
			(s,i) = nextvertex(s,i)
		elif dist == n-m+1 :
			s[i-1] += 1
		else :
			out = []
			for j in range(0,len(s) ) :
				if s[j] == 2 :
					out.append(lst[j])
			result.append(out)
			(s,i) = bypass(s,i,2)
			if i == 0 :
				result.sort()
				return(result)

if __name__ == '__main__' :
	out = subset([1,3,2,6,5,4],3)
	print(out)
