import flask
from flask import render_template
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm
from wtforms import SubmitField, IntegerField

app = flask.Flask(__name__)
bootstrap = Bootstrap5(app)
app.config['SECRET_KEY'] = 'a very secret key!'

class InputForm(FlaskForm):
    parameter = IntegerField('Iteration', default=3)
    submit = SubmitField('RUN!')


def pipeline(inp):
    output = []
    for i in range(inp):
        output.append(('data1','data2','data3'))
    return output

@app.route('/', methods=['GET','POST'])
def index():
    form = InputForm()
    if form.validate_on_submit():
        print(pipeline(form.parameter.data))
    return render_template('index.jinja2', form=form)
