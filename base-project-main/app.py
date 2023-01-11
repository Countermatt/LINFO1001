import os
from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy


# Init the Flask app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
db = SQLAlchemy(app)


# Define sqlalchemy models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100))


class Segment(db.Model):
    instance_id = db.Column(db.Integer, primary_key=False)
    segment_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(100), primary_key=True)
    interval = db.Column(db.String(100), primary_key=False)
    uptime = db.Column(db.Integer, primary_key=False)
    heavy = db.Column(db.Integer, primary_key=False)
    car = db.Column(db.Integer, primary_key=False)
    bike = db.Column(db.Integer, primary_key=False)
    pedestrian = db.Column(db.Integer, primary_key=False)
    heavy_lft = db.Column(db.Integer, primary_key=False)
    heavy_rgt = db.Column(db.Integer, primary_key=False)
    car_lft = db.Column(db.Integer, primary_key=False)
    car_rgt = db.Column(db.Integer, primary_key=False)
    bike_lft = db.Column(db.Integer, primary_key=False)
    bike_rgt = db.Column(db.Integer, primary_key=False)
    pedestrian_lft = db.Column(db.Integer, primary_key=False)
    pedestrian_rgt = db.Column(db.Integer, primary_key=False)
    direction = db.Column(db.Integer, primary_key=False)
    car_speed_hist_0to70plus = db.Column(db.String(100), primary_key=False)
    car_speed_hist_0to120plus = db.Column(db.String(100), primary_key=False)
    timezone = db.Column(db.String(100), primary_key=False)
    v85 = db.Column(db.String(100), primary_key=False)

    def __str__(self):
        return 'pedestrian : {}'.format(self.pedestrian) + 'car' + str(self.car)

# Init database if tables do not exist
with app.app_context():
    db.create_all()


# Define the routes code
@app.route("/")
def user_list():
    users = db.session.execute(db.select(User).order_by(User.username)).scalars()
    return render_template("base.html", users=users)

@app.route("/segment")
def segment_list():
    segment = db.session.execute(db.select(Segment).order_by(Segment.date)).scalars()
    return render_template("segment.html", segment=segment)

@app.route("/create", methods=["POST"])
def user_create():
    user = User(username=request.form["username"], email=request.form["email"])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for("user_list"))

@app.route("/delete/<int:id>")
def user_delete(id):
    user = db.get_or_404(User, id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("user_list"))

@app.route('/segment/<int:segment_id>/<string:date>')
def show_id(segment_id, date):
    segment = db.get_or_404(Segment, (segment_id, date))
    return 'Segment %s' % segment

# Standalone dev execution
if __name__ == '__main__':

    app.run(host="0.0.0.0")
