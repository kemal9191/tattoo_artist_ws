from flask import Blueprint, jsonify, url_for, render_template, request, redirect, flash
from app.models import Tattoo
from app.main.forms import ContactForm

main = Blueprint("main", __name__)

@main.route('/')
@main.route('/home')
def home():
    return render_template("home.html", title="Home")


@main.route('/some-fe')
def some_fe():
    return jsonify({
        "content":"this is some repsonse"
    })


@main.route('/about-us')
def about():
    return render_template('about.html',title="About Us")


@main.route('/gallery')
def gallery():
    tattoos = Tattoo.query.all()
    return render_template('gallery.html', title="Gallery", tattoos=tattoos)


@main.route('/contact-us', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Your request has been successfully submitted', 'success')
        return redirect(url_for('main.home'))
    return render_template('contact.html', title="Contact Us", form=form)


