import requests
url = 'https://lichess.org/api/account/email'

response = requests.get(url,  headers={"Authorization": "add your own lip"})

data = response.json()
print(data)


# import json
# url = "http://127.0.0.1:5000"

# item = {
#     "role": "teacher",
# }

# data = json.dumps(item)

# # response = requests.post(url+'/users', data=data, headers={"Content-Type": "application/json"})
# # response = requests.get(url+'/users')
# response = requests.put(url + '/users/10', data=data, headers={"Content-Type": "application/json"})
# response1 = requests.delete(url + '/users/3')
# response2 = requests.get(url + '/users/3')


# print(response1.json())
# print(response2.json())

