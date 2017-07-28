import time
import numpy as np

def Score(DNA,si,l,score,m):
	for i in range( si,si+l):
		c = DNA[i-1] 
		score[ i - si ][ m[c] ] += 1
	max_score = sum( [ max(score[j]) for j in range(0,l) ] ) 
	return(max_score)


def ByPass(DNA,s,i,k,score,l,m):
	for j in range(i-1,-1,-1):
		for n in range( s[j]-1,s[j]-1+l):
			c = DNA[j][ n ]
			score[ n-s[j]+1 ][ m[c] ] += -1
		if s[j] < k:
			s[j] += 1
			return(j+1)
		else :
			s[j] = 1
	return(0)	
		

def MotifSearch (DNA,t,n,l):
	''' motif search '''
	s = [1] * t
	bestScore = l * t - 2* t
#	bestScore = 0
	bestMotif = []
	m = { 'A':0, 'T':1 , 'C':2, 'G': 3}
	score = np.zeros((l,4))
	i = 1
	while i > 0 :
		max_score = Score(DNA[i-1],s[i-1],l,score,m)
		if i < t :
			if max_score + (t-i)*l  < bestScore :
				i = ByPass(DNA,s,i,n-l+1,score ,l,m )
			else :
				i += 1
			
		else :
			if max_score > bestScore :
				bestScore = max_score
				bestMotif = list(s)
			i = ByPass(DNA,s,i,n-l+1,score ,l,m )
	for j in range(0 ,t):
		print(DNA[j][ bestMotif[j] : bestMotif[j]+l  ])
	print(bestScore,bestMotif)
	return(bestMotif)


if  __name__ == '__main__' :
	start = time.time()
	DNA = [
		'GATCGCTGACAGTTAAAGTGAAAAGCCTAAATGACATGACAGCAAAGGAGAAATTCTCTCCTCTCACGTC',
		'CAGAGCAATGCGGATCGCTGACGGAGATTCTGTAAAAGTGTTGATTTTCTGAAAGTGAGAATTCTTAAAC',
		'TGACATGACAGCAAAGGAGAAATTCTCTCGATCGCTGACCTCTCACGTCCAACCTGATCAGTTGCAGCAG',
		'AGATTTGCTAGCTGAAAACGGTCGCTTGAATATTACTCGATCGCTGACCTGCGGTGATTTCCGCATTTTC',
		'GGTTTTGAAATTGGAAGTTAAGATTGATCCATCAATCATGGGTGGAATGATCGTGATCGCCGACCCGTAT',
		'GGTTTTGAAATTGGAAGTTAAGATTGATCCATCAATCATGGGTGGAATGATCGGTTCGCTGACTCCGTAT',
		'ACAAGGCTGCCTTTGATGACCGGGATCCCATACCAAGGAGGAATGACTGGGATCGCTAACGAGTGGAATC',
		'TGGGGCCTCTGAAGAAGAAAACCAGAGCAAGGGAAGGGAAATGAGAAAAGATCGCTGACGCTAGTTCAAG'
	]
	MotifSearch(DNA,8,70,10)
	end = time.time()
	print(start,end,end-start)
