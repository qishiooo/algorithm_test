
def search(s1,s2,k):
	dist=0
	for i in range(0,len(s1)):
		if s1[i] != s2[i] :
			dist += 1
		if dist > k :
			return(False)
	return(True)


def search_first_motif( s, motif ,k ):
	''' search first motif (dist <= k ) from a long str'''
	l = len(motif)
	for i in range(0 , len(s) ):
		subs = s[i:i+l]
		if  search(subs ,motif,k ) :
			print(i,subs)
			return

if __name__ == '__main__':
	search_first_motif('1a234A239083ab23acdabefg23349sf3f3abcdegfh8fuabc9ofsabc','abcdefgh',2)
