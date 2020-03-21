import urllib.request

import json


# Define parameters for request

def get_token():
    """
    export TOKEN=`curl -d '{"email":"<EMAIL>","password":"<PASSWORD>"}' -H "Content-Type: application/json" -X POST localhost:8080/auth  | jq -r '.token'`
    """
    data = {"email": "<EMAIL>", "password": "<PASSWORD>"}
    url = 'http://127.0.0.1:8080/auth'
    headers = {'Content-Type': "application/json"}

    req = urllib.request.Request(url,headers=headers, data=bytes(json.dumps(data), encoding="utf-8"))
    response = urllib.request.urlopen(req)
    response_content = response.read()
    token = json.loads(response_content.decode())["token"]

    return token



def check_token(token):
    url = 'http://127.0.0.1:8080/contents'
    headers = {'Authorization': f'Bearer {token}'}

    req = urllib.request.Request(url, headers=headers, )

    response = urllib.request.urlopen(req)
    return response.read()


token = get_token()
print(check_token(token))





class Mul:
    def __init__(self,n):
        self.n = n
    def __power__(self,fles):