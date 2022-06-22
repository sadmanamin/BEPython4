import json
from project import app, cache, celery
from flask import render_template, request, redirect, url_for
from project.model import Todo

@app.route('/')
def home():
    # todo_list = Todo.query.all()
    # return render_template('todo.html',todo_list=todo_list)
    # my_dictionary = {}
    result = cache.get('todo_list')
    if result:
        return result
    else:
        todo_list = Todo.query.all()
        # print(isinstance(todo_list[0], Todo))
        cache.set('todo_list',str(todo_list))
        # for todo in todo_list:
        return 'success'

    

# @app.route("/add", methods=["POST"])
# def add():
#     title = request.form["title"]
#     new_todo = Todo(title=title)
#     db.session.add(new_todo)
#     db.session.commit()
#     return redirect(url_for("home"))

# @app.route("/update/<int:todo_id>")
# def update(todo_id):
#     todo = Todo.query.filter_by(id=todo_id).first()
#     todo.complete = not todo.complete
#     db.session.commit()
#     return redirect(url_for("home"))

# @app.route("/delete/<int:todo_id>")
# def delete(todo_id):
#     todo = Todo.query.filter_by(id=todo_id).first()
#     db.session.delete(todo)
#     db.session.commit()
#     return redirect(url_for("home"))

@app.route('/set_cache/<country>/<capital>')
def set_cache(country, capital):
    # d = {
    #     country : capital
    # }

    cache.set(country,capital)

    return 'success'

@app.route('/get_cache/<country>')
def get_cache(country):
    # d = {
    #     country : capital
    # }

    capital = cache.get(country)

    return capital

# @app.route('/populate')
# def populate():
#     for i in range(0,10000):
#         title = f'test todo - {i}'
#         todo = Todo(title)
#         db.session.add(todo)
#     db.session.commit()
#     return 'success'

@celery.task
def find_fibonacci_async(number):
    print("Starting calculation of "+str(number))
    def fib(n):
        if n == 1:
            return 0
        if n == 2:
            return 1
        
        return fib(n-1)+fib(n-2)
    result = fib(number)
    print("Result of "+str(number))
    return result

