#!/usr/bin/python3

from models.base_model import BaseModel
from models.client import Client
from models.mechanic import Mechanic
from models.vendor import Vendor
from models.bid import Bid
from models.job import Job
from models.order import Order
from models.image import Image
from models.part import Part
from models.review import Review
from models.vehicle import Vehicle
from models import storage

if __name__ == "__main__":
    client1 = Client(first_name="first", last_name="last", email="firstlast@email.com", password="pwd2023", phone_number=84823)
    client1.save()
    mech1 = Mechanic(first_name="Jake", last_name="Kim", email="jakekim@email.com", phone_number=789097789, business_name="Jake Garage",  jobs_completed=2, rating=2)
    mech1.save()
    rev1 = Review(client_id=client1.id, mechanic_id=mech1.id, description="Good guy", rating=5)
    rev1.save()