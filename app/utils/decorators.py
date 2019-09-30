from flask import redirect, request, session, url_for
from functools import wraps


def breadcrumb(text):
    def func(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            """Historical breadcrumbs."""
            if 'breadcrumbs' not in session:
                session['breadcrumbs'] = []
            if len(session['breadcrumbs']) == 0 or\
               request.url != session['breadcrumbs'][-1]['url']:
                session['breadcrumbs'].append({
                    'text': text,
                    'url': request.url
                })
            # Keep number of breadcrumbs not more than 5.
            if len(session['breadcrumbs']) > 5:
                session['breadcrumbs'].pop(0)
            session.modified = True

            return f(*args, **kwargs)
        return wrapper
    return func


def is_logged_in(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if 'user' in session:
            return f(*args, **kwargs)

        return redirect('{!s}?redirect={!s}'.format(
            url_for('index.login'), request.url))
    return wrapper
