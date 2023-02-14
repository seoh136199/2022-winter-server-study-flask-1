from flask import Flask, request
from database import Database

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get():
    id = request.args.get("id")
    pw = request.args.get("pw")

    db = Database()
    sql = "SELECT * FROM user where id = %s"
    result = db.execute_one(sql, (id))

    db.commit()
    db.close()

    if (result == None):
        return "False", 200
    elif (result['password'] != pw):
        print(len(result['password']))
        print(len(pw))
        return "False", 200
    else:
        return "True", 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)