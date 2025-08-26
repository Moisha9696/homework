from flask import abort
from models import Post, db


class PostService:
    @staticmethod
    def get_all_posts():
        return Post.query.all()

    @staticmethod
    def get_post_by_id(post_id):
        post = Post.query.get(post_id)
        if not post:
            abort(404)
        return post

    @staticmethod
    def create_post(title, content):
        if not title or not content:
            raise ValueError("Title and content cannot be empty")

        new_post = Post(title=title, content=content)
        db.session.add(new_post)
        db.session.commit()
        return new_post

    @staticmethod
    def update_post(post_id, title, content):
        post = PostService.get_post_by_id(post_id)

        if not title or not content:
            raise ValueError("Title and content cannot be empty")

        post.title = title
        post.content = content
        db.session.commit()
        return post

    @staticmethod
    def delete_post(post_id):
        post = PostService.get_post_by_id(post_id)
        db.session.delete(post)
        db.session.commit()
        return post_id