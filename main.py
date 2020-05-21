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


# print games
cha = ''
hitA = 0
hitF = 0
hitN = 0
hitS = 0
hasInvalid = 0

for i in games:
    cha = i[0]
    
    if cha >= 'A' and hitA == 0:
        print("**__Games A-E__**")
        hitA = 1
    elif cha >= 'F' and hitF == 0:
        print("\n**__Games F-M__**")
        hitF = 1
    elif cha >= 'N' and hitN == 0:
        print("\n**__Games N-R__**")
        hitN = 1
    elif cha >= 'S' and hitS == 0:
        print("\n**__Games S-Z__**")
        hitS = 1
    
    if cha >= 'A' and cha <= 'Z':
        print(i)
