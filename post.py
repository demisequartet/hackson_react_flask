import requests
import random


def login():
    url = 'http://localhost:5000/login'
    data = {'user': 'admin', 'password': 'admin'}
    # data = {'user': 'admin', 'password': 'adminnnnn'}

    r = requests.post(url, data=data)

    res = r.json()

    print(res)


def post2():
    url = 'http://localhost:5000/createUser'
    data = {'user': 'admin2', 'password': 'adminn', 'handleName': 'admin'}

    r = requests.post(url, data=data)
    print(r.text)


def recordRanking():
    url = 'http://localhost:5000/recordRankingInfo'
    data = {'user_number': '1', 'iscorrect': random.random() > 0.5}

    r = requests.post(url, data=data)
    print(r.text)


if __name__ == '__main__':

    # for _ in range(100):
    #     recordRanking()

    login()
