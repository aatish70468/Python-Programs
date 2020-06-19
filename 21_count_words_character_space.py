fo = open("21_file.txt", "r")
count_words = []
count_character = 0
count_space = 0

for i in fo:
    count_words += i.split()
    count_space += i.count(" ")

for i in range(len(count_words)):
    count_character = count_character + len(count_words[i])

print("No. of Words: " + str(len(count_words)))
print("No. of Character: " + str(count_character + count_space))
print("No. of Space: " + str(count_space))
