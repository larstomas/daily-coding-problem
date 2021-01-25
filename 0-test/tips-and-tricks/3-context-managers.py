# f = open("./0-test/tips-and-tricks/test.txt", "r")

# file_content = f.read()

# f.close()

# words = file_content.split(" ")
# word_count = len(words)
# print(word_count)

## Alternative

with open("./0-test/tips-and-tricks/test.txt", "r") as f:
    file_content = f.read()

words = file_content.split(" ")
word_count = len(words)
print(word_count)