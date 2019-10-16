def selection_sort(lst):

	n = len(lst)

	for i in range(n): # to loop throught through all the elments within the list

		smallest_index = i # let the index for smallest element be initially i

		for j in range(i+1, n):  # loop from i + 1 to n 
			if(lst[j] < lst[smallest_index]):  # if any element is less than lst[smallest_index]
				smallest_index = j # then smallest index becomes the new index

		# swapping the elements (swapping 2 nos operation)
		temp = lst[smallest_index]
		lst[smallest_index] = lst[i]
		lst[i] = temp

	return lst # return sorted list


print(selection_sort([5, 7, 14, 2, 8]))