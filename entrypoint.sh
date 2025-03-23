#!/bin/bash

# DB migrationを実行する
poetry run python -m api.migrate_cloud_db

# uvicormを立ち上げる
# ローカル用（--reloadでホットリロードを有効）
# poetry run uvicorn api.main:app --host 0.0.0.0 --reload

# クラウドデプロイ用（ホットリロード無効）
poetry run uvicorn api.main:app --host 0.0.0.0