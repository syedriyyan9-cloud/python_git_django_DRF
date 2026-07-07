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