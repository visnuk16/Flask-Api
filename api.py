import requests
import json

reqUrl = "https://api.github.com/users/visnu-04"

headersList = {
 "Accept": "*/*",
 "User-Agent": "Thunder Client (https://www.thunderclient.com)" 
}

payload = ""

response = requests.requests("GET", reqUrl, data=payload,  headers=headersList)

print(type(json.loads(response.text)))


response = json.loads(response.text)

print(response)

print("followers : " , ["fowllowers"])