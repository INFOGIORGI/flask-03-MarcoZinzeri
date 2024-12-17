from flask import Flask,render_template

app = Flask(__name__)

lista=(("parmigiano","SC02",7),("sugo","SC03",2),("mozzarella","SC03",3))
@app.route("/")
def homepage():
    return render_template("home.html",titolo="home")

@app.route("/detail")
def detail():
    return render_template("details.html",titolo="details",lista=lista)

@app.route("/dettaglios/<nscaffale>")
def scaffale(nscaffale):
    listavuota=[]
    for i in lista:
        if i[1]==nscaffale:
            listavuota.append(i)
  
    return render_template("dettaglioscaffale.html",titolo="scaffale",listavuota=listavuota, nscaffale=nscaffale)


app.run(debug=True)
