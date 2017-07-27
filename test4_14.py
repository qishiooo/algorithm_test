
def calculate_frequency(s,k):
	d = {}
	for i in range(0,len(s)-k):
		s1 = s[i:i+k]
		if d.has_key(s1):
			d[s1] += 1
		else :
			d[s1] = 1
	di = sorted(d.items(),key = lambda f : f[1],reverse=True )
	for i in di:
		print(i)

if __name__ == "__main__":
	calculate_frequency('actgagagactagtcagcttagacgatacgtaagctagcacatgactatgactatactgactagcatcgaat',5)
