import requests
import sys



def create_blog():
    url = 'http://127.0.0.1:8000/blog/list_create_blogs/'

    data = {
    'username': 'costica',
    'details': 'this is the second costica',
    'age': 39
 }


    headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI4ODMwMzc4LCJpYXQiOjE3Mjg4MjY3NzgsImp0aSI6ImQyOGQ5NTJmZGExMzRiYjU5Mzk4ZThkYWRmYzNjZTVhIiwidXNlcm5hbWUiOiJhZHJpYW4ifQ.5uwZiDkNu3lqHHAlvLuc0hjtMTtnwi5WEOcLYehfTz4"
    }
    res = requests.post(url=url, headers=headers,data=data)


    print(res.status_code)
    print(res.url)
    print(res.text)


def list_blogs():
    url = 'http://127.0.0.1:8000/blog/list_create_blogs'


    headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI4OTE0MTk5LCJpYXQiOjE3Mjg5MTA1OTksImp0aSI6IjA3MDUzNDI3ZDk4NjRlZGE4MDJkNmRmYjRjMWVmNWIxIiwidXNlcm5hbWUiOiJhZHJpYW4ifQ.gTUoMitAnzeXXJKCwkx14w1AOHqyH2mfeHjMwCgj3Ps"
    }

    res = requests.get(url=url, headers=headers)

    print(res.status_code)
    print(res.url)
    print(res.text)


def update_blog():
    url = 'http://127.0.0.1:8000/blog/list_create_blogs?id=1'

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






def remove_blog():
    url = f'http://127.0.0.1:8000/blog/remove_blog?id={sys.argv[2]}'

    headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI4OTE0MTk5LCJpYXQiOjE3Mjg5MTA1OTksImp0aSI6IjA3MDUzNDI3ZDk4NjRlZGE4MDJkNmRmYjRjMWVmNWIxIiwidXNlcm5hbWUiOiJhZHJpYW4ifQ.gTUoMitAnzeXXJKCwkx14w1AOHqyH2mfeHjMwCgj3Ps"
    }

    res = requests.delete(url=url,headers=headers)

    print(res.status_code)
    print(res.url)
    print(res.text)

# got adrian and remove costica




if __name__ == "__main__":
    if sys.argv[1] == 'create_blog':
        create_blog()

    elif sys.argv[1] == 'list_blogs':
        list_blogs()

    elif sys.argv[1] == 'update_blog':
        update_blog()
    
    elif sys.argv[1] == 'remove_blog':
        remove_blog()

    else:
        exit(0) 

