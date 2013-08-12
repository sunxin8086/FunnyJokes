#!/usr/bin/python
from daemon import Daemon
from wsgiref.util import is_hop_by_hop
import sys
import getopt
import os
import json
import re
import urlparse
import urllib
import logging
from logging import FileHandler
from logging import Formatter
sys.path.append('../../Python/eve')
from eve import Eve

class FunnyJokesEveServer(Daemon):
    def run_daemon(self):
        app = Eve()
        app.on_get += general_callback
        app.on_post_joke += post_joke_callback 
        file_handler = FileHandler('/tmp/funny_jokes_eve_server.log')
        file_handler.setLevel(logging.INFO)
        formatter = Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]')
        file_handler.setFormatter(formatter)
        app.logger.addHandler(file_handler)
        app.run(host='localhost', port=8888)
        app.logger.warning("Test Loggin")

def general_callback(resource, request, payload):
    print 'A GET on the "%s" endpoint was just performed!' % resource
    print payload
    print request

def post_joke_callback(request, payload):
    print payload
    print request

def main():
    """
    Funny Jokes Eve Server is the back end server that supports the Funny Jokes app across all platform. Its built on top of Eve framework 
    Its a full restful service that will support retrieve, add, edit jokes, etc. 
    """

    daemon = FunnyJokesEveServer('/tmp/funny_jokes_eve_server.pid', '/dev/null', '/tmp/funny_jokes_eve_server.out', '/tmp/funny_jokes_eve_server.err')
    # parse command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["help", "start", "stop"])
    except getopt.error, msg:
        print msg
        print "for help use --help"
        sys.exit(2)
    # process options
    for o, a in opts:
        if o in ("-h", "--help"):
            print main. __doc__
            sys.exit(0)
        if o in ("--start"):
            print "starting the Funny Jokes Eve Server"
            print "stdout log is located at /tmp/funny_jokes_eve_server.out"
            print "stderr log is located at /tmp/funny_jokes_eve_server.err"
            daemon.start()           
        if o in ("--stop"):
            print "stopping the Funny Jokes Eve Server"
            daemon.stop()
    # process arguments
if __name__ == "__main__":
    main()
