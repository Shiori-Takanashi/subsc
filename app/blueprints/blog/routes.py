from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import login_required, current_user
from app.blueprints.blog import blog_bp
from app.services.post_service import PostService


@blog_bp.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    posts = PostService.get_all_posts(page=page, per_page=10)
    return render_template('blog/index.html', posts=posts)


@blog_bp.route('/post/<int:post_id>')
def post_detail(post_id):
    post = PostService.get_post_by_id(post_id)
    if not post:
        abort(404)
    return render_template('blog/post_detail.html', post=post)


@blog_bp.route('/post/create', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        post = PostService.create_post(
            title=title,
            content=content,
            author_id=current_user.id
        )
        flash('Post created successfully!', 'success')
        return redirect(url_for('blog.post_detail', post_id=post.id))

    return render_template('blog/create_post.html')


@blog_bp.route('/post/<int:post_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = PostService.get_post_by_id(post_id)
    if not post:
        abort(404)

    if post.author_id != current_user.id:
        abort(403)

    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')

        PostService.update_post(post_id, title=title, content=content)
        flash('Post updated successfully!', 'success')
        return redirect(url_for('blog.post_detail', post_id=post.id))

    return render_template('blog/edit_post.html', post=post)


@blog_bp.route('/post/<int:post_id>/delete', methods=['POST'])
@login_required
def delete_post(post_id):
    post = PostService.get_post_by_id(post_id)
    if not post:
        abort(404)

    if post.author_id != current_user.id:
        abort(403)

    PostService.delete_post(post_id)
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('blog.index'))
