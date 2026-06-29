# Script 1: Create a list of numbers 1–10. Print all even numbers using slicing and list comprehension both ways.

list = [x for x in range(1,11)]
print(list)

# even numbers using slicing
evens = list[1::2]
print(evens)

# even numbers using list comprehension 
even_nums = [x for x in list if x % 2 == 0]
print(even_nums)

