from flask import Flask,render_template
from mocks import Post
app=Flask(__name__)

posts=Post.all()
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")
    

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/blog')
def posts_index():
    posts=Post.all()
    return render_template("posts/index.html",posts=posts)

@app.route('/blog/post/<int:id>')
def show_posts(id): 
    print(id)
    post= Post.find(id)
    post=posts[id-1]
    return render_template("posts/ssssshow.html",post =post)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("errors/404.html"),404


if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0' , port=5000)
    