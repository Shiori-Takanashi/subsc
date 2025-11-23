from flask import jsonify, request
from app.blueprints.api import api_bp
from app.blueprints.api.schemas import PostSchema, UserSchema
from app.services.post_service import PostService
from app.services.user_service import UserService


post_schema = PostSchema()
posts_schema = PostSchema(many=True)
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@api_bp.route('/posts', methods=['GET'])
def get_posts():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    posts = PostService.get_all_posts(page=page, per_page=per_page)
    return jsonify(posts_schema.dump(posts.items))


@api_bp.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = PostService.get_post_by_id(post_id)
    if not post:
        return jsonify({'error': 'Post not found'}), 404
    return jsonify(post_schema.dump(post))


@api_bp.route('/posts', methods=['POST'])
def create_post():
    data = request.get_json()

    post = PostService.create_post(
        title=data.get('title'),
        content=data.get('content'),
        author_id=data.get('author_id')
    )
    return jsonify(post_schema.dump(post)), 201


@api_bp.route('/users', methods=['GET'])
def get_users():
    users = UserService.get_all_users()
    return jsonify(users_schema.dump(users))


@api_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = UserService.get_user_by_id(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user_schema.dump(user))
