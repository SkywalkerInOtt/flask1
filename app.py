from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    username = request.args.get('name')
    return render_template('index.html', name = username);

if __name__ == '__main__':
    app.run(host = "0.0.0.0", port=5001, debug=True)
