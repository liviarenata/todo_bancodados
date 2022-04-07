from flask import Flask, render_template, request, redirect

from flask_sqlalchemy import SQLAlchemy

app = Flask('app')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

class Todos(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100))
  complete = db.Column(db.Boolean)
  category = db.Column(db.String(50))

@app.route('/')
def index():
  todos = Todos.query.all()
  return render_template(
    'index.html',
    todos=todos
  )

@app.route('/create', methods=['POST'])
def create():
  title = request.form.get('title')
  cat = request.form.get('category')

  new_todo = Todos(
    title=title,
    category=cat,
    complete=False
  )

  db.session.add(new_todo)
  db.session.commit()
  
  return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
  todos.pop(index)
  return redirect('/')

@app.route('/complete/<int:index>')
def complete(index):
  todos[index]['complete'] = True
  return redirect('/')

@app.route('/update/<int:index>', methods=['POST'])
def update(index):
  title = request.form.get('title')
  todos[index]['title'] = title
  return redirect('/')

# IMPORTANTE V
if __name__ == '__main__':
  db.create_all()
  app.run(host='0.0.0.0', port=8080)