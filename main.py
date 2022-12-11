from flask import *
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
import dbaccess
import hashlib


app = Flask(__name__)

app.secret_key = b'jugemjugemgokonosurikirekaijarisuigyono'
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin):
    def __init__(self, user_id):
        self.user_id = user_id

    def get_id(self):
        return self.user_id


def calculate_password_hash(password):
    # https://zenn.dev/ikaro1192/books/999b71a570cb89024716/viewer/b12daf947c46f9ce44e9
    text = password.encode('utf-8')
    result = hashlib.sha512(text).hexdigest()
    return result


@app.route('/')
def index():
    return 'Hello World'


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.route('/getRankingInfo', methods=['GET'])
def getRankingInfo():
    return jsonify(dbaccess.get_ranking())


@app.route('/recordRankingInfo', methods=['POST'])
def recordRankingInfo():
    user_number = request.form['user_number']
    iscorrect = request.form['iscorrect']

    try:
        dbaccess.record_ranking(user_number, iscorrect)
    except Exception as e:
        print(f'e is {e}')
        return jsonify({'result': 'failed'})

    return jsonify({'result': 'success'})


@app.route('/createUser', methods=['POST'])
def createUser():
    user = request.form['user']
    password = request.form['password']
    handleName = request.form['handleName']

    sha512_password = calculate_password_hash(password)

    try:
        dbaccess.create_user(user, sha512_password, handleName)
    except Exception as e:
        print(f'e is {e}')
        return jsonify({'result': 'failed'})

    return jsonify({'result': 'success'})


@app.route('/login', methods=['GET', 'POST'])
def login():
    # パスワードを平文で送っているので、注意。対策を後で考える。
    # GETメソッドはデバッグ用、実運用では使用しない。

    if request.method == 'GET':
        user = request.args.get('user')
        password = request.args.get('password')

    else:
        user = request.form['user']
        password = request.form['password']

    sha512_password = calculate_password_hash(password)

    if dbaccess.login(user, sha512_password):
        num = dbaccess.get_user_number(user)
        handleName = dbaccess.get_user_handleName(user)
        loginUser = User(num)
        print(loginUser)
        login_user(loginUser)
        return jsonify({'result': 'success', 'user_number': num, 'handleName': handleName})
    else:
        return jsonify({'result': 'failed'})


@ app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()

    return jsonify({'result': 'logout'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
