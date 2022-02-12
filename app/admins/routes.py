from flask import redirect, url_for, render_template,request, flash, Blueprint
from app import db
from app.models import Tattoo
from app.admins.forms import PostForm

admins = Blueprint("admins", __name__)

@admins.route('/admin')
def admin_home():
    return "This is admin page"


@admins.route('/create_post')
def create_post():
    form = PostForm()
    return render_template("create_post.html", form=form)