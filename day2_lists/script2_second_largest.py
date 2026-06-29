# Script 2: Given arr = [3,1,4,1,5,9,2,6,5] — find the second largest element without using sort() (use max() and list comprehension).

arr = [3,1,4,1,5,9,2,6,5]
print(arr)

def second_largest(arr):
    largest = [x for x in arr if x!= max(arr)]
    second_largest = max(largest)
    return second_largest

second_largest_num = second_largest(arr)

print(second_largest_num)