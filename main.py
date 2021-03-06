from flask import Flask, request, render_template, redirect, url_for
from property import lofts_register
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from create import Lofts
from cfg import STATES, STATUS, SELECT_REGISTER, TOTAL_VALUE, SELECT_ALL, UPDATE_REGISTER, DELETE_REGISTER, ID

engine = create_engine("sqlite:///lofts_register.db", echo=False)

Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__, template_folder='templates', static_url_path='/static')


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        if request.form['button'] == "Register loft":
            return redirect(url_for("register"))
        elif request.form['button'] == "Select loft":
            return redirect(url_for("select_register"))
        elif request.form['button'] == "Select all lofts":
            return redirect(url_for("select_all"))
        elif request.form['button'] == "Update register":
            return redirect(url_for("update_register"))
        elif request.form['button'] == "Delete register":
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
        select_state = request.form.get('select_state')
        dados = session.query(Lofts).filter(Lofts.state == select_state).all()
        return render_template('select/state.html', states=STATES, dados=dados)
    return render_template('select/state.html', states=STATES, dados=None)


@app.route('/total_value', methods=['GET', 'POST'])
def total_value():
    if request.method == "POST":
        select_total = request.form.get("select_total")
        dados = session.query(Lofts).filter(Lofts.total_value == select_total).all()
        return render_template('select/total_value.html', total_value=TOTAL_VALUE, dados=dados)
    return render_template('select/total_value.html', total_value=TOTAL_VALUE, dados=None)


@app.route('/dropdown_status', methods=['GET', 'POST'])
def status():
    if request.method == "POST":
        select_status = request.form.get('select_status')
        dados = session.query(Lofts).filter(Lofts.status == select_status).all()
        return render_template('select/status.html', status=STATUS, dados=dados)
    return render_template('select/status.html', status=STATUS, dados=None)


@app.route('/dropdown_select all', methods=['GET', "POST"])
def select_all():
    if request.method == "POST":
        dados = session.query(Lofts).all()
        return render_template('select/select_all.html', select_all=SELECT_ALL, dados=dados)
    return render_template('select/select_all.html', select_all=SELECT_ALL, dados=None)


@app.route('/dropdown_update', methods=['GET'])
def update_register():
    return render_template('select/update_register.html', update_register=UPDATE_REGISTER)


@app.route('/delete', methods=["GET", "POST"])
def delete_register():
    if request.method == "POST":
        select_id = request.form.get('select_id')
        dados = session.query(Lofts).filter(Lofts.id == select_id).all()
        return render_template('select/delete.html', id=ID, dados=dados)
    return render_template('select/delete.html', id=ID, dados=None)


@app.route('/confirm', methods=["GET", "POST"])
def confirm_delete(delete_register):
    if request.method == "POST":
        select_id = request.form.get('select_id')
        if request.form['button'] == "Yes":
            session.query(Lofts).filter(Lofts.id == select_id).delete()
            return render_template('select/delete.html')
        elif request.form['button'] == "No":
            return render_template('select/delete.html')
    return render_template('select/delete.html')




if "__main__" == __name__:
    app.run(debug=True)
