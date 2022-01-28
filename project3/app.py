from flask import Flask, render_template, request
import model

app = Flask(__name__)



@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/output', methods=["POST", "GET"])
def output():
    hum = request.args.get('hum')
    sun = request.args.get('sun')
    press = request.args.get('press')
    rain = request.args.get('rain')

    prediction = model.classify(hum, sun, press, rain)

    no_yes = {0.0: 'No.', 1.0: 'Yes.'}

    result = no_yes[prediction]

    return render_template('output.html', result=result)

if __name__ == '__main__':
    app.run()