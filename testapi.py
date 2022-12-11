import requests
import random

URL = "http://localhost:21345/"


def login():
    url = f'{URL}login'
    data = {'user': 'admin', 'password': 'admin'}
    # data = {'user': 'admin', 'password': 'adminnnnn'}

    r = requests.post(url, data=data)

    res = r.json()

    print(res)


def post2():
    url = f'{URL}login'
    data = {'user': 'admin2', 'password': 'adminn', 'handleName': 'admin'}

    r = requests.post(url, data=data)
    print(r.text)


def recordRanking():
    url = f'{URL}recordRankingInfo'
    data = {'user_number': '1', 'iscorrect': random.random() > 0.5}

    r = requests.post(url, data=data)
    print(r.text)


def logout():
    url = f'{URL}logout'

    r = requests.get(url)
    print(r.text)


if __name__ == '__main__':

    # for _ in range(100):
    #     recordRanking()

    login()

    logout()
