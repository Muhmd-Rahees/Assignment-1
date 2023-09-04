# Write a Python program that accepts a word from the user and reverse it.

word = str(input("Enter the word : "))

reverse_word = ""

for i in reversed(word) :
    reverse_word += i
print(reverse_word, "is the reverse of the word you entered")

