
def BreakPointReversalSort(lst):
	''' breakpoint reversal sort'''
	bk = 1000
	print(lst)
	while bk >0 :
		(bk,lst) = bpsort(lst)
		print(bk,lst)
		
	

def bpsort(lst):
	pre_point = 0
	pre_band = 0
	last= 0
	add = {0 : 0}
	subtract = {}
	for i in range(0 , len(lst)):
		if  lst[i] == pre_point +1  :
			add[ pre_band ] =  i+1
			if subtract.has_key( pre_band ):
				del(subtract[pre_band])
		elif lst[i] == pre_point -1 :
			subtract[ pre_band ] = i+1
		else :
			pre_band = i+1
			subtract[ pre_band ] = i+1
		pre_point = lst[i]
	if pre_point != max(lst) :
		n = len(lst)+1
		add[ n ] = n 	
	
	bp = len(subtract) + len(add) - 1
	if len(subtract) == 0  :
		for (k,v) in add.iteritems():
			if k == 0 or k == len(lst)+1 :
				continue
			a = rev(lst,k,v)
			return(bp,a)

	for (k,v) in subtract.iteritems() :
		n2 = lst[v-1]
		n3 = lst[k-1]
		n4 = n3 + 1
		n1 = n2 - 1		
		pos2 = lst.index(n2) + 1
		pos3 = lst.index(n3) + 1
		pos4 = n3 < max(lst) and lst.index(n4)+1  or  len(lst) + 1
		pos1 = n2 > 1 and lst.index(n1)+1  or 0
		if pos4 < pos3 and ( add.has_key(pos4) or subtract.has_key(pos4) ) :
			left3 = lst[pos3-2]
			left4 = pos4 > 1 and lst[pos4-2] or 0
			if left3 +1 == left4 or left3 -1 == left4 :
				a = rev(lst,pos4,pos3-1)
				return(bp-2 ,a)
		elif pos4 > pos3 and (add.has_key(pos4) or subtract.has_key(pos4)   ) :
			left3 = lst[pos3-2] 
			left4 = lst[pos4-2]
			if left3 +1 == left4 or left3 -1 == left4 :
				a = rev(lst,pos3,pos4-1)
				return(bp-2,a)

		if pos1 < pos2  and (  subtract.has_key(pos1) or n1 in add.values() ) :
			right1 = lst[pos1]
			right2 = pos2< len(lst) and lst[pos2] or len(lst)+1
			if right1 +1 == right2 or right1 -1 == right2 :
				a = rev(lst,pos1+1,pos2)
				return(bp-2,a)
		elif pos1 > pos2 and( n1 in add.values() or subtract.has_key(pos1) ):
			right1 = pos1 < len(lst) and lst[pos1]  or  len(lst) +1 
			right2 = lst[pos2]
			if right1 +1 == right2 or right1 -1 == right2 :
				a = rev(lst ,pos2 +1 ,pos1)
				return(bp-2,a)


	for (k,v) in subtract.iteritems() :
		#n = lst[v-1] + 1
		n2 = lst[v-1]
		n3 = lst[k-1]
		n4 = n3 + 1
		n1 = n2 - 1		
		pos2 = lst.index(n2) + 1
		pos3 = lst.index(n3) + 1
		pos4 = n3 < max(lst) and lst.index(n4)+1  or  len(lst) + 1
		pos1 = n2 > 1 and lst.index(n1)+1  or 0
		if pos4 < pos3 and ( add.has_key(pos4) or subtract.has_key(pos4) ) :
			a = rev(lst,pos4,pos3-1)
			return(bp-1 ,a)
		elif pos4 > pos3 and (add.has_key(pos4) or subtract.has_key(pos4)   ) :
			a = rev(lst,pos3,pos4-1)
			return(bp-1,a)
		if pos1 < pos2  and (  subtract.has_key(pos1) or n1 in add.values() ) :
			a = rev(lst,pos1+1,pos2)
			return(bp-1,a)
		elif pos1 > pos2 and( n1 in add.values() or subtract.has_key(pos1) ):
			a = rev(lst ,pos2 +1 ,pos1)
			return(bp-1,a)



def rev(lst,start,end):
	a = list(lst[0:start-1])
	a.extend( [lst[i] for i in range(end-1,start-2,-1) ] )
	a.extend(lst[end:])
	return(a)



if __name__ == '__main__':
#	BreakPointReversalSort([7,2,1,6,5,8,4,3,9])
#	BreakPointReversalSort([4,2,7,1,3,8,6,9,5])
#	BreakPointReversalSort([3,4,8,9,1,2,5,6,7])
	BreakPointReversalSort([3,4,6,5,8,1,7,2])
