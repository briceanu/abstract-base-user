import requests
import sys



def signup():
    url = 'http://127.0.0.1:8000/user/signup'

    data = {
    'username': 'costica',
    'password': 'ak471989Aionaw',
    'confirm_password': 'ak471989Aionaw',
    'is_married': True,
    'email': 'costica@gmail.com',
    'age':27
}


    res = requests.post(url=url,data=data)

    print(res.status_code)
    print(res.url)
    print(res.text)


def signin():
    url = 'http://127.0.0.1:8000/user/signin'

    data = {
    'username': 'adrian',
    'password': 'ak471989Aionaw'
}


    res = requests.post(url=url,data=data)

    print(res.status_code)
    print(res.url)
    print(res.text)


def new_access():
    url = 'http://127.0.0.1:8000/user/new-accesstoken'  

    headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyODQxMzgzMiwiaWF0IjoxNzI4MzI3NDMyLCJqdGkiOiI0MmI4YWVmMzQ1N2Y0ZGMzOTUwZDhmMDAxODA3ZDk2YiIsInVzZXJuYW1lIjoiaW9uIn0.bhNVbiSFaQ7rIwwoAbnTTjfQZgDmILKxG5MvFvPc6Wc"
    }

    res = requests.post(url=url, headers=headers)

    print(f'Status Code: {res.status_code}')
    print(f'Response URL: {res.url}')
    print(f'Response Text: {res.text}')


def black_list_token():
    url = 'http://127.0.0.1:8000/user/invalidate_token'  

    data = {
     "refresh" : "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyODU4MjUwMywiaWF0IjoxNzI4NDk2MTAzLCJqdGkiOiJjNWUwOTA4ODM5OWQ0MmMzODgzMWQ2ODJlMzYyOGZjOCIsInVzZXJuYW1lIjoibWFyaWFuIn0.edjFf62LulYCzyqC1-4tkkTy9EOIcVZrOnfINOuD5So"
    }

    res = requests.post(url=url, data=data)

    print(f'Status Code: {res.status_code}')
    print(f'Response URL: {res.url}')
    print(f'Response Text: {res.text}')



if __name__ == "__main__":
    if sys.argv[1] == 'signup':
        signup()

    if sys.argv[1] == 'signin':
        signin()
    if sys.argv[1] == 'new_access':
        new_access()
    if sys.argv[1] == 'black_list':
        black_list_token()

    else:
        exit(0) 

