from flask import Flask, render_template, request

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/output', methods=["POST", "GET"])
def output():
    number = request.args.get('numb')

    return render_template('output.html', result=number)

if __name__ == '__main__':
    app.run()