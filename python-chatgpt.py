#generic library to make http requests to an API
import requests
import os

#endpoint
api_endpoint = "https://api.openai.com/v1/completions"
#API Key
api_key = os.getenv("OPENAI_API_KEY")

#request headers as per the open ai API docs
request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer" + api_key
}
#request body as per the open ai API docs
request_data = {
    "model": "text-davinci-003",
    "prompt": "Write python script for printing out today's date",
    "max_tokens": 100,
    "temperature": 0.5
}
#performing a post request
response = requests.post(api_endpoint, headers=request_headers, json=request_data)
#check if the request was successful
if response.status_code == 200:
    print(response.json())
else:
    print(f"Request failed with status code: {str(response.status_code)}")