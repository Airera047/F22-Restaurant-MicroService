from flask import Flask, Response, request
from datetime import datetime
import json
from restaurant_resource import RestaurantResource
from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__)

CORS(app)


@app.get("/api/health")
def get_health():
    t = str(datetime.now())
    msg = {
        "name": "F22-Starter-Microservice",
        "health": "Good",
        "at time": t
    }

    # DFF TODO Explain status codes, content type, ... ...
    result = Response(json.dumps(msg), status=200, content_type="application/json")

    return result


@app.route("/api/restaurants/id/<rid>", methods=["GET"])
def get_restaurant_by_id(rid):

    result = RestaurantResource.get_restaurant_by_key(rid)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/restaurants/query/<query>/<offset>/<limit>", methods=["GET"])
def get_restaurants_by_query(query, offset, limit):

    result = RestaurantResource.get_restaurant_by_query(query, int(offset), int(limit))

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/restaurants/create/<rid>/<name>/<address>/<email>/<phone>/<category>", methods=["POST"])
def create_restaurants_by_rid(rid, name, address, email, phone, category):

    result = RestaurantResource.create_restaurant_by_key(rid, name, address, email, phone, category)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/restaurants/update/<rid>/<name>/<address>/<email>/<phone>/<category>", methods=["POST"])
def update_restaurants_by_rid(rid, name, address, email, phone, category):

    result = RestaurantResource.update_restaurant_by_key(rid, name, address, email, phone, category)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp

@app.route("/api/restaurants/delete/<rid>", methods=["POST"])
def delete_restaurants_by_rid(rid):

    result = RestaurantResource.delete_restaurant_by_key(rid)

    if result:
        rsp = Response(json.dumps(result), status=200, content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)

