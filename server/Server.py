from sqlalchemy import exc
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Statistics.sqlite3'
db = SQLAlchemy(app)


class Statistic(db.Model):
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    mode = db.Column("mode", db.String(100))
    wpm = db.Column("wpm", db.Float)
    cpm = db.Column("cpm", db.Float)
    time = db.Column("time", db.Integer)

    def __init__(self, name, mode, wpm, cpm, time):
        self.name = name
        self.mode = mode
        self.wpm = wpm
        self.cpm = cpm
        self.time = time

    def json_encoder(self):
        return {
            "id": self._id,
            "name": self.name,
            "mode": self.mode,
            "wpm": self.wpm,
            "cpm": self.cpm,
            "time": self.time
        }


@app.route("/statistics", methods=["POST", "GET"])
def statistics():
    if request.method == "GET":
        try:
            stats = [stat.json_encoder() for stat in Statistic.query.all()]
        except Exception as e:
            return jsonify({"STATUS": "Error", "MESSAGE": str(e)})

        return jsonify(stats)
    if request.method == "POST":
        content = request.get_json()
        try:
            db.session.add(Statistic(content["name"], content["mode"], content["wpm"],
                                     content["cpm"], content["time"]))
            db.session.commit()
        except exc.StatementError as e:
            return jsonify({"STATUS": "StatementError", "MESSAGE": str(e)})
        except KeyError as e:
            return jsonify({"STATUS": "KeyError", "MESSAGE": str(e)})
        except Exception as e:
            return jsonify({"STATUS": "Error", "MESSAGE": str(e)})

        return jsonify({"STATUS": "SUCCESS"})


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
