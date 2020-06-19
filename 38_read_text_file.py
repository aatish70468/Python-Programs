fo = open("38_file.txt", "r")
statement = []
no_statement = 0
no_lines = 0
for i in fo:
    statement += i.split(". ")
    no_lines += 1

fo.close()
no_statement = len(statement)
print(statement)
print("No. of Lines: " + str(no_lines))
print("No. of Statement: " + str(no_statement))
