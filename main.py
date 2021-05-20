from flask import Flask, request, render_template, redirect, url_for
from property import lofts_register
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create import Lofts
from cfg import STATES, STATUS, SELECT_REGISTER, TOTAL_VALUE, SELECT_ALL, UPDATE_REGISTER

engine = create_engine("sqlite:///lofts_register.db", echo=False)

Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__, template_folder='templates', static_url_path='/static')


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        if request.form['button'] == "Register loft":
            return redirect(url_for("register"))
        if request.form['button'] == "Select loft":
            return redirect(url_for("select_register"))
        if request.form['button'] == "Select all lofts":
            return redirect(url_for("select_all"))
        if request.form['button'] == "Update register":
            return redirect(url_for("update_register"))
        if request.form['button'] == "Delete register":
            return redirect(url_for("delete_register"))
    return render_template('home.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        loft = lofts_register(request.form)
        session.add(loft)
        session.commit()
        return redirect(url_for("sucess"))
    return render_template('register.html')


@app.route("/sucess_link", methods=['GET', 'POST'])
def sucess():
    if request.method == "POST":
        return redirect(url_for("home"))
    return render_template('s.html')


@app.route("/select_register", methods=['GET', 'POST'])
def select_register():
    if request.method == "POST":
        if request.form['button'] == "state":
            return redirect(url_for("state"))
        elif request.form['button'] == 'total_value':
            return redirect(url_for("total_value"))
        elif request.form['button'] == 'status':
            return redirect(url_for("status"))
    return render_template('select/select_register.html')


@app.route('/state', methods=['GET', 'POST'])
def state():
    if request.method == "POST":
        dados = session.query(Lofts).filter(Lofts.state == "a").all()
        return render_template('select/state.html', states=STATES, dados=dados)
    return render_template('select/state.html', states=STATES, dados=None)


@app.route('/total value', methods=['GET'])
def total_value():
    return render_template('select/total_value.html', total_value=TOTAL_VALUE)


@app.route('/dropdown_status', methods=['GET'])
def status():
    return render_template('select/status.html', status=STATUS)


@app.route('/dropdown_select all', methods=['GET'])
def select_all():
    return render_template('select/select_all.html', select_all=SELECT_ALL)


@app.route('/dropdown_update', methods=['GET'])
def update_register():
    return render_template('select/update_register.html', update_register=UPDATE_REGISTER)


@app.route('/delete', methods=['GET'])
def delete_register():
    return render_template('select/delete.html')


if "__main__" == __name__:
    app.run(debug=True)
