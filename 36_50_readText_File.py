fo = open("36_file.txt", "r")
words = []
no_lines = 0
for i in fo:
    words += i.split()
    no_lines += 1

same_words = {}
count = 0
for i in sorted(words):
    count = words.count(i)
    same_words[i] = count
    count = 0

no_words = len(same_words)
print("No. of Lines: " + str(no_lines))
print("No. of Unique Words: " + str(no_words))
print("Words in Dictionary: " + str(same_words))
