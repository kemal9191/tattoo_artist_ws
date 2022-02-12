from ast import In
from wtforms import FileField, StringField, SubmitField
from flask_ckeditor import CKEditorField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired

class PostForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    content = CKEditorField('Content')
    image = FileField('Post Image')
    submit = SubmitField('Save')


class TattooForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    image = FileField('Tattoo Image')