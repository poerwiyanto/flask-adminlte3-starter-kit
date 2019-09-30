from .forms import LoginForm, RegisterForm
from .models import User, db
from app import app
from app.utils.decorators import breadcrumb, is_logged_in
from app.utils.flash_msgs import FAILED_LOGIN, REGISTERED_MSG
from flask import\
    Blueprint, flash, redirect, render_template, request, session, url_for
from flask_babel import _
import bcrypt

mod_index = Blueprint('index', __name__, url_prefix='/')


@mod_index.route('/')
@is_logged_in
@breadcrumb('Home')
def index():
    print(session)
    print(app.permanent_session_lifetime)

    return render_template(
        'index/index.html',
        title=_('Beranda'))


@mod_index.route('/login', methods=['GET', 'POST'])
def login():
    """Construct login form and validate login."""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query\
            .filter_by(username=request.form['username'])\
            .first()
        if user is not None and bcrypt.checkpw(
                request.form['password'].encode('utf-8'),
                user.password.encode('utf-8')):
            # Set user session and its lifetime.
            if 'remember' in request.form:
                session.permanent = True
            else:
                session.permanent = False
            session['user'] = {
                'id': user.id,
                'name': user.name
            }

            # Redirect to defined url or index.
            if request.form['redirect'] != '':
                return redirect(request.form['redirect'])
            return redirect(url_for('index.index'))
        else:
            flash(FAILED_LOGIN, 'error')

    return render_template(
        'index/login.html',
        form=form)


@mod_index.route('/logout')
def logout():
    """Pop necessary session keys."""
    session.pop('breadcrumbs', None)
    session.pop('user', None)

    return redirect(url_for('index.login'))


@mod_index.route('/register', methods=['GET', 'POST'])
def register():
    """Construct registration form and register a new user."""
    form = RegisterForm()
    if form.validate_on_submit():
        # Hash password using bcrypt.
        hashed_password = bcrypt.hashpw(
            request.form['password'].encode('utf-8'),
            bcrypt.gensalt())
        user = User(
            name=request.form['name'],
            password=hashed_password,
            status='active',
            username=request.form['username'])
        db.session.add(user)
        db.session.commit()

        flash(REGISTERED_MSG.format(_('Pengguna')), 'success')

        return redirect(url_for('index.login'))

    return render_template(
        'index/register.html',
        form=form)
