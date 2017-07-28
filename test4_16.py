import time
import numpy as np


def MedianSearch(DNA,t,n,l):
	s = [1] * l
	i = 1
	minDist = 2*l
	bestMedian = []
	while i > 0 :
		dist = Caldist(DNA,s,i,t,n,l)
		if i < l :
			if dist > minDist :
				(s,i) = Bypass(s,i)
			else :
				i += 1
		else :
			if dist < minDist :
				minDist = dist
				bestMedian = list(s)
			(s,i) = Bypass(s,i)
	return(bestMedian)


def Bypass(s,current):
	for i in range(current,0,-1):
		if s[i-1] < 4 :
			s[i-1] += 1
			return(s,i)
		else :
			s[i-1] = 1	
	return(s,0)


def Caldist(DNA,s,current,t,n,l):
	dist = 0
	m = ['A','T','C','G']
	for i in range( 0 , t):
		min_d = current
		d = current
		for j in range(0 , n-l+1):
			d = current
			for k in range(0 ,current):
				c1 = DNA[i][j+k]
				c2 = m[ s[k-1]-1 ]
				if c1 == c2 :
					d -= 1
			if min_d > d :
				min_d = d
			if d == 0 :
				break
		dist += min_d
	return(dist)



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
		'TGGGGCCTCTGAAGAAGAAAACCAGAGCAAGGGAAGGGAAATGAGAAAAGATCGCTGACGCTAGTTCAAG',
	]
	MedianSearch(DNA,8,70,10)
	end = time.time()
	print(start,end,end-start)
