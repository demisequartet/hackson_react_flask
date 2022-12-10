import requests


def post():
    url = 'http://localhost:5000/login'
    data = {'user': 'admin', 'password': 'adminn'}
    r = requests.post(url, data=data)
    print(r.text)


def post2():
    url = 'http://localhost:5000/createUser'
    data = {'user': 'admin2', 'password': 'adminn', 'handleName': 'admin'}

    r = requests.post(url, data=data)
    print(r.text)

def recordRanking():
    url = 'http://localhost:5000/'
    data = {'user_number': '1', 'iscorrect': 'True'}

    r = requests.post(url, data=data)
    print(r.text)

if __name__ == '__main__':
    post2()
