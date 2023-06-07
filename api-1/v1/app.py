from models import storage
from api.v1.views import app_views
from flask import Flask
from os import environ


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close_storage(error):
    """closes storage"""
    storage.close()


if __name__ == "__main__":
    host = environ.get("API_HOST")
    port = environ.get("API_PORT")
    app.run(host='0.0.0.0', port=5000, debug=True)
