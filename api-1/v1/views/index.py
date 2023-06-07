#!/usr/bin/pyhton3
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.vehicle import Vehicle
from models.client import Client
from models.bid import Bid
from models.job import Job
from models.mechanic import Mechanic
from models.image import Image
from models.review import Review
from models.order import Order
from models.vendor import Vendor
from models.part import Part


@app_views.route('/status', strict_slashes=False)
def status():
    """return api status"""
    return jsonify({"status": "OK"})

@app_views.route('stats', strict_slashes=False)
def objects_count():
    """Retrieve num of objects of each type"""
    classes = [Client, Bid, Job, Mechanic, Image, Review, Order, Vendor, Part, Vehicle]
    class_names = ['clients', 'bids', 'jobs', 'mechanics', 'images', 'reviews', 'orders', 'vendors', 'parts', 'vehicles']

    obj_count = {}
    for i in range(len(classes)):
        obj_count[class_names[i]] = storage.count(classes[i])
    return jsonify(obj_count)
    
    