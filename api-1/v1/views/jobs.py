#!/usr/bin/python3
"""Handles all restful api actns for jobs"""
from api.v1.views import app_views
from models import storage
from models.job import Job
from models.client import Client
from flask import jsonify, request, abort


@app_views.route('/jobs', methods=["GET", "POST"], strict_slashes=False)
@app_views.route("/jobs/<job_id>",
                 methods=["GET", "DELETE", "PUT"], strict_slashes=False)
def get_all_jobs(job_id=None):
    """Returns all jobs"""
    all_jobs = storage.all(Job).values()
    job_dicts = [obj.to_dict() for obj in all_jobs]
    if not job_id:
        if request.method == "GET":
            return jsonify(job_dicts), 200
        if request.method == "POST":
            job_attrs = request.get_json()
            if not job_attrs or type(job_attrs) is not dict:
                abort(400, "Invalid input")
            if job_attrs.get("client_id") is None or \
                job_attrs.get("job_title") is None:
                abort(400, "Incomplete information")
            client_id = job_attrs.get("client_id")
            client_obj = storage.get(Client, client_id)
            if not client_obj:
                abort(404, "Invalid Client Id")
            job_obj = Job(**job_attrs)
            job_obj.save()
            return jsonify(job_obj.to_dict()), 201
        
    else:
        obj = storage.get(Job, job_id)
        if not obj:
            abort(404, "Invalid Job Id")
        if request.method == "GET":
            return jsonify(storage.get(Job, job_id).to_dict()), 200
        elif request.method == "PUT":
            my_dict = request.get_json()
            if not my_dict:
                abort(400, "Not a JSON")
            else:
                ignore_keys = ["id", "created_at", "updated_at"]
                my_dict = {key: value for key, value in my_dict.items() if key
                           not in ignore_keys}
                for k, v in my_dict.items():
                    setattr(obj, k, v)
                obj.save()
                return jsonify(obj.to_dict()), 201
        elif request.method == "DELETE":
            # obj.delete()
            # obj.save()
            storage.delete(obj)
            storage.save()
            return jsonify({}), 200

@app_views.route('<client_id>/jobs', methods=["GET", "POST"], strict_slashes=False)
def get_job_by_client_id(client_id):
    client_objs = storage.all(Client).values()
    client_exists = False
    for client_obj in client_objs:
        if client_obj.id == client_id:
            client_exists = True
            break
    if not client_exists:
        abort(404)
    if request.method == "GET":
        job_objs = storage.all(Job).values()
        list_dict = [obj.to_dict() for obj in job_objs if
                     obj.client_id == client_id]
        return jsonify(list_dict), 200
    elif request.method == "POST":
        my_dict = request.get_json()
        if not my_dict or type(my_dict) is not dict:
            abort(400, "Not a JSON")
        if not my_dict.get('job_title'):
            abort(400, "Missing title")
        else:
            my_dict["client_id"] = client_id
            obj = Job(**my_dict)
            obj.save()
            return jsonify(obj.to_dict()), 201
