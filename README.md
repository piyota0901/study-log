# Study-Log
勉強記録アプリ  
学習用にアプリを作成してみる

## 構成
- バックエンド(python)
  - FastAPI
    - https://fastapi.tiangolo.com/ja/
- フロントエンド
  - React or Vue

## 前提条件
- Python 3.8.10

## ツール
- poetry
  - https://cocoatomo.github.io/poetry-ja/
  - pythonの依存関係管理とパッケージングのためのツール

## Poetry使い方
https://python-poetry.org/docs/configuration/#displaying-a-single-configuration-setting
```bash
tatsuro@tatsuro-surface:~/development/study-log$ poetry init

This command will guide you through creating your pyproject.toml config.

Package name [study-log]:  
Version [0.1.0]:  
Description []:  
Author [piyota0901 <piyo.tatsu.0901@gmail.com>, n to skip]:  
License []:  
Compatible Python versions [^3.8]:  

Would you like to define your main dependencies interactively? (yes/no) [yes] 
You can specify a package in the following forms:
  - A single name (requests)
  - A name and a constraint (requests@^2.23.0)
  - A git url (git+https://github.com/python-poetry/poetry.git)
  - A git url with a revision (git+https://github.com/python-poetry/poetry.git#develop)
  - A file path (../my-package/my-package.whl)
  - A directory (../my-package/)
  - A url (https://example.com/packages/my-package-0.1.0.tar.gz)

Search for package to add (or leave blank to continue): 

Would you like to define your development dependencies interactively? (yes/no) [yes] 
Search for package to add (or leave blank to continue): 

Generated file

[tool.poetry]
name = "study-log"
version = "0.1.0"
description = ""
authors = ["piyota0901 <piyo.tatsu.0901@gmail.com>"]

[tool.poetry.dependencies]
python = "^3.8"

[tool.poetry.dev-dependencies]

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"


Do you confirm generation? (yes/no) [yes] 
tatsuro@tatsuro-surface:~/development/study-log$ poetry install
Updating dependencies
Resolving dependencies... (0.1s)

Writing lock file
No dependencies to install or update
```
- vscodeにpoetryを認識させる
  - https://zenn.dev/pesuchin/articles/4c128aeb60cb42204311
  - `setting.json`
    ```json
    {
      "python.defaultInterpreterPath": "/home/xxxxxxx/.cache/pypoetry/virtualenvs/study-log-h5lKZ4xv-py3.8/bin/python",
    }
    ```

## 各構成
---------------------

### バックエンド
- FastAPI
  - https://fastapi.tiangolo.com/tutorial/bigger-applications/

- Pydantic
  - https://pydantic-docs.helpmanual.io/usage/types/

### 開発時
- サーバ起動
  ```bash
  $ uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
  ```

### その他
- isortの有効化
  ```json
  {
    "editor.codeActionsOnSave": {
          "source.organizeImports": true
      }
  }
  ```
- sqlalchemyのUpdate
  - propertyを書き換える
  - settarr()が便利
    - https://github.com/tiangolo/fastapi/discussions/2561
    ```python
    update_data = updates.dict(exclude_unset=True)
    for key, value in update_data.items():
      setattr(item, key, value)
    ```

### JWT

- 有効期限(expire)は、`jwt.decode`時に検証される
- `jose.exceptions.ExpiredSignatureError: Signature has expired`エラーがスローされる
```bash
>>> from jose import jwt
>>> import datetime
>>> datetime.datetime.now()
datetime.datetime(2022, 7, 12, 21, 51, 3, 524089)
>>> datetime.datetime.utcnow()
datetime.datetime(2022, 7, 12, 12, 51, 17, 210806)
>>> to_encode = {"sub":"sample", "exp": datetime.utcnow()}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'datetime' has no attribute 'utcnow'
>>> to_encode = {"sub":"sample", "exp": datetime.datetime.utcnow()}
>>> jwt.encode(to_encode, "secret", algorithm="HS256")
'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJzYW1wbGUiLCJleHAiOjE2NTc2MzA5MjR9._zjLE3vw1J4aikvagwK-wyd9GOKcAihKYoAsb2GKBYQ'
>>> token = jwt.encode(to_encode, "secret", algorithm="HS256")
>>> jwt.decode(token, "secret", algorithms="HS256")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/tatsuro/.cache/pypoetry/virtualenvs/study-log-h5lKZ4xv-py3.8/lib/python3.8/site-packages/jose/jwt.py", line 157, in decode
    _validate_claims(
  File "/home/tatsuro/.cache/pypoetry/virtualenvs/study-log-h5lKZ4xv-py3.8/lib/python3.8/site-packages/jose/jwt.py", line 481, in _validate_claims
    _validate_exp(claims, leeway=leeway)
  File "/home/tatsuro/.cache/pypoetry/virtualenvs/study-log-h5lKZ4xv-py3.8/lib/python3.8/site-packages/jose/jwt.py", line 314, in _validate_exp
    raise ExpiredSignatureError("Signature has expired.")
jose.exceptions.ExpiredSignatureError: Signature has expired.
>>> 
```
- jwt(ジョット)
  - pythonだとjose（fastapi情報）
  - https://pyjwt.readthedocs.io/en/latest/usage.html
  - https://pyjwt.readthedocs.io/en/latest/api.html
  - Header.Payload.署名の3情報をつなげた文字列
    - Header
      - JSON文字列
        ```json
        {
          "typ": "JWT",
          "alg": "HS256"
        }
        ```
      - joseでは気にしなくてよい。自動的に設定される.
    - Payload(クレーム)
      - 任意のデータを含むJSON文字列
      - 予約済みのキー
        - "iss" (Issuer) Claim
        - "sub" (Subject) Claim
        - "aud" (Audience) Claim
        - "exp" (Expiration Time) Claim
        - "nbf" (Not Before) Claim
        - "iat" (Issued At) Claim
        - "jti" (JWT ID) Claim
      - 必ずしも使用する必要はない
      - "exp"
        - joseではencode時にexpを検証してくれる
          - `verify_exp`パラメータでoffにもできる
      - "iss"
        ```python
        payload = {"some": "payload", "iss": "urn:foo"}

        token = jwt.encode(payload, "secret")
        decoded = jwt.decode(token, "secret", issuer="urn:foo", algorithms=["HS256"])
        ```
        ※issuerが正しくない場合、jwt.InvalidIssuerErrorがスローされる
  - claimを必須にする方法
    ```
    Requiring Presence of Claims
    If you wish to require one or more claims to be present in the claimset,  you can set the require parameter to include these claims. 
    ```
    ```python
    >>> jwt.decode(encoded, options={"require": ["exp", "iss", "sub"]})
    {'exp': 1371720939, 'iss': 'urn:foo', 'sub': '25c37522-f148-4cbf-8ee6-c4a9718dd0af'}
    ```
- role base access control
  - https://github.com/vineetkarandikar/aws-samples/blob/main/auth.py