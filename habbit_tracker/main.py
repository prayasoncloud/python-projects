import requests

URL = "https://pixe.la/v1/users"
TOKEN = ""


body = {
    "token": TOKEN,
    "username":"prayaspatel",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=URL, json=body)
# print(response.text)

graphic_enpoint = "https://pixe.la/v1/users/prayaspatel/graphs/pokm123"

graph_body = {
    "id": "pokm123",
    "name": "prayas patel",
    "unit": "pages",
    "type": "int",
    "color": "momiji"

}


# response = requests.post(url=graphic_enpoint, json=graph_body, headers=headers)
# print(response.text)

body_pixel = {
    "date": "20240912",
    "quantity": "3"
}

response = requests.post(url=graphic_enpoint, headers=headers, json=body_pixel)
print(response.text)