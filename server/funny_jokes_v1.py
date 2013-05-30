from bottle import route, get, request, HTTPError, static_file
import os

@get('/v1/jokes')
def get_jokes():
    file_name = 'jokes.json'
    if os.path.isfile("test_data/" + file_name):
        return static_file(file_name, root='test_data')
    else:
        raise HTTPError(404, "%s not found" % file_name)
