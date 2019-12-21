from app import app
from flask import request, render_template
from app.forms import *
from app.models import *


@app.route('/', methods=['GET','POST'])
def index():
    form = Example.query.all()
    return render_template('index.html', form=form)


@app.route('/create_form', methods=['GET','POST'])
def create_form():

    form = ExampleForm(request.form)

    if request.method == 'POST' and form.validate():
        print(form)
        example = Example()
        example.int_row = form.int_row.data
        example.str_row = form.str_row.data
        db.session.add(example)
        db.session.commit() # сохранение изменений

    return render_template('forms.html', form=form)


@app.route('/change_form/<id_form>', methods=['GET','POST'])
def change_form(id_form):

    table = Example.query.get(id_form)
    form = ExampleForm(obj=table)

    if request.method == 'POST' and form.validate():
        print(form)
        example = Example()
        example.int_row = form.int_row.data
        example.str_row = form.str_row.data
        db.session.add(example)
        db.session.commit() # сохранение изменений

    return render_template('forms.html', form=form)
