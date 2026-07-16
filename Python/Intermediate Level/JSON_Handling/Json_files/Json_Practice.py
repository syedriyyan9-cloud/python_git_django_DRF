import json
# loading json into a python obj
# file_path = 'US_states.json'
# with open(file_path, 'r', encoding='utf-8') as f:
#     data = json.load(f)

# we can also load the file and use json.load to load the content, no need to 
# use r or encoding parameters
with open('US_states.json') as file_opened: # opens the json file
    data = json.load(file_opened)   # loads the content from json file to data
print(type(data))

# now lets say we want to remove all the area code from the data and then
# rewrite the json file into a separate file 
# we have already read the data. now we have to remove area code
for state in data['states']:
    del state['area_codes']
print(data)
# now that we have remove the area codes we have to store it so we will 
# create a file and save data to it

# with open only opens the file. dump does the remaining work it self,
with open('updated_data.json', 'a', encoding='utf-8') as f: #creates a json file if not present
    json.dump(data, f, indent=2)    # adds json content to the json file
