# -*- coding: utf-8 -*-

"""
    eve-demo settings
    ~~~~~~~~~~~~~~~~~

    Settings file for our little demo.

    PLEASE NOTE: We don't need to create the two collections in MongoDB.
    Actually, we don't even need to create the database: GET requests on an
    empty/non-existant DB will be served correctly ('200' OK with an empty
    collection); DELETE/PATCH will receive appropriate responses ('404' Not
    Found), and POST requests will create database and collections when needed.
    Keep in mind however that such an auto-managed database will most likely
    perform poorly since it lacks any sort of optimized index.

    :copyright: (c) 2012 by Nicola Iarocci.
    :license: BSD, see LICENSE for more details.
"""

import os

# We want to seamlessy run our API both locally and on Heroku so:
if os.environ.get('PORT'):
    # We're hosted on Heroku!  Use the MongoHQ sandbox as our backend.
    MONGO_HOST = 'alex.mongohq.com'
    MONGO_PORT = 10047
    MONGO_USERNAME = 'evedemo'
    MONGO_PASSWORD = 'evedemo'
    MONGO_DBNAME = 'app9346575'

    # also, correctly set the API entry point
    SERVER_NAME = 'eve-demo.herokuapp.com'
else:
    # Running on local machine. Let's just use the local mongod instance.
    MONGO_HOST = 'localhost'
    MONGO_PORT = 27017
    MONGO_USERNAME = ''
    MONGO_PASSWORD = ''
    MONGO_DBNAME = 'funny_jokes'

    # let's not forget the API entry point
    SERVER_NAME = 'localhost:5001'


# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET']

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET']

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
#CACHE_CONTROL = 'max-age=20'
#CACHE_EXPIRES = 20

# Our API will expose two resources (MongoDB collections): 'people' and
# 'works'. In order to allow for proper data validation, we define beaviour
# and structure.
jokes = {
    # 'title' tag used in item links.
    'item_title': 'joke',
    'additional_lookup': {
        'url': '[\d]+',
        'field': '_id'
    },
    'schema': {
        'author_id': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 20,
            'required' : True,
        },
        'language': {
            'type': 'string',
            'minlength': 3,
            'maxlength': 3,
            'required' : True,
        },
        'category': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 20,
            'required' : True,
        },
        'title': {
            'type': 'string',
            'minlength': 0,
            'maxlength': 50,
        },
        'content': {
            'type': 'string',
            'minlength': 10,
            'maxlength': 4000,
            'required' : True,
        },
        'like_number': {
            'type': 'int',
        },
        'dislike_number': {
            'type': 'int',
        },
        'share_number': {
            'type': 'int',
        },
        'comment_number': {
            'type': 'int',
        }
    }

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>/'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform GET
    # requests at '/people/<lastname>/'.
}

# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = {
    'jokes': jokes,
}
