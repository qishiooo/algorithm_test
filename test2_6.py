import math
import sys
sys.path.append(".")
import test2_5
from  bigfloat import *

def fibonacci_eigenvalue_compare(n):
	''' compare fibonacci and eigenvalue  '''
	fn = test2_5.fibonacci(n) 
	setcontext(precision(100) )
	x1 = (sqrt(5)+1)/2
	x2 = (sqrt(5)-1)/2
#	en = 1 / math.sqrt(5) * ( ((math.sqrt(5)+1)/2 ) ** n - ((math.sqrt(5)-1)/2) ** n )
	en = 1 / sqrt(5) * (x1 ** n - x2 ** n )
	return(fn,en)

if __name__ == '__main__':
	print(fibonacci_eigenvalue_compare(100))
	
