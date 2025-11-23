from app.models.post import Post
from app.extensions.db import db


class PostService:
    @staticmethod
    def get_post_by_id(post_id):
        return Post.query.get(post_id)

    @staticmethod
    def get_all_posts(page=1, per_page=10):
        return Post.query.order_by(Post.created_at.desc()).paginate(
            page=page, per_page=per_page, error_out=False
        )

    @staticmethod
    def get_posts_by_author(author_id, page=1, per_page=10):
        return Post.query.filter_by(author_id=author_id).order_by(
            Post.created_at.desc()
        ).paginate(page=page, per_page=per_page, error_out=False)

    @staticmethod
    def create_post(title, content, author_id):
        post = Post(title=title, content=content, author_id=author_id)
        db.session.add(post)
        db.session.commit()
        return post

    @staticmethod
    def update_post(post_id, **kwargs):
        post = PostService.get_post_by_id(post_id)
        if not post:
            return None

        for key, value in kwargs.items():
            if hasattr(post, key):
                setattr(post, key, value)

        db.session.commit()
        return post

    @staticmethod
    def delete_post(post_id):
        post = PostService.get_post_by_id(post_id)
        if post:
            db.session.delete(post)
            db.session.commit()
            return True
        return False
