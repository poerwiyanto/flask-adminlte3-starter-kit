from app.utils.decorators import breadcrumb
from flask import Blueprint, render_template
from flask_babel import _
from flask_menu import register_menu

mod_roles = Blueprint('roles', __name__, url_prefix='/roles')


@mod_roles.route('/')
@breadcrumb(_('Grup'))
@register_menu(mod_roles, '.users.roles', _('Grup'))
def index():
    return render_template(
        'index/index.html',
        title=_('Beranda'))
