from flask import Flask, request, jsonify
from Recommender import Recommender
import os

app = Flask(__name__)

# Call Recommender init here. Training yaha hogayi server chalte hi.
# Routes me use Recommender ka getRecommendation function, ye instantly return karega

# JS calls Flask, Flask me routes h jisme we send recommendations, update/insert/edit dataset ( jaha pe bhi wo hosted h )
REC = Recommender()


@app.route('/productRecommendation', methods=['GET'])
def getRecommendations():
    if request.method == 'GET':
        userId = request.args.get('userId')
        if userId != None:
            recommendations = REC.getProductRecommendation(int(userId))
        print(recommendations)
        return jsonify(recommendations)


@app.route('/getProductList', methods=['GET'])
def getProductList():
    if request.method == 'GET':
        return jsonify(REC.productList)


@app.route('/getUserOrderHistory', methods=['GET'])
def getUserOrderHistory():
    if request.method == 'GET':
        userId = request.args.get('userId')
        orderHist = REC.getUserOrderHistory(int(userId))
        return jsonify(orderHist)


@app.route('/getUserBrowseHistory', methods=['GET'])
def getUserBrowseHistory():
    if request.method == 'GET':
        userId = request.args.get('userId')
        browseHist = REC.getUserBrowseHistory(int(userId))
        return jsonify(browseHist)


@app.route('/')
def index():
    return "<h1>Welcome to the Flask server</h1>"


PORT = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
    app.run(port=PORT, debug=True, use_reloader=False)
