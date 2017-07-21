
def square_matrix_multiply( lst ):
	[a1,a2,a3,a4]= lst[:]
	return ([a1*a1+a2*a3,a1*a2+a2*a4,a1*a3+a3*a4 ,a2*a3+a4*a4])
	

def fibonacci_fast (n):
	''' fast fibonacci algorithm ,  O( log(N) )'''
	after = [1,1,1,0]
	i = 1
	while 1 :
		before = after
		after = square_matrix_multiply(before)
		i *= 2
		print(i,after)
		if i > n : break
	if 3 * i/4 > n :
		if i/2 == n :
			return(before[2])
		elif i/2 + 1 == n :
			return(before[0])
		else :
			(x,y)=(before[2],before[0])
			for j in range(i/2+2,n+1):
				result = x + y
				(x,y)=(y,result)
			return(y)
	else :
		if i == n :
			return(after[2])
		else :
			(x,y)=(after[2],after[0])
			for j in range(i-1,n-1,-1):
				result = y - x 
				(y,x) = (x,result)
				print(x,y,result)
			return(x)
		
if __name__ == '__main__' :
	print(fibonacci_fast(7))
