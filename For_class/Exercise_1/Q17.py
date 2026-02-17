# Write a program that takes two 5-letter words as input and finds the sum of the distance
# between the respective characters of these words.
# Example:
# Input:
# abcde
# abdfe
# Distance: 0-0-1-2-0
# Output: 3
# Input:
# pqxzy
# qpyax
# Distance: 1-1-1-25-1
# Output: 29

word1 = input("Enter a 5 letter word: ")
word2 = input("Enter another 5 letter word: ")
for i in range(4):
    print(abs(ord(word1[i]) - ord(word2[i])),"- ", end="")
print(abs(ord(word1[4]) - ord(word2[4])))
