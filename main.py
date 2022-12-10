from flask import *
import dbaccess


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'


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

    try:
        dbaccess.create_user(user, password, handleName)
    except Exception as e:
        print(f'e is {e}')
        return jsonify({'result': 'failed'})

    return jsonify({'result': 'success'})


@app.route('/login', methods=['POST'])
def login():
    user = request.form['user']
    password = request.form['password']

    if dbaccess.login(user, password):
        num = dbaccess.get_user_number(user)
        return jsonify({'result': 'success', 'user_number': num})
    else:
        return jsonify({'result': 'failed'})


if __name__ == '__main__':
    app.run(debug=True)
