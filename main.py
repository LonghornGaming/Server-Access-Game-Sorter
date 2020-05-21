# literally just run quicksort on some data read from stdin

import sys

# read files + write to list "games"
file = open('file.txt')
games = file.readlines()

# QuickSort partition method
def split(arr, low, high): 
    lowerIndex = low - 1
    thePivot = arr[high]
  
    for i in range(low, high): 
        if arr[i] < thePivot: 
            lowerIndex += 1
            temp = arr[lowerIndex]
            arr[lowerIndex] = arr[i]
            arr[i] = temp
  
    temp = arr[lowerIndex + 1]
    arr[lowerIndex + 1] = arr[high]
    arr[high] = temp
    return lowerIndex + 1 

# Actual QuickSort method .. do they have this in python3 already? 
def quickSort(arr, low, high): 
    if low < high: 
        index = split(arr,low,high) 
        quickSort(arr, low, index-1) 
        quickSort(arr, index+1, high) 

# call QuickSort
quickSort(games, 0, len(games)-1)

# print result
for i in games:
    print(i)
