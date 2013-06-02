#/usr/bin/python
from pymongo import Connection
from datetime import datetime
import json
query = """{   
 '_id' = {0},
 'author_id' = '{1}',
 'device_id' = '{2}',
 'language' = '{3}',
 'category' = '{4}',
 'title' = '{5}',
 'content' = '{6}',
 'like_number' = '{7}',
 'dislike_number' = '{8}',
 'share_number' = '{9}',
 'comment_number' = '{10}',
 'updated_by' = '{11}',
 'updated' = '{12}',
 'created' = '{13}'
}"""

dict = {
   "0" : "_id",
   "1" : "author_id",
   "2" : "device_id",
   "3" : "language",
   "4" : "category",
   "5" : "title",
   "6" : "content",
   "7" : "like_number",
   "8" : "dislike_number",
   "9" : "share_number",
   "10" : "comment_number",
   "11" : "last_updated_by",
   "12" : "updated",
   "13" : "created"
}

f = open('joke_06_01_2013.txt', 'r')
j = open('joke_json.txt', 'w')


conn = Connection()
db = conn.funny_jokes
jokes = db.jokes
linenum = 0
for line in f:
    value = {} 
    line = line.strip()
    if line != '':
        items = line.split('\t')
    i = 0
    for item in items:
        if item == 'NULL':
            item = ''
        lookup_key = str(i)
        key = dict[lookup_key] 
        if 'number' in key:
            item = int(item)
        if key in ('created', 'updated'):
            item = datetime.strptime(item, '%Y-%m-%d %H:%M:%S.%f') 
        value[key] = item
        i = i + 1 
        if i == 11:
            lookup_key = str(i)
            key = dict[lookup_key] 
            value[key] = 'sunxin8086' 
            i = i + 1
    linenum = linenum + 1
    print linenum
    jokes.insert(value)
    j.write(str(value) + '\n')
    if linenum > 10:
        break
f.close()
j.close()
