from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/id', methods=['GET'])
def get():
    id = int(request.args.get('id'))
    if id >= 5000:
        return { "result": True }
    else:
        return { "result": False }

@app.route('/id', methods=['POST'])
def post():
    params = request.get_json()
    return { "name": params["name"] }

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)