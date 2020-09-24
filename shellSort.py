def shellSort(arr,n): 
	gap = n/2

	while gap > 0: 
		for i in range(gap,n): 
			temp = arr[i] 
			j = i 
			while j >= gap and arr[j-gap] >temp: 
				arr[j] = arr[j-gap] 
				j -= gap 

			arr[j] = temp 
		gap /= 2

arr = [50, 40, 30, 20, 10] 
n = len(arr) 

print ("Vetor Desordenado:") 
print (arr)

shellSort(arr,n) 

print ("\n\nVetor Ordenado:") 
print (arr)