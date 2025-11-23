"""初期データのロード"""
import json
import os
from app.extensions.db import db
from app.models.user import User
from app.models.post import Post


def load_seed_data():
    """JSONファイルから初期データを読み込んでデータベースに登録"""
    # ユーザーが既に存在する場合はスキップ
    if User.query.count() > 0:
        return

    # JSONファイルのパスを取得
    json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'seed_data.json')

    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # ユーザーを作成
    user_map = {}
    for user_data in data['users']:
        user = User(
            username=user_data['username'],
            email=user_data['email']
        )
        user.set_password(user_data['password'])
        db.session.add(user)
        user_map[user_data['username']] = user

    db.session.commit()

    # 投稿を作成
    for post_data in data['posts']:
        author = user_map[post_data['author_username']]
        post = Post(
            title=post_data['title'],
            content=post_data['content'],
            author_id=author.id
        )
        db.session.add(post)

    db.session.commit()

    print("初期データを作成しました")
    print("ログイン情報: admin@example.com / password123")
