import requests

# response = requests.get('https://xkcd.com/353/')
# print(type(response))
# print(help(response))
# print(response.text)
# print(response.content)
# print(response.headers)

# saves image from internet to folder
# image = requests.get('https://imgs.xkcd.com/comics/python.png')
# with open('image.png', 'wb') as f:
#     f.write(image.content)

# print(response.status_code)

# payload = {'page': 3, 'count':323}
# # get request
# res = requests.get('https://httpbin.org/get', params=payload)
# print(res.text)
# print(res.url)  # to look at what url was searched for using get


# payload = {'username':'riyyan', 'email':'riyyanhassan@gmail.com'}
# post request
# res = requests.post('https://httpbin.org/post', data=payload)
# print(res.text)

# we get our responses in json 
# so we can use .json method to convert it to python objects
# print(res.json())   # here we can store it in a variable and use it like a dict
# r_dict = res.json()
# print(r_dict['form'])

# basic auth using .get method
r = requests.get('https://httpbin.org/basic-auth/riyyan/123', auth=('riyyan','123'), timeout=3)
print(r.status_code)

# always use timeout as if not used and the page does not give back the response
# then request will wait indefinitely, hanging the program.
# so always use it.
# use timeout parameter and the param takes the values in seconds.