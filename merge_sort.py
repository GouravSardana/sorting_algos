def mergeSort(lst):

	n = len(lst)
	mid = n // 2

	if(n <= 1):
		print("list is already sorted", lst)
	
	else: # we split our list into 2 halves (left half and right half) 

		left_half = lst[ :mid] 
		right_half = lst[mid: ]

		mergeSort(left_half)  # recursively call the mergeSort method on each half 
		mergeSort(right_half)

		# merge process
		i=j=k = 0
		while(i < len(left_half) and j < len(right_half)):
			if(left_half[i] < right_half[j]):
				lst[k] = left_half[i]
				i = i + 1
			else:
				lst[k] = right_half[j]
				j = j + 1
			k = k + 1

		while(i < len(left_half)):
			lst[k] = left_half[i]
			i = i + 1
			k = k + 1
		while(j < len(right_half)):
			lst[k] = right_half[j]
			j = j + 1
			k = k + 1

	return lst		
	

# print(mergeSort([14,46,43,27,57,41,45,21,70]))

# print(mergeSort([10, 8 , 8, 7 , 5, 4]))