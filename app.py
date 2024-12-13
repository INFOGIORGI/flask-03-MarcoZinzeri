from flask import Flask,render_template

app = Flask(__name__)

lista=(("parmigiano","SC02",7),("sugo","SC03",2),(""))
@app.route("/")
def homepage():
    return render_template("home.html",titolo="home")

@app.route("/detail")
def detail():
    return render_template("details.html",titolo="details",lista=lista)

app.run(debug=True)
