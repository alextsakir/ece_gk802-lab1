from datetime import datetime as dt
from requests import get, Response

url = "https://www.facebook.com"

response: Response = get(url)
print("RESPONSE:", response.status_code, "\t\tSERVER:", response.headers.get("Server"))
# print("HEADERS:", response.headers)

if not response.cookies:
    print("no cookies in response")
for index, cookie in enumerate(response.cookies):
    print("\nCookie", index, "\t\t", cookie)
    for inner, attr in enumerate(cookie.__dict__):
        if not cookie.__dict__[attr]:
            continue
        if attr == "expires":
            print("\t\texpires at", dt.fromtimestamp(cookie.__dict__[attr]).strftime("%A, %d %B %Y"))
            print("\t\thas expired:", cookie.is_expired())
        elif attr == "_rest" and isinstance(cookie.__dict__[attr], dict):
            print("\t\tnon standard attributes:")
            print("\t\t\t" + "\t\t".join([str(_k) + ": " + str(_v) for _k, _v in cookie.__dict__[attr].items()]))
        else:
            print("\t\t" + attr + ":", cookie.__dict__[attr])
