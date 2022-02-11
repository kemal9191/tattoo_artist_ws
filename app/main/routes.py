from flask import Blueprint, url_for, render_template, request, redirect
from app.models import Tattoo

main = Blueprint("main", __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template("layout.html", title="Home")


@main.route('/about-us')
def about():
    return render_template('about.html',title="About Us")


@main.route('/gallery')
def gallery():
    return render_template('gallery.html', title="Gallery")


@main.route('/contact-us')
def contact():
    return render_template('contact.html', title="Contact Us")