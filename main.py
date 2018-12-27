from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:MyNewPass@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    blog_name = db.Column(db.String(120))
    added = db.Column(db.Boolean)

    def __init__(self, name):
        self.name = name
        self.added = False

@app.route('/', methods=['POST', 'GET'])
def index():

#    if request.method == 'POST':
#        blog_name = request.form['blog']
#        new_blog = Blog(blog_name)
#        db.session.add(new_blog)
#        db.session.commit()

#    blogs = Blog.query.filter_by(added=False).all()
#    added_blogs = Blog.query.filter_by(added=True).all()

#    return render_template('main_blog.html',title="Build A Blog", 
#        blogs=blogs, added_blogs=added_blogs)
    

@app.route('/add_blog', methods=['POST'])
def add_blog():



    return redirect('/') 

if __name__ == '__main__':
    app.run()