import re
def text_match(text):
    patterns = '^[a-zA-Z0-9_]*$'
    if re.search(patterns, text):
        return 'Found a Match!'
    else:
        return 'Not Matched!'

print(text_match("The quick brown"))
print(text_match("Python_Exercises_1"))
