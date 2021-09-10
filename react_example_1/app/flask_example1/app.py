from logging import debug
from types import MethodType
from flask import Flask, render_template, request, redirect, url_for, jsonify, json
from forms import Todo
from flask_sqlalchemy import SQLAlchemy
from os import environ, path
import datetime
from flask_cors import CORS

app = Flask(__name__)
# CORS(app)
app.config['SECRET_KEY']= 'password'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'
db = SQLAlchemy(app)

class TodoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(240))

    def __str__(self):
        return f'{self.content}, {self.id}'

def todo_serializer(todo):
    return{
        'id': todo.id,
        'content': todo.content
    }


@app.route('/api', methods=['GET'])
def hello_world():
    # request_method = request.method
    # todo = TodoModel.query.all()
    # if request.method == 'POST':
    #     first_name = request.form['first_name']
    #     return redirect(url_for('name',first_name=first_name))
    # return render_template('hello.html', request_method=request_method, todo=todo)
    return jsonify([*map(todo_serializer, TodoModel.query.all())])

@app.route('/api/create', methods=['GET', 'POST'])
def create():
    todo_form = Todo()
    todo = TodoModel(content=todo_form.content.data)
    # request_data = json.loads(request.data)
    # todo = TodoModel(content = request_data['content'])
    db.session.add(todo)
    db.session.commit()

    return {'201':"todo new one created "}

@app.route('/api/<int:id>')
def show(id):
    return jsonify([*map(todo_serializer, TodoModel.query.filter_by(id=id))])

@app.route('/api/<int:id>', methods=['POST'])
def delete(id):
    request_data = json.loads(request.data)
    TodoModel.query.filter_by(id=request_data['id']).delete()
    db.session.commit()

    return {'204' : 'Deleted successfully'}

@app.route('/name/<string:first_name>')
def name(first_name):
    return f'{first_name}'

@app.route('/', methods=['GET', 'POST'])
def todo():
    db_components = TodoModel.query.all();
    todo_form = Todo()
    if todo_form.validate_on_submit():
        todo = TodoModel(content=todo_form.content.data)
        db.session.add(todo)
        db.session.commit()
        return redirect('/')
    return render_template('todo.html', form=todo_form, datalist=db_components)

@app.route('/delete/<int:id>', methods = ['GET',"DELETE"])
def delete_todo(id):
    task = TodoModel.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
        return redirect('/')
    except:
        return f'There was an error while deleting that task'

@app.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    task = TodoModel.query.get_or_404(id)
    # todo_form = Todo(instance=task)
    if request.method == "POST":
        task = request.form['content']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return f'there was an issue while updating'
    else:
        return render_template('update.html', form=task,)


if __name__ == '__main__':
    app.run(debug=True)