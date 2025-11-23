# Flask Blog Application

Flask を使用したブログアプリケーション。ユーザー認証、投稿管理、REST API を備えた完全な Web アプリケーションです。

## 機能

- **ユーザー認証**: ログイン、登録、ログアウト
- **ブログ機能**: 投稿の作成、編集、削除、一覧表示、詳細表示
- **REST API**: JSON 形式でのデータアクセス（ユーザー、投稿）
- **権限管理**: 自分の投稿のみ編集・削除可能
- **レスポンシブデザイン**: モダンな UI/UX

## プロジェクト構成

```
project/
├── app/
│   ├── __init__.py              # アプリケーションファクトリー
│   ├── config.py                # 設定ファイル
│   ├── extensions/              # Flask 拡張機能
│   │   ├── db.py               # SQLAlchemy
│   │   ├── cache.py            # Flask-Caching
│   │   └── login.py            # Flask-Login
│   ├── blueprints/             # Blueprint モジュール
│   │   ├── auth/               # 認証機能
│   │   ├── blog/               # ブログ機能
│   │   └── api/                # REST API
│   ├── services/               # ビジネスロジック層
│   │   ├── user_service.py
│   │   └── post_service.py
│   ├── models/                 # データモデル
│   │   ├── user.py
│   │   └── post.py
│   ├── utils/                  # ユーティリティ
│   │   └── seed.py            # 初期データロード
│   ├── data/                   # データファイル
│   │   └── seed_data.json     # 初期データ（JSON）
│   ├── templates/              # Jinja2 テンプレート
│   └── static/                 # CSS, JS, 画像
├── tests/                      # テストコード
├── migrations/                 # データベースマイグレーション
├── wsgi.py                     # アプリケーションエントリーポイント
├── pyproject.toml              # プロジェクト設定
└── README.md
```

## セットアップ

### 必要要件

- Python 3.10+
- uv (推奨) または pip

### インストール

1. リポジトリをクローン:
```bash
git clone <repository-url>
cd subsc
```

2. 仮想環境を作成して依存関係をインストール:
```bash
# uv を使用する場合
uv sync

# pip を使用する場合
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 起動方法

```bash
python wsgi.py
```

アプリケーションは `http://127.0.0.1:5000` で起動します。

初回起動時に自動的にデータベースが作成され、サンプルデータが投入されます。

### 初期ログイン情報

```
Email: admin@example.com
Password: password123

Email: test@example.com
Password: password123
```

## API エンドポイント

### 認証 (Auth)

| エンドポイント | メソッド | 説明 | 認証 |
|--------------|---------|------|------|
| `/auth/login` | GET, POST | ログイン | 不要 |
| `/auth/register` | GET, POST | ユーザー登録 | 不要 |
| `/auth/logout` | GET | ログアウト | 必須 |

### ブログ (Blog)

| エンドポイント | メソッド | 説明 | 認証 |
|--------------|---------|------|------|
| `/blog/` | GET | 投稿一覧 | 不要 |
| `/blog/post/<post_id>` | GET | 投稿詳細 | 不要 |
| `/blog/post/create` | GET, POST | 投稿作成 | 必須 |
| `/blog/post/<post_id>/edit` | GET, POST | 投稿編集 | 必須 |
| `/blog/post/<post_id>/delete` | POST | 投稿削除 | 必須 |

### REST API

| エンドポイント | メソッド | 説明 |
|--------------|---------|------|
| `/api/posts` | GET | 投稿一覧取得（JSON） |
| `/api/posts/<post_id>` | GET | 投稿詳細取得（JSON） |
| `/api/posts` | POST | 投稿作成（JSON） |
| `/api/users` | GET | ユーザー一覧取得（JSON） |
| `/api/users/<user_id>` | GET | ユーザー詳細取得（JSON） |

## 初期データのカスタマイズ

初期データを変更するには `app/data/seed_data.json` を編集してください:

```json
{
  "users": [
    {
      "username": "admin",
      "email": "admin@example.com",
      "password": "password123"
    }
  ],
  "posts": [
    {
      "title": "投稿タイトル",
      "content": "投稿内容",
      "author_username": "admin"
    }
  ]
}
```

データベースをリセットして初期データを再投入する場合:

```bash
# データベースファイルを削除
rm instance/app.db

# アプリケーションを起動（自動的に再作成される）
python wsgi.py
```

## 開発

### テストの実行

```bash
pytest
```

### コード構成のポイント

- **アプリケーションファクトリーパターン**: `create_app()` で柔軟な設定が可能
- **Blueprint による機能分割**: 認証、ブログ、API を独立したモジュールとして管理
- **サービス層**: ビジネスロジックをルートから分離
- **データとロジックの分離**: 初期データは JSON、ロードロジックは別ファイル

## 技術スタック

- **Flask**: Web フレームワーク
- **SQLAlchemy**: ORM
- **Flask-Login**: ユーザー認証
- **Flask-WTF**: フォーム処理とバリデーション
- **Flask-Caching**: キャッシング（オプション）
- **Marshmallow**: API シリアライゼーション
- **SQLite**: データベース（開発環境）

## ライセンス

MIT License
