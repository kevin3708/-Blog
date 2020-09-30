from flask import render_template,redirect,url_for
from . import main
from ..models import Comment
from .forms import CommentForm

@main.route('/blog/comment/new',methods = ['GET','POST'])
def new_comment(id):
    form = CommentForm()
    
    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data
        new_comment = Comment(title,comment)
        new_comment.save_comment()
        return redirect(url_for('blog'))

    return render_template('new_comment.html',CommentForm=form)
