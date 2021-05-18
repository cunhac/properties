# http://pythonclub.com.br/peewee-um-orm-python-minimalista.html
# https://gist.github.com/natorsc/2aa22acad48379c446f8141894da0d8
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
        print('post')
        return redirect(url_for("filter"))
    return render_template('select/state.html', states=STATES)


@app.route('/filter', methods=["GET"])
def filter(state):

    dados = session.query(Lofts).filter(Lofts.state == state)

    dados_filter = session.execute(dados)
    print('filter', dados_filter)
    return render_template('select/filter.html', dados=dados_filter)

    # def product(product_id):
    #     product = Products.query.filter_by(id=product_id).first() or abort(
    #         404, "produto nao encontrado"
    #     )
    #     return render_template("product.html", product=product)

    # if request.method == "POST":
    #     engine = create_engine("sqlite:///lofts_register.db", echo=False)
    #
    #     Session = sessionmaker(bind=engine)
    #     session = Session()
    #
    #     dados= session.query(Lofts).filter(Lofts.state == state)
    #
    #     dados_filter = session.execute(dados)
    #
    #     return render_template(dados=dados_filter)


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


if __name__ != "__main__":
    pass
else:
    app.run()

# @app.route("/api/searchstate/<state>", methods=['POST'])
# def searchstate(state):
#     pass


if "__main__" == __name__:
    app.run(debug=True)

# conn = sqlite3.connect('lofts_register.db')
# cursor = conn.cursor()
# dados = session.query(Lofts).filter(Lofts.state == 1).all()
# return dados

# @app.route('/api/state/<_state>', methods=['POST'])
# def api_state(_state):
#     dados = session.query(Lofts).filter(Lofts.state == _state).all()
#     _data = {'response':[]}
#     if dados:
#         list_dados = []
#         for dado in dados:
#             _data_json = dict(
#                 id=dado.id,
#                 state=dado.state,
#                 city=dado.city,
#             )
#             list_dados.append(_data_json)
#         _data = {'response':list_dados}
#         print(_data)
#
#     return _data
