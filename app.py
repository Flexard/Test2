from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/all-players")
def all_players():
    search = request.args.get("search", "")
    sort = request.args.get("sort", "name")

    db = sqlite3.connect("football.db")
    db.row_factory = sqlite3.Row

    if search:
        if sort == "age":
            players = db.execute(
                "SELECT * FROM players WHERE name LIKE ? ORDER BY age",
                ("%" + search + "%",)
            ).fetchall()

        elif sort == "value":
            players = db.execute(
                "SELECT * FROM players WHERE name LIKE ? ORDER BY market_value DESC",
                ("%" + search + "%",)
            ).fetchall()

        else:
            players = db.execute(
                "SELECT * FROM players WHERE name LIKE ? ORDER BY name",
                ("%" + search + "%",)
            ).fetchall()

    else:
        if sort == "age":
            players = db.execute(
                "SELECT * FROM players ORDER BY age"
            ).fetchall()

        elif sort == "value":
            players = db.execute(
                "SELECT * FROM players ORDER BY market_value DESC"
            ).fetchall()

        else:
            players = db.execute(
                "SELECT * FROM players ORDER BY name"
            ).fetchall()

    db.close()

    return render_template(
        "category.html",
        players=players,
        category="All Players",
        search=search,
        sort=sort
    )


@app.route("/goalkeepers")
def goalkeepers():
    return category_page("Goalkeeper", "Goalkeepers")


@app.route("/defenders")
def defenders():
    return category_page("Defender", "Defenders")


@app.route("/midfielders")
def midfielders():
    return category_page("Midfielder", "Midfielders")


@app.route("/forwards")
def forwards():
    return category_page("Forward", "Forwards")


def category_page(position, category):
    db = sqlite3.connect("football.db")
    db.row_factory = sqlite3.Row

    players = db.execute(
        "SELECT * FROM players WHERE position = ?",
        (position,)
    ).fetchall()

    db.close()

    return render_template(
        "category.html",
        players=players,
        category=category
    )


@app.route("/table")
def table():
    db = sqlite3.connect("football.db")
    db.row_factory = sqlite3.Row

    players = db.execute(
        "SELECT * FROM players"
    ).fetchall()

    db.close()

    return render_template("table.html", players=players)


@app.route("/player/<name>")
def player(name):
    db = sqlite3.connect("football.db")
    db.row_factory = sqlite3.Row

    player = db.execute(
        "SELECT * FROM players WHERE name = ?",
        (name,)
    ).fetchone()

    db.close()

    return render_template("player.html", player=player)


app.run(debug=True)