import test4_1


def same_multiple_set ( set1 ,set2):
	''' set1 + set2  and set1 - set2  have same  patial digest segment '''
	set_plus = []
	set_subtract = []
	for i in set1 :
		for j in set2 :
			set_plus.append(i+j)
			set_subtract.append(i-j)
	set_plus.sort()
	set_subtract.sort()
	lst1 = test4_1.multiple_set(set_plus)
	lst2 = test4_1.multiple_set(set_subtract)
	print(lst1)
	print(lst2)

if __name__ == '__main__':
	#same_multiple_set([1,2,6],[-6,2,7])
	same_multiple_set([1,2],[4,7])
