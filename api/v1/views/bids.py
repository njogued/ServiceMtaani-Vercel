#!/usr/bin/python3
"""handles api actns for bids"""
from api.v1.views import app_views
from models import storage
from models.job import Job
from models.bid import Bid
from models.mechanic import Mechanic
from flask import abort, request, jsonify

@app_views.route('/jobs/<job_id>/bids', strict_slashes=False,
                 methods=["GET", "POST"])
def get_bids_job_id(job_id):
    job_objs = storage.all(Job).values()
    job_obj = storage.get(Job, job_id)    
    if job_obj is None:
        abort(404, "Invalid jobid")
    for job_obj in job_objs:
        if job_obj.id == job_id:
            job_exists = True
            break
    if not job_exists:
        abort(404)
    if request.method == "GET":
        bid_objs = storage.all(Bid).values()
        list_dict = [obj.to_dict() for obj in bid_objs if obj.job_id == job_id]
        return jsonify(list_dict), 200
    elif request.method == "POST":
        my_dict = request.get_json()
        if not my_dict:
            abort(400, "Not a JSON")
        if not my_dict.get('mechanic_id'):
            abort(400, "Missing mechanic id")
        else:
            my_dict["job_id"] = job_id
            obj = Bid(**my_dict)
            obj.save()
            return jsonify(obj.to_dict()), 201

@app_views.route('/jobs/<job_id>/bids/<bid_id>', strict_slashes=False,
                 methods=["GET", "PUT", "DELETE"])
def get_bids_job_id_bid_id(job_id, bid_id):
    job_obj = storage.get(Job, job_id)
    bid_obj = storage.get(Bid, bid_id)    
    if job_obj is None or bid_obj is None:
        abort(404, "Invalid job or bid id")
    if request.method == "GET":
        if bid_obj.job_id == job_obj.id:
            return jsonify(bid_obj.to_dict()), 200    
    elif request.method == "PUT":
        my_dict = request.get_json()
        if not my_dict:
            abort(400, "Not a JSON")
        if not my_dict.get('mechanic_id'):
            abort(400, "Missing mechanic id")
        else:
            obj = Bid(**my_dict)
            obj.save()
            return jsonify(obj.to_dict()), 201
    elif request.method == "DELETE":
        storage.delete(bid_obj)
        storage.save()
        return jsonify({}), 200
    
@app_views.route('/bids', methods=["GET", "POST"], strict_slashes=False)
@app_views.route("/bids/<bid_id>",
                 methods=["GET", "DELETE", "PUT"], strict_slashes=False)
def get_all_bids(bid_id=None):
    """Returns all jobs"""
    all_bids = storage.all(Bid).values()
    bid_dicts = [obj.to_dict() for obj in all_bids]
    if not bid_id:
        if request.method == "GET":
            return jsonify(bid_dicts), 200
        if request.method == "POST":
            bid_attrs = request.get_json()
            if not bid_attrs or type(bid_attrs) is not dict:
                abort(400, "Invalid input")
            if bid_attrs.get("mechanic_id") is None or \
                bid_attrs.get("job_id") is None or \
                    bid_attrs.get("job_amount") is None:
                abort(400, "Incomplete information")
            mechanic_id = bid_attrs.get("mechanic_id")
            job_id = bid_attrs.get("job_id")
            mech_obj = storage.get(Mechanic, mechanic_id)
            job_obj = storage.get(Job, job_id)
            if not mech_obj:
                abort(404, "Invalid Mechanic Id")
            if not job_obj:
                abort(404, "Invalid Job Id")
            job_obj = Job(**bid_attrs)
            job_obj.save()
            return jsonify(job_obj.to_dict()), 201
        
    else:
        obj = storage.get(Bid, bid_id)
        if not obj:
            abort(404, "Invalid Bid Id")
        if request.method == "GET":
            return jsonify(storage.get(Bid, bid_id).to_dict()), 200
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