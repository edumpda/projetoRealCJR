'''app'''
from datetime import datetime
import uuid
from flask import Flask, render_template, request, redirect, url_for
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
        new_password = request.form['password']
        user.senha = new_password
        db.session.commit()
        return redirect(url_for('login'))


    return render_template('recup.html')

@app.route('/feed')
def feed():
    if current_user.is_authenticated:
        return render_template('feed.html', username=current_user.username)
    else:
        return render_template('feed.html', username=None)

@app.route('/perfil')
@login_required
def perfil_usuario():
    return render_template('perfil_usuario.html', username=current_user.username)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)