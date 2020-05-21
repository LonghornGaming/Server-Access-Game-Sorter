# literally just run quicksort on some data read from stdin

# read files + write to list "games"
file = open('file.txt')
games = file.read().splitlines()

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

print("Games A-E")
for i in games:
    cha = i[0]
    if cha >= 'A' and cha <= 'E':
        print(i)

print("\nGames F-M")
for i in games:
    cha = i[0]
    if cha >= 'F' and cha <= 'M':
        print(i)

print("\nGames N-R")
for i in games:
    cha = i[0]
    if cha >= 'N' and cha <= 'R':
        print(i)

print("\nGames S-Z")
for i in games:
    cha = i[0]
    if cha >= 'S' and cha <= 'Z':
        print(i)