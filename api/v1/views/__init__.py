from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.jobs import *
from api.v1.views.bids import *
from api.v1.views.mechanics import *
from api.v1.views.clients import *
from api.v1.views.vendors import *
from api.v1.views.reviews import *
from api.v1.views.parts import *
from api.v1.views.orders import *