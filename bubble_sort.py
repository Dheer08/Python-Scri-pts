def bubble_sort(arr):
	n = len(arr)

	for i in range(0,n):
		for j in range(i+1,n):
			if(arr[i] > arr[j]):
				temp = arr[i]
				arr[i] = arr[j]
				arr[j] = temp


	return arr

print(bubble_sort([1,5,7,2,3]))