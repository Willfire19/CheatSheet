# Sorting
import random

def mergesort( aList ):
	_mergesort( aList, 0, len( aList ) - 1 )
 
 
def _mergesort( aList, first, last ):
	# break problem into smaller structurally identical pieces
	mid = ( first + last ) / 2
	if first < last:
		_mergesort( aList, first, mid )
		_mergesort( aList, mid + 1, last )

	# merge solved pieces to get solution to original problem
	a, f, l = 0, first, mid + 1
	tmp = [None] * ( last - first + 1 )

	while f <= mid and l <= last:
		if aList[f] < aList[l] :
			tmp[a] = aList[f]
			f += 1
		else:
			tmp[a] = aList[l]
			l += 1
		a += 1

	if f <= mid :
		tmp[a:] = aList[f:mid + 1]

	if l <= last:
		tmp[a:] = aList[l:last + 1]

	a = 0
	while first <= last:
		aList[first] = tmp[a]
		first += 1
		a += 1
 
def quicksort( aList ):
	_quicksort( aList, 0, len( aList ) - 1 )
 
def _quicksort( aList, first, last ):
	if first < last:
		pivot = partition( aList, first, last )
		_quicksort( aList, first, pivot - 1 )
		_quicksort( aList, pivot + 1, last )
 
 
def partition( aList, first, last ) :
	pivot = first + random.randrange( last - first + 1 )
	swap( aList, pivot, last )
	for i in range( first, last ):
		if aList[i] <= aList[last]:
			swap( aList, i, first )
			first += 1

	swap( aList, first, last )
	return first
  
def swap( A, x, y ):
	A[x],A[y]=A[y],A[x]

def main():
	print "Sorting"
	print "Merge Sort"

	array = [5, 3, 6, 10, 2, 0, 1, 8]
	mergesort(array)
	print array

	array2 = [6, 9, 3, 10, 4, 5, 1]
	quicksort(array2)
	print array2

if __name__ == "__main__":
	main()