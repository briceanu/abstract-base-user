import requests
import sys



def create_blog():
    url = 'http://127.0.0.1:8000/blog/list_create_blogs'

    data = {
    'username': 'costica',
    'details': 'i this pawodmapowd mapwod mpaw    ',
    'age': 45
 }


    headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI4NTE0OTk1LCJpYXQiOjE3Mjg1MTEzOTUsImp0aSI6IjhhYTBiM2QxODQxNTRmZTk4NDQ3YTUyMjVkZTczYTkwIiwidXNlcm5hbWUiOiJjb3N0aWNhIn0.jvtLoATTTzeGMye1UWy5Uf1bk7iOVEFyxMh_mhuYPLI"
    }
    res = requests.post(url=url, headers=headers,data=data)


    print(res.status_code)
    print(res.url)
    print(res.text)


def list_blogs():
    url = 'http://127.0.0.1:8000/blog/list_create_blogs'


    headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI4NTE0NDczLCJpYXQiOjE3Mjg1MTA4NzMsImp0aSI6IjhjNTdhMTRlMDkxMDQ3YWU5NDQ3YTdhYTIwYTIyYjliIiwidXNlcm5hbWUiOiJjb3N0aWNhIn0.M8C9k359WH3K1d63Kcq0HEWmV3StqBJi0RUt8HTVSYM"
    }

    res = requests.get(url=url, headers=headers)

    print(res.status_code)
    print(res.url)
    print(res.text)


def update_blog():
    url = 'http://127.0.0.1:8000/blog/list_create_blogs?id=5'

    data = {
    'username': 'costica',
    'details': 'sus su sus us su ',
    'age': 56,
 }
    headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI4NTE2NDI4LCJpYXQiOjE3Mjg1MTI4MjgsImp0aSI6IjE3YjVkMDU1OWZlZTRlNzBiOTVlMTgwOTM1MDEzMGY3IiwidXNlcm5hbWUiOiJhZHJpYW4ifQ.edwWPkA8wmvtsCDXBU-ELkZRcHzazNemw7ihNLogpiM"
    }

    res = requests.put(url=url,data=data, headers=headers)

    print(res.status_code)
    print(res.url)
    print(res.text)

if __name__ == "__main__":
    if sys.argv[1] == 'create_blog':
        create_blog()

    if sys.argv[1] == 'list_blogs':
        list_blogs()
    if sys.argv[1] == 'update_blog':
        update_blog()

    else:
        exit(0) 

