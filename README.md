# [SERVICEMTAANI](/README.md)

The app is designed to be user-friendly and accessible to both clients and mechanics.

Clients are able to create an account and post job requests. The job requests will include the specifics of the work required, such as car service, part changes, or a description of the issue with the car.

Mechanics will be able to create an account, view job requests, and bid on the jobs they are interested in. Clients will be able to choose a mechanic based on a combination of factors such as cost and reputation. Once a client selects a mechanic, the two parties will communicate through the app to arrange for the mechanic to either go to the client's premises to carry out the job or for the client to deliver the car to the mechanic's premises.

Additionally, the app has an online platform for selling car parts


# [Table of Content](#table-of-content)
- [File Descriptions](#file-descriptions)
* [Usage](#usage)
- [Examples of use](#example-of-usage)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#licence)

# [File Descriptions](#file-descriptions)
## [modules/](/models/) directory contains classes used for this project:
### [base_model.py]() - The BaseModel class from which future classes will be derived

- `def __init__(self, **kwargs)` - Initialization of the base model
- `def __str__(self)` - String representation of the BaseModel class
- `def save(self)` - Updates the attribute updated_at with the current datetime
- `def to_dict(self)` - returns a dictionary containing all keys/values of the instance
- `def delete(self)` - Delete the object from the database
- `def update(self, attr, value)` - Update the object attributes

### Classes Inheriting from Base Model:
- [bid.py](/models/bid.py)
- [client.py](/models/client.py)
- [image.py](/models/image.py)
- [job.py](/models/job.py)
- [mechanic.py](/models/mechanic.py)
- [order.py](/models/order.py)
- [part.py](/models/part.py)
- [review.py](/models/review.py)
- [vehicle.py](/models/vehicle.py)
- [vendor.py](/models/vendor.py)

## [/models/engine](/models/engine/) directory contains DBStorage class that handles database methods  :
### [DBstorage.py](/models/engine/dbstorage.py) - Database Storage class
Has the following methods to manage and manipulate dadabase data
- `def __init__(self)` - Initializes mysql db
- `def reload(self)` - Reloads data in the db
- `def new(self, obj)` - Creates a new object
- `def save(self)` - Commits the session to the db to save the changes
- `def delete(self, obj=None)` - Deletes an object
- `def close(self)` - Closes the session
- `def all(self, cls=None)` - Retrieves all objects of a class
- `def get(self, cls, id)` - Method to retrieve one object
- `def find(self, cls=None, attr=None, val=None)`- Return an instance for a db entry
- `def count(self, cls=None)` -
        Return count of the class passed or
        total items in db if no class is passed
- `def openjobs(self)` - Returns a list of open jobs
- `def query_bids(self, client_id, job_id=None)` - Returns all placed bids for client jobs
- `def query_active_jobs(self, client_id)`- Returns all assigned jobs
- `def query_winning_bid(self, job_id)` - Querys the winning bid from the db
- `def query_completed_jobs(self, client_id)` - Finds the completed jobs for a client

## [app_flask/](/app_flask/) - Contains the home.py file which initializes the flask app and defines all the routes necessary for the app functionality with flask
### [home.py](/app_flask/home.py) - Initializes flask app and defines other methods for specific routes
## [app_flask/templates](/app_flask/templates/) - Contains html templates with jinja2 syntax
## [app_flask/static](/app_flask/static/)
- ### [app_flask/static/images](/app_flask/static/images) - Contains static image files
- ### [app_flask/static/scripts](/app_flask/static/scripts) - Contains static js files with jQuery syntax
    - [accept_bids.js](app_flask/static/scripts/accept_bids.js)
        - Accept bid by client
        - Delete bid by mechanic
    - [create_job.js](app_flask/static/scripts/create_job.js)
    - [deletepart.js](app_flask/static/scripts/deletepart.js)
    - [hide_blog.js](app_flask/static/scripts/hide_blog.js)
    - [mechanic_homepage.js](app_flask/static/scripts/mechanic_homepage.js)
    - [modal_bid.js](app_flask/static/scripts/modal_bid.js)
    - [ordered_parts.js](app_flask/static/scripts/ordered_parts.js)
    - [review_job.js](app_flask/static/scripts/review_job.js)
- ### [app_flask/static/styles](/app_flask/static/styles) - Contains static css styling files
    - [button.css](/app_flask/static/styles/button.css) - Buttons styles
    - [main.css](/app_flask/static/styles/main.css) - Landing page styles
    - [styles.css](/app_flask/static/styles/styles.css) - General body styles
    - [vendor_footer.css](/app_flask/static/styles/vendor_footer.css) - Vendor footer styles





# [Usage]()
# [Example of Usage]()
# [Bugs](#bugs)
No bugs reported

# [Authors](/AUTHORS)
List of contributers
1. Edward Njogu | <njogued@gmail.com> | [Github](https://github.com/njogued)
2. Isaac Kiarie | <igitaukiarie@gmail.com> | [Github](https://github.com/GKiarie)
3. Jacob Mdigo | <mdigojacob@gmail.com> | [Github](https://github.com/Mdigo12)
# [License](/LICENSE)
Licensed by MIT










