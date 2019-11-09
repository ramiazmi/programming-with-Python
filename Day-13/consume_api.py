import requests
import json

'''
In this example we will show hoe 
'''
# url = 'http://127.0.0.1:5000/api/employees/IT'
url = 'http://127.0.0.1:5000/api/employees'
data = {"department_name": "IT"}

print(data)
response = requests.get(url, data=json.dumps(data))

print(response.json())
print(response.text)
