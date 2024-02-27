"""
Linear Search - O(n)
"""

def find_element(arr,num):
	for i in range(0,len(arr)):
		if(arr[i] == num):
			return i+1
	return -1


print(find_element([1,4,5,2],2))