text = input("Enter a paragraph: ")

words = text.lower().split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

print(frequency)