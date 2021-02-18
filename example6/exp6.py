import requests


def do_get(url):
    resp = requests.get(url)
    print(resp.status_code)
    print(resp.content)
    print(resp.text)
    print(resp.json())


def do_post(url, data):
    resp = requests.post(url, json=data)
    print(resp.json())


do_get("https://www.google.com/")
do_post("https://URL/path/", {
    "login": "LOGIN",
    "password": "PASSWORD"
})
