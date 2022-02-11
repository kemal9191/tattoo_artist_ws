from flask import redirect, url_for, render_template,request, flash, Blueprint
from app import db
from app.models import Tattoo

admins = Blueprint("admins", __name__)

@admins.route('/admin')
def admin_home():
    return "This is admin page"