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
    SERVER_NAME = 'localhost:8888'


# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST']

API_VERSION = 'v1'
URL_PREFIX = 'xinsun'

# Enable reads (GET), edits (PATCH) and deletes of individual items
# (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'DELETE']
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# We enable standard client cache directives for all resources exposed by the
# API. We can always override these global settings later.
#CACHE_CONTROL = 'max-age=20'
#CACHE_EXPIRES = 20

# Our API will expose two resources (MongoDB collections): 'people', 'jokes', 'comments', 'likes',
# 'categories', 'messages', 'subscriptions'.
# In order to allow for proper data validation, we define beaviour
# and structure.

people = {
    # 'title' tag used in item links.
    'item_title': 'person',
    'additional_lookup': {
        'url': '[\d]+',
        'field': 'username'
    },
    'datasource': {
        'projection': {
            '_id' : 1,
            'username' : 2,
            'password' : 3,
            'account_type' : 4, 
            'email' : 5,
            'sex' : 6, 
            'birthday' : 7, 
            'profile_title' : 8, 
            'profile_content' : 9, 
            'jokes_number' : 10,
            'comments_number' : 11,
            'likes_number' : 12,
            'dislikes_number' : 13,
            'updated' : 14,
            'created' : 15
            }
    },

    'schema': {
        'username': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 30,
            'required' : True,
            'unique' : True,
        },
        'password': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 30,
            'required' : True,
        },
        'account_type': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 1,
            'required' : True,
            'allowed' : ['R', 'W', 'M', 'A'], 
        },
        'email': {
            'type': 'string',
            'minlength': 8,
            'maxlength': 100,
            'required' : True,
        },
        'sex': {
            'type': 'boolean',
            'required' : True,
        },
        'birthday': {
            'type': 'datetime',
            'required' : True,
        },
        'profile_title': {
            'type': 'string',
            'minlength': 0,
            'maxlength': 50,
            'required' : True,
        },
        'profile_content': {
            'type': 'string',
            'minlength': 0,
            'maxlength': 500,
            'required' : True,
        },
        'profile_pic': {
            'type': 'string',
            'minlength': 0,
            'maxlength': 500,
        },
        'jokes_number': {
            'type': 'integer',
            'readonly' : True,
        },
        'comments_number': {
            'type': 'integer',
            'readonly' : True,
        },
        'likes_number': {
            'type': 'integer',
            'required' : True,
        },
        'dislikes_number': {
            'type': 'integer',
            'required' : True,
        }
    }
}

jokes = {
    # 'title' tag used in item links.
    'item_title': 'joke',
    'additional_lookup': {
        'url': '[\d]+',
        'field': '_id'
    },
    'datasource': {
        'projection': {
            '_id' : 1,
            'author_id' : 2,
            'language' : 3,
            'category' : 4, 
            'title' : 5,
            'content' : 6, 
            'likes_number' : 7, 
            'dislikes_number' : 8,
            'comments_number' : 9,
            'shares_number' : 10,
            'last_updated_by' : 11,
            'updated' : 12,
            'created' : 13
            }
    },
    'schema': {
        'author_id': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 30,
            'required' : True,
        },
        'device_id': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 50,
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
            'type': 'integer',
            'required' : True,
        },
        'dislike_number': {
            'type': 'integer',
            'required' : True,
        },
        'share_number': {
            'type': 'integer',
            'required' : True,
        },
        'comment_number': {
            'type': 'integer',
            'required' : True,
        }
    }
}

comments = {
    # 'title' tag used in item links.
    'item_title': 'comment',
    'additional_lookup': {
        'url': '[\d]+',
        'field': '_id'
    },
    'datasource': {
        'projection': {
            '_id' : 1,
            'joke_id' : 2,
            'author_id' : 3,
            'content' : 4, 
            'last_updated_by' : 5,
            'udpated' : 6,
            'created' : 7
            }
    },
    'schema': {
        'joke_id': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 20,
            'required' : True,
        },
        'author_id': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 30,
            'required' : True,
        },
        'device_id': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 50,
            'required' : True,
        },
        'content': {
            'type': 'string',
            'minlength': 10,
            'maxlength': 4000,
            'required' : True,
        },
        'last_updated_by': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 30,
            'required' : True,
        }
    }
}

likes = {
    # 'title' tag used in item links.
    'item_title': 'like',
    'additional_lookup': {
        'url': '[\d]+',
        'field': '_id'
    },
    'datasource': {
        'projection': {
            '_id' : 1,
            'joke_id' : 2,
            'author_id' : 3,
            'liked' : 4,
            'updated' : 5, 
            'created' : 6 
            }
    },
    'schema': {
        'joke_id': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 20,
            'required' : True,
        },
        'author_id': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 30,
            'required' : True,
        },
        'device_id': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 50,
            'required' : True,
        },
        'liked': {
            'type': 'boolean',
            'required' : True,
        }
    }
}

categories = {
    # 'title' tag used in item links.
    'item_title': 'category',
    'additional_lookup': {
        'url': '[\d]+',
        'field': 'short_name'
    },
    'datasource': {
        'projection': {
            '_id' : 1,
            'short_name' : 2,
            'language' : 3,
            'name' : 4, 
            'description' : 5, 
            'count' : 6, 
            'hidden' : 7 
            }
    },
    'schema': {
        'short_name': {
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
        'name': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 50,
            'required' : True,
        },
        'description': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 100,
            'required' : True,
        },
        'count': {
            'type': 'integer',
            'required' : True,
        },
        'hidden': {
            'type': 'boolean',
            'required' : True,
        }
    }
}




# The DOMAIN dict explains which resources will be available and how they will
# be accessible to the API consumer.
DOMAIN = {
    'people': people,
    'jokes': jokes,
    'comments': comments,
    'likes': likes,
    'categories': categories,
#    'messages': messages,
#    'subscriptions': subscriptions,
}
