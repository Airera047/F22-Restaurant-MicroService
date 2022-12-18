from flask import Flask, Response, request
from datetime import datetime
import json
from restaurant_resource import RestaurantResource
from review_resource import ReviewResource
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
    result = Response(json.dumps(msg), status=200,
                      content_type="application/json")

    return result


@app.route("/api/restaurants/id/<rid>", methods=["GET"])
def get_restaurant_by_id(rid):

    result = RestaurantResource.get_restaurant_by_key(rid)

    if result:
        rsp = Response(json.dumps(result), status=200,
                       content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/restaurants/top5/<cuisine>", methods=["GET"])
def get_restaurant_top5(cuisine):

    result = RestaurantResource.get_restaurant_top5(cuisine)

    if result:
        rsp = Response(json.dumps(result), status=200,
                       content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/restaurants/all", methods=["GET"])
def get_all_restaurants():

    result = RestaurantResource.get_all_restaurants()

    if result:
        rsp = Response(json.dumps(result), status=200,
                       content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/restaurants/query/<query>/<offset>/<limit>", methods=["GET"])
def get_restaurants_by_query(query, offset, limit):

    result = RestaurantResource.get_restaurant_by_query(
        query, int(offset), int(limit))

    if result:
        rsp = Response(json.dumps(result), status=200,
                       content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/restaurants/create/<rid>/<cuisine>/<name>/<rating>/<address>/<zip_code>/<phone>/<url>", methods=["POST"])
def create_restaurants_by_rid(rid, cuisine, name, rating, address, zip_code, phone, url):

    result = RestaurantResource.create_restaurant_by_key(
        rid, cuisine, name, rating, address, zip_code, phone, url)

    if result:
        rsp = Response(json.dumps(result), status=200,
                       content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/restaurants/update/<rid>/<cuisine>/<name>/<rating>/<address>/<phone>", methods=["POST"])
def update_restaurants_by_rid(rid, cuisine, name, rating, address, phone):

    result = RestaurantResource.update_restaurant_by_key(
        rid, cuisine, name, rating, address, zip_code, phone, url)

    if result:
        rsp = Response(json.dumps(result), status=200,
                       content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/restaurants/delete/<rid>", methods=["POST"])
def delete_restaurants_by_rid(rid):

    result = RestaurantResource.delete_restaurant_by_key(rid)

    if result:
        rsp = Response(json.dumps(result), status=200,
                       content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/reviews/id/<rid>", methods=["GET"])
def get_review_by_id(rid):

    result = ReviewResource.get_review_by_key(rid)

    if result:
        rsp = Response(json.dumps(result), status=200,
                       content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/reviews/uid/<uid>", methods=["GET"])
def get_review_by_user_id(rid):

    result = ReviewResource.get_review_by_user_id(rid)

    if result:
        rsp = Response(json.dumps(result), status=200,
                       content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/reviews/rid/<rid>", methods=["GET"])
def get_review_by_restaurant_id(rid):

    result = ReviewResource.get_review_by_user_id(rid)

    if result:
        rsp = Response(json.dumps(result), status=200,
                       content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/reviews/create/<rid>/<rating>/<content>", methods=["POST"])
def create_reviews_by_rid(rid, rating, content):

    result = ReviewResource.create_review_by_key(rid, rating, content)

    if result:
        rsp = Response(json.dumps(result), status=200,
                       content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/reviews/update/<rid>/<rating>/<content>", methods=["POST"])
def update_reviews_by_rid(rid, rating, content):

    result = ReviewResource.update_review_by_key(rid, rating, content)

    if result:
        rsp = Response(json.dumps(result), status=200,
                       content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/reviews/delete/<rid>", methods=["POST"])
def delete_reviews_by_rid(rid):

    result = ReviewResource.delete_review_by_key(rid)

    if result:
        rsp = Response(json.dumps(result), status=200,
                       content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/write_reviews/create/<rrid>/<uid>/<rid>", methods=["POST"])
def create_write_reviews_by_rid(rrid, uid, rid):

    result = ReviewResource.create_write_review_by_key(rrid, uid, rid)

    if result:
        rsp = Response(json.dumps(result), status=200,
                       content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


@app.route("/api/write_reviews/delete/<rid>", methods=["POST"])
def delete_write_reviews_by_rid(rid):

    result = ReviewResource.delete_write_review_by_key(rid)

    if result:
        rsp = Response(json.dumps(result), status=200,
                       content_type="application.json")
    else:
        rsp = Response("NOT FOUND", status=404, content_type="text/plain")

    return rsp


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)
