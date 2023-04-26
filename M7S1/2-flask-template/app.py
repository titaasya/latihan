from flask import Flask, render_template, request, jsonify
from flask_ngrok import run_with_ngrok

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def iris_prediction():
    if request.method == 'GET':
        return render_template("iris-prediction.html")
    else:
        print(request)
        return jsonify(request.args)


if __name__ == '__main__':
    run_with_ngrok(app)
    app.run()