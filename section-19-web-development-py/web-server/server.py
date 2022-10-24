from flask import Flask, render_template, url_for

app = Flask(__name__)
print(__name__)

@app.route("/")
def hello_world():
    print(url_for('static', filename='global.ico'))
    return render_template('./index.html')

@app.route("/about.html")
def about():
    return render_template('./about.html')
  
# @app.route("/favicon.ico")
# def blog():
#     return "<p>Blog</p>"

@app.route("/blog/2020/dogs")
def blog2():
    return "<p>This is my dog, dog</p>"

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return render_template('./index.html')
  
# @app.route("/blog")
# def blog():
#     return "<p>Blog</p>"

# @app.route("/blog")
# def blog2():
#     return "<p>This is my dog, dog</p>"