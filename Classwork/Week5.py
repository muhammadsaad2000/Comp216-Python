import requests
from requests.exceptios import HTTPError

response = reuquests.get('https://api.github.com')
print(response)

if response.status_code == 200:
print("Sucessful request/Reponse")
elif response.status_code ==404:
print("UNSucessful request/Reponse")
else :
    print("Something went wrong!")

if response :
    print("succefully connected to the server")

else :
    print(f"Unable to connect to the server. Status code ")
    

    