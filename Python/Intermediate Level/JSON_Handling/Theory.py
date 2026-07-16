# json module has 4 main functions.
# 1. dumps() which turns a python dict into json string
# 2. loads() which turns a json string into python dict which python can read
# 3. load() used to load json from a file to python program
# 4. dump() used to save json to a file from python program
# 
# Then we have requests module that is used for handling APIs
# requests.get() method gets data using api from server
# requests.post() method sends data using an api from server
# the data that is sent back from the server is called a response
# a response has a few methods like .status_code which give status code
# .headers returns header, and .text that returns body of the response
# they all have their own purposes like status_code can be used to check if 
# response is valid using conditional statement like if status_code == 200 etc.
# 
# use requests.Session() when making multiple requests to the same API
# it persists headers, cookies, and connection pooling automatically. 
# Sessions also handle authentication once and reuse it across requests, 
# making your code cleaner and more efficient. 
# Remember to set timeouts using the timeout parameter to prevent your code 
# from hanging indefinitely, especially when dealing with unreliable networks. 
# 
# Status codes are grouped by category: 2xx for success, 3xx for redirection, 
# 4xx for client errors (your mistake), and 5xx for server errors (their problem). 
# Always handle at least 200, 400, 401, 404, and 500 in your code. 
# Headers are crucial for authentication, content negotiation, and rate limiting 
# many APIs require you to send API keys via headers like {"X-API-Key": "your_key"}.