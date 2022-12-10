# 12 月ハッカソン　バックエンド RESTAPI 仕様書

## ステータスコード

下記のコードを返却します。

| ステータスコード | 説明                      |
| ---------------- | ------------------------- |
| 200              | リクエスト成功            |
| 404              | 存在しない URL にアクセス |
| 405              | 許可されていないメソッド  |
| 500              | 不明なエラー              |

## ランキング情報の取得

```
GET /getRankingInfo
```

### Request

クエリパラメータ不要

### Response の具体例

```
HTTP/1.1 200 OK
[
  {
    "correct": 53, //正解数
    "incorrect": 51, //誤答数
    "user_number": 1 //ユーザー
  }
]
```

## 回答情報の登録

```
POST /recordRankingInfo
```

### Request

```
{
    "user_number":(int ログイン成功時に帰ってくる番号です)
    "iscorrect":(正解ならtrue 不正解ならfalse)
}
```

### Response

```
HTTP/1.1 200 OK
{
    "result":success"
}

or

{
    "result":failed"
}
基本的にfailedになり得ない
```

## ログイン

```
POST /login
```

### Request

```
{
    "user":ユーザーID
    "password":パスワード
}
```

### Response

```
{
    "result":"success"
    "user_number":ユーザーIDに対応する番号
}

失敗時
{
    "result":"failed"
}
```

## ユーザー登録

```
POST /createUser
```

### Request

```
{
    "user":ユーザー名
    "password":パスワード
    "handleName":ハンドルネーム
}
```

### Response

```
{
    "result":"success"
}

or
{
    "result":"failed"
}

同じユーザー名が存在するとき、登録失敗する仕様
```
