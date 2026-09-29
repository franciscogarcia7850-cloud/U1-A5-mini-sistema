from functools import wraps

from flask import session, flash, redirect, url_for


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            flash('Tienes que iniciar sesión para entrar a esa página', 'warning')
            return redirect(url_for('users.login'))
        return f(*args, **kwargs)
    return decorated
