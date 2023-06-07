#!/usr/bin/python3
"""Handles client api"""


from api.v1.views import app_views
from models import storage
from models.client import Client
from models.job import Job
from flask import request, jsonify, abort

@app_views.route("/clients", methods=["GET", "POST"],strict_slashes=False)
@app_views.route("/clients/<client_id>", methods=["GET", "PUT", "DELETE"], strict_slashes=False)
def get_all_clients(client_id=None):
    all_clients = storage.all(Client).values()

    clients_list = [client.to_dict() for client in all_clients]

    if not client_id:
        if request.method == "GET":
            return jsonify(clients_list), 200

        elif request.method == "POST":
            my_dict = request.get_json()
            if not my_dict:
                abort(400, "Invalid Input")
            if my_dict.get("first_name") is None or \
                my_dict.get("last_name") is None or \
                my_dict.get("phone_number") is None or \
                my_dict.get("password") is None or \
                my_dict.get("email") is None:
                abort(400, "Incomplete Information")

            else:
                client_obj = Client(**my_dict)
                client_obj.save()
                return jsonify(client_obj.to_dict()), 201
    else:
        client_obj = storage.get(Client, client_id)

        if not client_obj:
            abort(404, "Client not Found")

        if request.method == "GET":
            return jsonify(client_obj.to_dict()), 200

        elif request.method == "PUT":
            my_dict = request.get_json()

            if not my_dict:
                abort(400, "Invalid input")

            else:
                for key, val in my_dict.items():
                    setattr(client_obj, key, val)
                client_obj.save()
                return jsonify(client_obj.to_dict()), 201
        else:
            storage.delete(client_obj)
            storage.save()
            return jsonify({}), 200


@app_views.route("/clients/<client_id>/jobs", strict_slashes=False)
def get_client_jobs(client_id=None):
    "get all jobs posted by client"

    if not client_id:
        abort(400, "Path not recognized")

    client_obj = storage.get(Client, client_id)

    if not client_obj:
        abort(404, "Not Found")
    else:
        client_jobs = [client_job.to_dict() for client_job in client_obj.jobs]
        return jsonify(client_jobs), 200


@app_views.route("/clients/<client_id>/orders", strict_slashes=False)
def get_client_orders(client_id=None):
    """get all orders posted by a client"""

    if not client_id:
        abort(400, "Path not Recognized")

    client_obj = storage.get(Client, client_id)

    if not client_obj:
        abort(404, "Not Found")

    else:
        client_orders = [client_order.to_dict() for client_order in client_obj.orders]
        return jsonify(client_orders), 200
