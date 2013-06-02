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
from eve import Eve

class FunnyJokesEveServer(Daemon):
    def run_daemon(self):
        app = Eve()
        app.run(host='localhost', port=5001)
        
def main():
    """
    Funny Jokes Server is the back end server that supports the Funny Jokes app across all platform. 
    Its a full restful service that will support retrieve, add, edit jokes, etc. 
    """

    daemon = FunnyJokesEveServer('/tmp/funnyjokeseveserver.pid', '/dev/null', '/tmp/funnyjokeseveserver.out', '/tmp/funnyjokeseveserver.err')
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
            print "stdout log is located at /tmp/funnyjokeseveserver.out"
            print "stderr log is located at /tmp/funnyjokeseveserver.err"
            daemon.start()           
        if o in ("--stop"):
            print "stopping the Funny Jokes Eve Server"
            daemon.stop()
    # process arguments
if __name__ == "__main__":
    main()
