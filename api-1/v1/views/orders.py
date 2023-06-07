#!/usr/bin/python3
"""API routes for parts"""

from api.v1.views import app_views
from models.order import Order
from models.part import Part
from models import storage
from flask import request, abort, jsonify

@app_views.route('/orders', methods=["GET", "POST"], strict_slashes=False)
@app_views.route('/orders/<order_id>', methods=["GET", "PUT", "DELETE"], strict_slashes=False)
def get_orders(order_id=None):
    all_orders = storage.all(Order)
    if not order_id:
        if request.method == "GET":
            orders_list = [order_obj.to_dict() for order_obj in all_orders.values()]
            return jsonify(orders_list), 200
        if request.method == "POST":
            order_attrs = request.get_json()
            if not order_attrs or type(order_attrs) is not dict:
                abort(400, "Invalid input")
            if order_attrs.get("client_id") is None:
                abort(400, "Incomplete information")
            order_obj = Order(**order_attrs)
            order_obj.save()
            return jsonify(order_obj.to_dict()), 201
    if order_id:
        order_obj = storage.get(Order, order_id)
        if request.method == "GET":
            return jsonify(order_obj.to_dict()), 200
        if request.method == "PUT":
            order_attributes = request.get_json()
            for key, value in order_attributes.items():
                if key not in ["id", "created_at", "updated_at"]:
                    setattr(order_obj, key, value)
            order_obj.save()
            return jsonify(order_obj.to_dict()), 201
        if request.method == "DELETE":
            order_obj.delete()
            storage.save()
            return jsonify({}), 200
        
@app_views.route('/orders/<order_id>/parts', methods=["GET"], strict_slashes=False)
@app_views.route('/orders/<order_id>/parts/<part_id>', methods=["GET", "PUT", "DELETE"], strict_slashes=False)
def order_parts(order_id=None, part_id=None):
    order_obj = storage.get(Order, order_id)
    if not order_obj:
            abort(404)
    if not part_id:
        if request.method == "GET":
            part_list = [part.to_dict() for part in order_obj.parts]
            return jsonify(part_list), 200  
    if part_id:
        part_obj = storage.get(Part, part_id)
        if request.method == "GET":
            return jsonify(part_obj.to_dict()), 200
        if request.method == "DELETE":
            for one_part in order_obj.parts:
                if one_part.id == part_obj.id:
                    order_obj.parts.remove(part_obj)
                    break
            storage.save()
            return jsonify({}), 200