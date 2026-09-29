from flask import Blueprint, render_template, redirect, url_for, flash, session

from bd import db
from models.user import User
from forms import RegisterForm, LoginForm, EditProfileForm
from decorators import login_required

users_bp = Blueprint('users', __name__)


def usuario_repetido(username, email, id=0):
    # Busca a otro usuario que ya tenga ese nombre de usuario o ese correo
    return User.query.filter(User.id != id, (User.username == username) | (User.email == email)).first()


@users_bp.route('/')
def index():
    users = User.query.all()
    return render_template('user_list.html', users=users)


@users_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if usuario_repetido(form.username.data, form.email.data):
            flash('Ese usuario o correo ya está registrado', 'danger')
        else:
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Usuario registrado, ya puedes iniciar sesión', 'success')
            return redirect(url_for('users.login'))
    elif form.errors:
        flash('Revisa los datos del formulario', 'danger')
    return render_template('register.html', form=form)


@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Bienvenido ' + user.username, 'success')
            return redirect(url_for('users.profile', id=user.id))
        flash('Usuario o contraseña incorrectos', 'danger')
    return render_template('login.html', form=form)


@users_bp.route('/logout')
def logout():
    session.clear()
    flash('Cerraste sesión', 'info')
    return redirect(url_for('users.index'))


@users_bp.route('/profile/<int:id>')
@login_required
def profile(id):
    user = db.get_or_404(User, id)
    return render_template('profile.html', user=user)


@users_bp.route('/profile/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_profile(id):
    if session['user_id'] != id:
        flash('Solo puedes editar tu propio perfil', 'danger')
        return redirect(url_for('users.profile', id=id))

    user = db.get_or_404(User, id)
    form = EditProfileForm(obj=user)
    if form.validate_on_submit():
        if usuario_repetido(form.username.data, form.email.data, id):
            flash('Ese usuario o correo ya está registrado', 'danger')
        else:
            user.username = form.username.data
            user.email = form.email.data
            db.session.commit()
            session['username'] = user.username
            flash('Perfil actualizado', 'success')
            return redirect(url_for('users.profile', id=id))
    elif form.errors:
        flash('No se pudo actualizar el perfil, revisa los datos', 'danger')
    return render_template('edit_profile.html', form=form, user=user)


@users_bp.route('/profile/<int:id>/delete', methods=['POST'])
@login_required
def delete_user(id):
    if session['user_id'] != id:
        flash('Solo puedes eliminar tu propia cuenta', 'danger')
        return redirect(url_for('users.profile', id=id))

    user = db.get_or_404(User, id)
    db.session.delete(user)
    db.session.commit()
    session.clear()
    flash('Usuario eliminado', 'success')
    return redirect(url_for('users.index'))
