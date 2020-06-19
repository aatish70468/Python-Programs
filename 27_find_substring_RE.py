import re
def find_substring(string, subString):
    if re.search(subString, string):
        return 'Substring Found'
    else:
        return 'Substring not Found'

string = input("Enter the String: ")
subString = input("Enter the subString: ")
print(find_substring(string, subString))
