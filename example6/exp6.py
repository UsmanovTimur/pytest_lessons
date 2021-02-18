import requests


def do_get(url):
    resp = requests.get(url)
    print(resp.status_code)
    print(resp.content)
    print(resp.text)
    print(resp.json())


do_get("https://www.google.com/")
