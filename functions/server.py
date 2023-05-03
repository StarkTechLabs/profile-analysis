from flask import Flask, jsonify, request
from flask_cors import CORS
from loader import handler as load_handler
from qa import handler as qa_handler

app = Flask(__name__)
CORS(app)


@app.route('/')
def main():
    return jsonify({
        'message': 'Welcome'
    })


@app.route('/loader', methods=['POST'])
def loader():
    res = load_handler(request)
    return jsonify({
        'message': 'Success'
    })


@app.route('/qa', methods=['POST'])
def qa():
    res = qa_handler(request)
    return jsonify(res)


#
# Error Handling
#

@app.errorhandler(Exception)
def handle_error(error):
    """ Default error handler """
    print(error)
    error = error or {}
    if type(error) is object:
        response = jsonify(error)
    else:
        response = str(error)

    return jsonify({'error': response, 'message': 'An error occurred.'}), 500


def run(port=8090, debug=False):
    """ """
    print('Running server on port ' + str(port))
    app.run(port=port, debug=debug)


if __name__ == "__main__":
    run()
