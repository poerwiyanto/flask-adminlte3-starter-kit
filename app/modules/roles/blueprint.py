from .forms import Form
from .models import Role, db
from app.utils.decorators import breadcrumb
from app.utils.flash_msgs import ADDED_MSG, EDITED_MSG
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_babel import _
from flask_menu import register_menu

mod_roles = Blueprint('roles', __name__, url_prefix='/roles')


@mod_roles.route('/')
@breadcrumb(_('Grup'))
@register_menu(mod_roles, 'rbac', _('Hak akses'))
@register_menu(mod_roles, 'rbac.roles', _('Grup'))
def index():
    """Roles list."""
    roles = Role.query.all()

    return render_template(
        'roles/index.html',
        data=roles,
        title=_('Grup'))


@mod_roles.route('/add', methods=['GET', 'POST'])
@breadcrumb('{!s} {!s}'.format(_('Tambah'), _('Grup')))
def add():
    """Add a new role."""
    form = Form()
    if form.validate_on_submit():
        role = Role(name=form.name.data)
        db.session.add(role)
        db.session.commit()

        flash(ADDED_MSG.format(form.name.data), 'success')

        return redirect(url_for('roles.index'))

    return render_template(
        'roles/form.html',
        action=url_for('roles.add'),
        form=form,
        submit_text=_('Tambah'),
        title='{!s} {!s}'.format(_('Tambah'), _('Grup')))


@mod_roles.route('/edit/<int:id>', methods=['GET', 'POST'])
@breadcrumb('{!s} {!s}'.format(_('Ubah'), _('Grup')))
def edit(id):
    """Edit a role."""
    form = Form()
    role = Role.query\
        .filter_by(id=id)\
        .first()

    # Prepopulate the form.
    if request.method == 'GET':
        form.name.data = role.name

    if form.validate_on_submit():
        role.name = form.name.data
        db.session.commit()

        flash(EDITED_MSG.format(form.name.data), 'success')

        return redirect(url_for('roles.index'))

    return render_template(
        'roles/form.html',
        action=url_for('roles.edit', id=id),
        form=form,
        submit_text=_('Ubah'),
        title='{!s} {!s}'.format(_('Ubah'), _('Grup')))
