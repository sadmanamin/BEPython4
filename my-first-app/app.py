from flask import Flask, redirect, url_for, render_template, request
import psycopg2

app = Flask(__name__)

data = {}
count = 0

conn = psycopg2.connect(
    host=os.getenviron('HOST'),
    database="beflask",
    user="postgres",
    password="123456")

cur = conn.cursor()

@app.route('/get-db')
def get_db():
    cur.execute('SELECT version()')

    # display the PostgreSQL database server version
    db_version = cur.fetchone()
    print(db_version)
    
# close the communication with the PostgreSQL
    cur.close()
    return 'True'

class Todo:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.complete = False

# @app.route('/<name>')
# @app.route('/')
# def index(name=None):
#     return render_template('index.html',my_name=name)

# @app.route('/home/<int:value>/<value2>')
# def home(value, value2):
#     return f"Hello {value} , {value2}"
#     # return redirect(url_for('index'))

# @app.route('/new_value', methods=['POST'])
# def new_value():
#     data = request.get_json()
#     print(data)
#     data['body'] = "asdasdasdasdasdas"
#     return data

@app.route('/new-todo', methods=['POST'])
def new_todo():
    title = request.form['title']
    global count
    count = count + 1
    todo = Todo(count, title)
    data[todo.id] = todo
    return redirect(url_for('show_todo'))

@app.route('/show-todo')
def show_todo():
    return render_template('todo.html',todo_list=data)

@app.route('/update/<int:id>')
def update(id):
    todo = data[id]
    todo.complete = True
    return redirect(url_for('show_todo'))



if __name__ == "__main__":
    data = {}
    count = 0
    app.run()















# conn = psycopg2.connect(
#     host="localhost",
#     database="dbv4",
#     user="postgres",
#     password="123456")

# cur = conn.cursor()

# @app.route('/get-db')
# def get_db():
#     cur.execute('SELECT version()')

#     # display the PostgreSQL database server version
#     db_version = cur.fetchone()
#     print(db_version)
    
# # close the communication with the PostgreSQL
#     cur.close()
#     return 'True'