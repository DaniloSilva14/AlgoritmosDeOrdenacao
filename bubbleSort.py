def bubbleSort(arr, n): 
	for i in range(n): 
		for j in range(0, n-i-1): 
			if arr[j] > arr[j+1] : 
				arr[j], arr[j+1] = arr[j+1], arr[j] 

arr = [50, 40, 30, 20, 10] 
n = len(arr) 

print ("Vetor Desordenado:") 
print (arr)

bubbleSort(arr,n) 

print ("\n\nVetor Ordenado:") 
print (arr)