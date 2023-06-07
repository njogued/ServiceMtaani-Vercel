#!/usr/bin/python3
"""API routes for parts"""

from api.v1.views import app_views
from models.part import Part
from models.image import Image
from models import storage
from flask import request, abort, jsonify

@app_views.route('/parts', methods=["GET", "POST"], strict_slashes=False)
@app_views.route('/parts/<part_id>', methods=["GET", "PUT", "DELETE"], strict_slashes=False)
def get_parts(part_id=None):
    all_parts = storage.all(Part)
    if not part_id:
        if request.method == "GET":
            parts_list = [part_obj.to_dict() for part_obj in all_parts.values()]
            return jsonify(parts_list), 200
        if request.method == "POST":
            part_attrs = request.get_json()
            if not part_attrs or type(part_attrs) is not dict:
                abort(400, "Invalid input")
            if part_attrs.get("part_name") is None or \
                part_attrs.get("vendor_id") is None or \
                    part_attrs.get("part_price") is None:
                abort(400, "Incomplete information")
            part_obj = Part(**part_attrs)
            part_obj.save()
            return jsonify(part_obj.to_dict()), 201
    if part_id:
        part_obj = storage.get(Part, part_id)
        if request.method == "GET":
            return jsonify(part_obj.to_dict()), 200
        if request.method == "PUT":
            part_attributes = request.get_json()
            for key, value in part_attributes.items():
                if key not in ["id", "created_at", "updated_at"]:
                    setattr(part_obj, key, value)
            part_obj.save()
            return jsonify(part_obj.to_dict()), 201
        if request.method == "DELETE":
            part_obj.delete()
            storage.save()
            return jsonify({}), 200
        
@app_views.route('/parts/<part_id>/images', methods=["GET", "POST"], strict_slashes=False)
@app_views.route('/parts/<part_id>/images/<image_id>', methods=["GET", "PUT", "DELETE"], strict_slashes=False)
def parts_images(part_id=None, image_id=None):
    # all_images = storage.all(Image)
    part_obj = storage.get(Part, part_id)
    if not image_id:
        if request.method == "GET":
            image_list = [image.to_dict() for image in part_obj.images]
            return jsonify(image_list), 200
        if request.method == "POST":
            image_attr = request.get_json()
            if not image_attr or type(image_attr) is not dict:
                abort(400, "Invalid input")
            if image_attr.get("image_path") is None:
                abort(400, "Missing information")
            image_attr["part_id"] = part_id
            image_obj = Image(**image_attr)
            image_obj.save()
            return jsonify(image_obj.to_dict()), 201
        
    if image_id:
        image_obj = storage.get(Image, image_id)
        if not image_obj:
            abort(404)
        if request.method == "GET":
            return jsonify(image_obj.to_dict()), 200
        # if request.method == "PUT":
        #     for key, value in image_attr.items():
        #         if key not in ["id", "created_at", "updated_at"]:
        #             setattr(image_obj, key, value)
        #     image_obj.save()
        #     return jsonify(image_obj.to_dict()), 201
        if request.method == "DELETE":
            image_obj.delete()
            storage.save()
            return jsonify({}), 200
        
@app_views.route('/parts/<part_id>/orders', \
                 methods=["GET"], strict_slashes=False)
def parts_orders(part_id):
    part_obj = storage.get(Part, part_id)
    if not part_obj:
        abort(404)
    if request.method == "GET":
        order_list = [order.to_dict() for order in part_obj.orders]
        return jsonify(order_list), 200
    
@app_views.route('/parts/<part_id>/purchases', strict_slashes=False)
def parts_purchases(part_id):
    part_obj = storage.get(Part, part_id)
    if not part_obj:
        abort(404)
    order_list = [order.to_dict() for order in part_obj.orders]
    len_order_list = len(order_list)
    purchases = f"Orders with {part_obj.part_name}: {len_order_list}"
    return jsonify(purchases), 200