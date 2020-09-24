def mergeSort(arr): 
	if len(arr) >1: 
		mid = len(arr)//2 
		L = arr[:mid] 
		R = arr[mid:] 

		mergeSort(L)
		mergeSort(R)

		i = j = k = 0
		
		while i < len(L) and j < len(R): 
			if L[i] < R[j]: 
				arr[k] = L[i] 
				i+= 1
			else: 
				arr[k] = R[j] 
				j+= 1
			k+= 1
		
		while i < len(L): 
			arr[k] = L[i] 
			i+= 1
			k+= 1
		
		while j < len(R): 
			arr[k] = R[j] 
			j+= 1
			k+= 1

arr = [50, 40, 30, 20, 10] 

print ("Vetor Desordenado:") 
print (arr)

mergeSort(arr) 

print ("\n\nVetor Ordenado:") 
print (arr)