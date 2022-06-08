from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route("/publications",methods=["GET"])
def getPublications():
    return jsonify({
        "publications":["carros"]
    })

@app.route("/publication<int:publication_id>",methods=["GET"])
def getPublication():
    return jsonify({
        "publication":{"name":"test"}
    })

@app.route("/publication", methods=["POST"])
def addPublication():
    name = request.json['name']
    return jsonify({
        "message":"Publication added"
    })

@app.route("/publication",methods=["PUT"])
def editPublication():
    return jsonify({
        "message":"Publication was updated"
    })

@app.route("/publication<int:publication_id>", methods=["DELETE"])
def deletePublication():
    return jsonify({
        "message":"The publication was deleted"
    })

if __name__ == '__main__':
    app.run(debug=True,port=3000)