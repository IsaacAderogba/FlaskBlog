from flask import Flask, escape, request

app = Flask(__name__)  # the server


@app.route('/')
@app.route('/home')
def hello():
    name = request.args.get("name", "Home Page")
    return f'<h1>Hello, {escape(name)}!</h1>'


@app.route('/about')
def about():
    return '<h1>About</h1>'


if __name__ == '__main__':
    app.run(debug=True)
