
from flask import Flask , render_template , request , redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Dashboard.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Monitor (db.Model):
    sr = db.Column (db.Integer, primary_key = True)
    Temperature = db.Column(db.Integer() , nullable = False)
    Heart_Beat = db.Column(db.Integer(), nullable = False)
    date = db.Column(db.DateTime , default = datetime.utcnow)


def __repr__(self) ->str :
    return f"{self.sr}-{self.Temperature}"



@app.route("/" , methods = ['GET' ,'POST'])
def home():
    if request.method == 'POST':
        
        Temperature = request.form['Temperature']
        Heart_Beat = request.form['Heart_Beat']

        x = Monitor( Temperature = Temperature , Heart_Beat = Heart_Beat )
        db.session.add(x)
        db.session.commit()

    data = Monitor.query.all()
    return render_template('database.html' , data = data )
    



@app.route("/delete/<int:sr>")
def delete(sr):
    y = Monitor.query.filter_by(sr=sr).first()
    db.session.delete(y)
    db.session.commit()
    return redirect("/")


if __name__ =="__main__":
    app.run(debug=True,port=8000)