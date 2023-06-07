#!/usr/bin/python3
"""Create API routes for the vendors
Routes: /vendors/<vendor_id>
      : /vendors/<vendor_id>/reviews/<review_id>
"""

from api.v1.views import app_views
from flask import jsonify, request, abort
from models.vendor import Vendor
from models.review import Review
from models.part import Part
from models import storage


@app_views.route('/vendors', \
                 methods=["GET", "POST"], strict_slashes=False)
@app_views.route('/vendors/<vendor_id>', \
                 methods=["GET", "PUT", "DELETE"], strict_slashes=False)
def get_vendors(vendor_id=None):
    all_vendors = storage.all(Vendor)
    if not vendor_id:
        if request.method == "GET":
            vendors_list = [vendor.to_dict() for vendor in all_vendors.values()]
            return jsonify(vendors_list), 200
        if request.method == "POST":
            vendor_attrs = request.get_json()
            if not vendor_attrs or type(vendor_attrs) is not dict:
                abort(400, "Invalid input")
            if vendor_attrs.get("first_name") is None or \
                vendor_attrs.get("last_name") is None or \
                    vendor_attrs.get("email") is None or \
                        vendor_attrs.get("password") is None:
                abort(400, "Incomplete information")
            vendor_obj = Vendor(**vendor_attrs)
            vendor_obj.save()
            return jsonify(vendor_obj.to_dict()), 201
    
    if vendor_id:
        vendor_obj = storage.get(Vendor, vendor_id)
        if not vendor_obj:
            abort(404, "Vendor not found")
        if request.method == "GET":
            return jsonify(vendor_obj.to_dict()), 200
        if request.method == "PUT":
            vendor_attributes = request.get_json()
            if not vendor_attributes or type(vendor_attributes) is not dict:
                abort(400, "Invalid input")
            for k, v in vendor_attributes.items():
                setattr(vendor_obj, k, v)
            vendor_obj.save()
            return jsonify(vendor_obj.to_dict()), 201
        if request.method == "DELETE":
            vendor_obj.delete()
            storage.save()
            return jsonify({}), 200
        
@app_views.route("/vendors/<vendor_id>/reviews", \
                 methods=["GET", "POST"], strict_slashes=False)
@app_views.route("/vendors/<vendor_id>/reviews/<review_id>", \
                 methods=["GET", "PUT", "DELETE"], strict_slashes=False)
def vendor_reviews(vendor_id=None, review_id=None):
    if not vendor_id:
        abort(400)
    vendor_obj = storage.get(Vendor, vendor_id)
    if not vendor_obj:
        abort(404)
    if not review_id:
        if request.method == "GET":
            #all_reviews = storage.all(Review).values()
            vendor_reviews = [one_review.to_dict() for one_review in \
                            vendor_obj.reviews]
            return jsonify(vendor_reviews), 200
        if request.method == "POST":
            review_dict = request.get_json()
            if not review_dict or type(review_dict) is not dict:
                abort(400, "Invalid input")
            if review_dict.get("client_id") is None \
                or review_dict.get("description") is None \
                    or review_dict.get("rating") is None:
                abort(400, "Incomplete information")
            review_dict["vendor_id"] = vendor_id
            review_obj = Review(**review_dict)
            review_obj.save()
            return jsonify(review_obj.to_dict()), 201
        
    if review_id:
        review_obj = storage.get(Review, review_id)
        if not review_obj:
            abort(404)
        if request.method == "GET":
            return jsonify(review_obj.to_dict()), 200
        if request.method == "PUT":
            review_attr = request.get_json()
            if not review_attr or type(review_attr) is not dict:
                abort(400, "Invalid input")
            for key, value in review_attr.items():
                if key not in ["id", "created_at", "updated_at"]:
                    setattr(review_obj, key, value)
            review_obj.save()
            return jsonify(review_obj.to_dict()), 201
        if request.method == "DELETE":
            review_obj.delete()
            storage.save()
            return jsonify({}), 200
        
@app_views.route("/vendors/<vendor_id>/parts", \
                 methods=["GET", "POST"], strict_slashes=False)
@app_views.route("/vendors/<vendor_id>/parts/<part_id>", \
                 methods=["GET", "PUT", "DELETE"], strict_slashes=False)
def vendor_parts(vendor_id=None, part_id=None):
    if not vendor_id:
        abort(400)
    vendor_obj = storage.get(Vendor, vendor_id)
    if not vendor_obj:
        abort(404)
    if not part_id:
        if request.method == "GET":
            #all_reviews = storage.all(Review).values()
            vendor_parts = [one_part.to_dict() for one_part in \
                            vendor_obj.parts]
            return jsonify(vendor_parts), 200
        if request.method == "POST":
            part_dict = request.get_json()
            if not part_dict or type(part_dict) is not dict:
                abort(400, "Invalid input")
            if part_dict.get("part_name") is None \
                or part_dict.get("part_price") is None:
                abort(400, "Incomplete information")
            part_dict["vendor_id"] = vendor_id
            part_obj = Part(**part_dict)
            part_obj.save()
            return jsonify(part_obj.to_dict()), 201
        
    if part_id:
        part_obj = storage.get(Part, part_id)
        if not part_obj:
            abort(404)
        if request.method == "GET":
            return jsonify(part_obj.to_dict()), 200
        if request.method == "PUT":
            part_attr = request.get_json()
            if not part_attr or type(part_attr) is not dict:
                abort(400, "Invalid input")
            for key, value in part_attr.items():
                if key not in ["id", "created_at", "updated_at"]:
                    setattr(part_obj, key, value)
            part_obj.save()
            return jsonify(part_obj.to_dict()), 201
        if request.method == "DELETE":
            part_obj.delete()
            storage.save()
            return jsonify({}), 200