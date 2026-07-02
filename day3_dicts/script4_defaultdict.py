# Script 4 — defaultdict:
# Given a list of words, use defaultdict(list) to group words by their first letter.

from collections import defaultdict

words = ["apple", "banana", "avocado", "blueberry", "cherry"]

groups = defaultdict(list)

for word in words:
    groups[word[0]].append(word)

for letter, words in groups.items():
    print(letter,":",words)
