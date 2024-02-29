from datetime import datetime
import requests
from http.cookiejar import Cookie

url = "https://www.facebook.com"

response = requests.get(url)
print(response.status_code)
print(response.headers)

print("SERVER:", response.headers.get("Server"))
if not response.cookies:
    print("no cookies received")
for index, cookie in enumerate(response.cookies):
    print("Cookie", index, ":\t\t", cookie, "\n")
    print(type(cookie))
    for attr in cookie.__dict__:
        if cookie.__dict__[attr]:
            if attr == "expires":
                print(attr, datetime.fromtimestamp(cookie.__dict__[attr] / 1000).strftime("%A, %d %B %Y"))
                continue
            print(attr, cookie.__dict__[attr])
    break

# print("this is a change for the second test branch")
