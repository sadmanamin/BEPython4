from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/<name>')
@app.route('/')
def index(name=None):
    return render_template('index.html',my_name=name)

@app.route('/home/<int:value>/<value2>')
def home(value, value2):
    return f"Hello {value} , {value2}"
    # return redirect(url_for('index'))

@app.route('/new_value', methods=['POST'])
def new_value():
    data = request.data
    print(data)
    data['body'] = "asdasdasdasdasdas"
    return data
    # request.


if __name__ == "__main__":
    app.run()