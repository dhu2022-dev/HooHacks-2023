import requests
import json

# me when i put my api key in an unsecure spot
api_key = '?key=6894504f927ce11d26da06fe17972703'

# get ALL the data
all_mock_cust = requests.get('http://api.nessieisreal.com/enterprise/customers' + api_key)

# the second number controls which customer we're pulling the id from
all_mock_cust = all_mock_cust.json()
cust_id = all_mock_cust['results'][1]['_id']

#get one data (china)
cust_data = requests.get('http://api.nessieisreal.com/enterprise/customers/' + cust_id + api_key)

print(cust_data.json())

response = requests.get('http://api.nessieisreal.com/ecustomers/' + cust_id + api_key) #56c66be5a73e49274150727b?key=6894504f927ce11d26da06fe17972703')
print(response.json())
