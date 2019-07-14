from flask import Flask,render_template,url_for,flash,redirect,request,abort,Blueprint
from flask_login import login_user,current_user,login_required
from first_tutorial import db
from first_tutorial.models import Post
from first_tutorial.posts.forms import PostForm

posts= Blueprint('post',__name__)



@posts.route("/post/new" ,methods=['POST','GET'])
@login_required
def new_post():
	form=PostForm()
	if form.validate_on_submit():
		post=Post(title=form.title.data,content=form.content.data ,author=current_user)
		db.session.add(post)
		db.session.commit()	
		flash('Your post has been created','success')
		return redirect(url_for('main.home'))
	return render_template('create_post.html',legend='New Post',title='New Post',form=form)

@posts.route("/post/<int:post_id>")
def post(post_id):
	post = Post.query.get_or_404(post_id)
	return render_template('post.html',title=post.title,post=post)



@posts.route("/post/<int:post_id>/update",methods=['POST','GET'])
@login_required

def update_post(post_id):
	post=Post.query.get_or_404(post_id)
	if post.author != current_user:
		abort(403)
	form= PostForm() 
	if form.validate_on_submit():
		post.title=form.title.data
		post.content=form.content.data
		db.session.commit()
		flash('Your Post has been updated','success')
		return redirect(url_for('posts.post',post_id=post.id))
	elif request.method == 'GET' :
		form.title.data=post.title
		form.content.data=post.content

	return render_template('create_post.html',legend='Update Form' ,title='Update Post',form=form)


@posts.route("/post/<int:post_id>/delete",methods=['POST'])
@login_required

def delete_post(post_id):
	post=Post.query.get_or_404(post_id)
	if post.author != current_user:
		abort(403)
	db.session.delete(post)
	db.session.commit()
	flash('Your Post has been deleted','success')
	return redirect(url_for('main.home'))
