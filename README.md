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