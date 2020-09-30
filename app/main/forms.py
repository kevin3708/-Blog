from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class BlogForm(FlaskForm):
    title = StringField('Blog Title',validators=[Required()])
    post = TextAreaField('Blog Post',validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):

    title = StringField('Comment title',validators=[Required()])
    comment = TextAreaField('Blog comment',validators=[Required()])
    submit = SubmitField('Submit')