import re
text = """
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""
# get all the names
pattern = re.compile(r"M(r|s|rs)(\.\s|\s)[a-zA-Z]+")
matches = pattern.finditer(text)
for match in matches:
    print(match)

print("---------------------------------------------")

emails = """
syedriyyan9@gmail.com
riyyahassan789@gmail.com
hassanriyyan@gmail.com
kittyslife6789@gmail.com
"""
# get only the emails that contain the word "riyyan"
pattern = re.compile(r"(\w*riyyan?|^riyyan)\w*@gmail.com")
matches = pattern.finditer(emails)
for match in matches:
    print(match)

print("---------------------------------------------")

urls = """
https://www.google.com
http://www.youtube.com
https://code.com
https://www.nasa.com
"""
# Get all the urls 
pattern = re.compile(r"https?://(www)?\.?[a-z]+\.com")
matches = pattern.finditer(urls)
for match in matches:
    print(match)

print("---------------------------------------------")

sentence = "Start of this sentence is from the first word."
# there are flags in re module that can be used to make coding easy
# one in IGNORECASE flat that ignores if the letters are upper case or lower case
pattern = re.compile(r"start", re.IGNORECASE)

# search method searches for the pattern in the entire text.
# if it exists then it returns its first instance where it is found else returns none
matches = re.search(pattern,sentence)
print(matches)

# match method searches for a pattern at the start of the text
# returns if found else returns none
matches = re.match("Start",sentence)
print(matches)

# findall returns a list of all the matched patterns, returns the first group if found, returns a list else none
# finditer returns the match object found based on the pattern given else none
