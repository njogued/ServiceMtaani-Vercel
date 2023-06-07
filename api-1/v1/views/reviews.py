#usr/bin/python3

from api.v1.views import app_views
from models import storage
from models.review import Review
from flask import request, jsonify, abort

@app_views.route("/reviews", methods=["GET", "POST"], strict_slashes=False)
@app_views.route("/reviews/<review_id>", methods=["GET", "PUT", "DELETE"], strict_slashes=False)
def get_all_reviews(review_id=None):
    all_reviews = storage.all(Review).values()

    review_list = [review.to_dict() for review in all_reviews]

    if not review_id:
        if request.method == "GET":
            return jsonify(review_list), 200

        if request.method == "POST":
            review_attr = request.get_json()

            if review_attr is None or type(review_attr) is not dict:
                abort(400, "Invalid input")

            if review_attr.get("client_id") is None or \
                review_attr.get("vendor_id") is None and \
                review_attr.get("mechanic_id") is None or \
                review_attr.get("description") is None or \
                review_attr.get("rating") is None:
                abort(400, "Incomplete Information")

            else:
                review_obj = Review(**review_attr)
                review_obj.save()
                return jsonify(review_obj.to_dict()), 201

    else:
        review_obj = storage.get(Review, review_id)

        if not review_obj:
            abort(404, "Review not Found")

        else:
            if request.method == "GET":
                return jsonify(review_obj.to_dict()), 200

            elif request.method == "PUT":
                review_update_attr = request.get_json()
                for key, value in review_update_attr.items():
                    setattr(review_obj, key, value)
                review_obj.save()
                return jsonify(review_obj.to_dict()), 201

            else:
                storage.delete(review_obj)
                storage.save()
                return jsonify({}), 200
