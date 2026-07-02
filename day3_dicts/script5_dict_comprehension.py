# Script 5 — Frequency counter + dict comprehension:
# Given nums = [1,1,2,2,2,3,4,4] — count frequency of each number using .get() method. Then write a dict comprehension that filters only numbers appearing more than once.


nums = [1,1,2,2,2,3,4,4]

# count frequency of each number using .get()

freq = {}

for num in nums:
    freq[num] = freq.get(num,0) + 1

print("Frequency of Each number: ")
for num, count in freq.items():
    print(num,":",count)

# filters only numbers appearing more than once

filtered_freq = {num: count for num,count in freq.items() if count > 1} 

print("Numbers appearing more than one's: ")
for num, count in filtered_freq.items():
    print(num,":",count)

