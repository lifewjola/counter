# Program to count the number of words in a file
filename = input("Enter the filename: ")
with open(filename) as file:
    text = file.read()
num_words = len(text.split())
num_lines = len(text.splitlines())
num_chars = len(text)

print("Number of words: ", num_words)
print("Number of lines: ", num_lines)
print("Number of characters: ", num_chars)
