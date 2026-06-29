# Script 3: Rotate a list to the right by k positions. Example: [1,2,3,4,5] rotated by 2 = [4,5,1,2,3]. Use slicing.


# method 1 - 

list = [1,2,3,4,5]
k = 2
n = len(list)
print(list)

list3 = list[-k::] + list[:n-k:]
print(list3)

# method 2 - 

def rotate(list, k, n):
    return list[-k::] + list[:n-k:]

rotated_list = rotate(list,k,n)
print(rotated_list)