'''app'''
from datetime import datetime
import uuid
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bdCJR.db'
app.secret_key = '2270a8a08878bc7736d27c028f4398654fcc332869df97825516ea68666620b0'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    user_id = db.Column(db.String(50), primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(5))
    email = db.Column(db.String(250), nullable=False)
    cargo = db.Column(db.String(250))
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    @property
    def is_authenticated(self):
        return True
    def get_id(self):
        return self.user_id


class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(50), nullable=False)
    content = db.Column(db.String(250), nullable=False)
    updated_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)
    created_at = db.Column(db.TIMESTAMP, default=datetime.utcnow)

class Comments(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.String(50), nullable=False)
    content_coments = db.Column(db.String(100))

def generate_user_id():
    return str(uuid.uuid4())

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        user_id = generate_user_id()
        username = request.form['registration']
        senha = request.form['password']
        gender = request.form['gender']
        email = request.form['email']
        cargo = request.form['cargo']

        new_user = User(user_id=user_id, username=username, senha=senha, gender=gender, email=email, cargo=cargo)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['registration']
        password = request.form['password']
        user = User.query.filter_by(username=username, senha=password).first()
        if user:
            login_user(user)
            return redirect(url_for('feed'))
        else:
            return redirect(url_for('login'))
        
    return render_template('login.html')

@app.route('/recup', methods=['GET', 'POST'])
def recup():
    if request.method == 'POST':
        username = request.form['registration']
        user = User.query.filter_by(username=username).first()
        new_password = request.form['password']
        new_password_confirm = request.form['password-confirm']
        if new_password == new_password_confirm:
            user.senha = new_password
            db.session.commit()
            return redirect(url_for('login'))
            
        else:
            return render_template('recup.html')

    return render_template('recup.html')

@app.route('/feed')
def feed():
    posts = Post.query.all()
    if current_user.is_authenticated:
        return render_template('feed.html', username=current_user.username, posts=posts)
    else:
        return render_template('feed.html', username=None, posts=posts)

@app.route('/perfil_usuario')
@login_required
def perfil_usuario():
    return render_template('perfil_usu.html', username=current_user.username)

@app.route('/post_aberto/<int:post_id>')
@login_required
def post_aberto(post_id):
    post = Post.query.get(post_id)
    comments = Comments.query.filter_by(post_id=post_id).all()
    if post:
        return render_template('post_aberto.html', post=post, comment=comments)


@app.route('/create_post', methods=['POST'])
def create_post():
    data = request.get_json()
    content = data['content']
    username = data['currentUsername']
    new_post = Post(user_id=username, content=content)
    db.session.add(new_post)
    db.session.commit()

    return jsonify({
        'post_id': new_post.post_id,
        'user_id': new_post.user_id,
        'content': new_post.content,
        'created_at': new_post.created_at.strftime('%Y-%m-%d %H:%M:%S')
    })

@app.route('/create_comment', methods=['POST'])
def create_comment():
    data = request.get_json()
    content = data['content']
    username = data['currentUsername']
    post_id = data['post_id']
    new_comment = Comments(post_id=post_id, user_id=username, content_coments=content)
    db.session.add(new_comment)
    db.session.commit()

    return jsonify({
        'post_id': new_comment.comment_id,
        'user_id': new_comment.user_id,
        'content': new_comment.content_coments
    })

@app.route('/editar_post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def editar_post(post_id):
    post = Post.query.get(post_id)
    if request.method == 'POST':
        new_content = request.form['content']
        post.content = new_content
        db.session.commit()
        return redirect(url_for('feed'))
    return render_template('editar_post.html', post=post)

@app.route('/excluir_post/<int:post_id>')
@login_required
def excluir_post(post_id):
    post = Post.query.get(post_id)
    if post:
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('feed'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)