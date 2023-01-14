from flask import Flask, jsonify, request, render_template, send_from_directory
from flask_cors import CORS
from model.city_model import match_exact

app = Flask(__name__, )
CORS(app)

FLUTTER_WEB_APP = 'templates'


@app.route('/web/')
def render_page_web():
    return render_template('index.html')


@app.route('/web/<path:name>')
def return_flutter_doc(name):

    datalist = str(name).split('/')
    DIR_NAME = FLUTTER_WEB_APP

    if len(datalist) > 1:
        for i in range(0, len(datalist) - 1):
            DIR_NAME += '/' + datalist[i]

    return send_from_directory(DIR_NAME, datalist[-1])


@app.route('/')
def render_page():
    return render_template('index.html')


@app.route("/search")
def search_city():
    args = request.args.get('cityName')
    if not args:
        return jsonify({"data": "no input data from user"})
    response = match_exact(args)
    return jsonify(response)


if __name__ == "__main__":
    app.run()
