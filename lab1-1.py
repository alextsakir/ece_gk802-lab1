import requests
from http.cookiejar import Cookie

url = "http://facebook.com/"

response = requests.get(url)

# print(response.headers)

# print("SERVER:", response.headers.get("Server"))

for index, cookie in enumerate(response.cookies):
    print("Cookie", index, ":\t\t", cookie, "\n")
    for attr in cookie.__dict__:
        if cookie.__dict__[attr]:
            print(attr, cookie.__dict__[attr])
    break

print("this is a change for branch")
