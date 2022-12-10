import psycopg2
from psycopg2.extras import DictCursor
import itertools

DATABASE_URL = "postgresql://postgres:Password@localhost:25432/postgres"


def get_connection():
    return psycopg2.connect(DATABASE_URL)


def get_dict_resultset(sql):
    conn = get_connection()
    cur = conn.cursor(cursor_factory=DictCursor)
    cur.execute(sql)
    results = cur.fetchall()
    dict_result = []
    for row in results:
        dict_result.append(dict(row))
    return dict_result


def get_users_number():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT user_number FROM userinfo")
    rows = cur.fetchall()

    # 二次元配列を一次元に　user_numberのlistを返す
    return list(itertools.chain.from_iterable(rows))


def create_user(id, password, handleName):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO userinfo(user_id,handleName,password) VALUES (%s, %s, %s) RETURNING user_number",
                (id, password, handleName))

    conn.commit()

    row = cur.fetchone()
    conn.close()
    if row is None:
        return False
    else:
        return True


def login(id, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM userinfo WHERE user_id = %s AND password = %s", (id, password))

    row = cur.fetchone()

    if row is None:
        return False
    else:
        return True


def get_user_number(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT user_number FROM userinfo WHERE user_id = %s", (user_id,))

    (num,) = cur.fetchone()

    return num


def select_user():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM userinfo")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    conn.close()


def get_ranking():
    sql = "SELECT * FROM ranking"
    rows = get_dict_resultset(sql)
    user_numbers = get_users_number()

    print(rows)
    print(user_numbers)

    res = []

    for user_number in user_numbers:
        res.append({'user_number': user_number, 'correct': 0, 'incorrect': 0})

    for row in rows:
        for r in res:
            if r['user_number'] == row['user_number']:
                if row['iscorrect'] == True:
                    r['correct'] += 1
                else:
                    r['incorrect'] += 1

    res.sort(key=lambda x: x['correct'], reverse=True)

    return res


def record_ranking(user_number, iscorrect):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO ranking(user_number,iscorrect) VALUES (%s, %s)",
                (user_number, iscorrect))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    # get_users_number()
    # select_user()
    # res = get_ranking()
    # print(res)

    print(get_user_number('admin'))
