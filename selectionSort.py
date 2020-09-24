def selectionSort(arr, n): 
  for i in range(n):
	  min_idx = i 
	  for j in range(i+1, n): 
		  if arr[min_idx] > arr[j]: 
			  min_idx = j 
				 
	  arr[i], arr[min_idx] = arr[min_idx], arr[i] 

arr = [50, 40, 30, 20, 10] 
n = len(arr)

print ("Vetor Desordenado:") 
print (arr)

selectionSort(arr,n) 

print ("\n\nVetor Ordenado:") 
print (arr)
