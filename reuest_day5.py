# Calling another microservice using get method
import requests
headers = {
   'X-Auth-Header': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MjMsImlzcyI6IkRTQ0UiLCJzdWIiOiJFbXBsb3llZSBNaWNyb3NlcnZpY2UgVG9rZW4ifQ.Dpd6Wv1VojYbfOn_h9_0w7_gG0pVkZIUotvabiLc2EY'
}
response = requests.get('http://localhost:5000/api/employee/1', headers=headers)
print(response.text)