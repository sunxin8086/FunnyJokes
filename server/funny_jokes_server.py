#!/usr/bin/python
from bottle import route, post, get, put, run, request, response, static_file, HTTPError
from daemon import Daemon
from wsgiref.util import is_hop_by_hop
import sys
import getopt
import os
import json
import re
import urlparse
import urllib

class FunnyJokesServer(Daemon):
    def run_daemon(self):
        run(host='0.0.0.0', port=8088, debug=True)
        
@route('/')
def hello():
    return "This is the funny jokes server" 

@route('/error')
def error():
    raise HTTPError(404, "No such board.")

def main():
    """
    Funny Jokes Server is the back end server that supports the Funny Jokes app across all platform. 
    Its a full restful service that will support retrieve, add, edit jokes, etc. 
    """

    daemon = FunnyJokesServer('/tmp/funnyjokesserver.pid', '/dev/null', '/tmp/funnyjokesserver.out', '/tmp/funnyjokesserver.err')
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
            print "starting the Funny Jokes Server"
            print "stdout log is located at /tmp/funnyjokesserver.out"
            print "stderr log is located at /tmp/funnyjokesserver.err"
            daemon.start()           
        if o in ("--stop"):
            print "stopping the Funny Jokes Server"
            daemon.stop()
    # process arguments
if __name__ == "__main__":
    main()
