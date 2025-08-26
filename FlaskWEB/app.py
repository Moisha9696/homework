from flask_migrate import Migrate
from models import db, Post
from services.post_service import PostService
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()


@app.before_request
def method_override():
    if request.method == 'POST' and '_method' in request.form:
        method = request.form['_method'].upper()
        if method in ['PUT', 'DELETE', 'PATCH']:
            request.environ['REQUEST_METHOD'] = method

@app.route('/')
def index():
    posts = PostService.get_all_posts()
    return render_template('index.html', posts=posts)

@app.route('/create', methods=['POST'])
def create():
    try:
        print(f"create")
        title = request.form['title']
        content = request.form['content']

        new_post = PostService.create_post(title, content)
        return render_template('post_snippet.html', post=new_post)
    except ValueError as e:
        print(f"Validation error: {e}")
        return '', 400
    except Exception as e:
        print(f"Error occurred: {e}")

        return '', 500  # Return an error response

@app.route('/post/<int:post_id>')
def post(post_id):
    post = PostService.get_post_by_id(post_id)
    return render_template('post.html', post=post)


@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        try:
            title = request.form['title']
            content = request.form['content']

            PostService.update_post(post_id, title, content)
            return redirect(url_for('post', post_id=post_id))

        except ValueError as e:
            print(f"Validation error: {e}")
            return render_template('edit_post.html', post=post, error=str(e))

    return render_template('edit_post.html', post=post)

@app.route('/delete/<int:post_id>', methods=['POST', 'DELETE'])
def delete(post_id):
    try:
        deleted_post_id = PostService.delete_post(post_id)
        return f'<div id="post-{deleted_post_id}"></div>'
    except Exception as e:
        print(f"Error deleting post: {e}")
        return '', 500

if __name__ == '__main__':
    app.run(debug=True)