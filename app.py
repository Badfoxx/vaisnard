from flask import Flask, render_template





#Create instance of Flask App
app = Flask(__name__)

#Define Route and Contant of that page
@app.route("/")
def home():
    return render_template("home.html")

#Define 2nd Route and Content

@app.route("/blog")
def about():
    return render_template("blog.html")

@app.route("/grom")
def volt():
    return render_template("grom.html")







#Running and Controlling the script
if (__name__ =="__main__"):
    app.run(debug=True)