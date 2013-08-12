#/usr/bin/python
from pymongo import Connection
from datetime import datetime
import json
schemas = { 'people' : {
   "_id" : 'd',
   "username" : 0,
   "password" : 1,
   "account_type" : 2,
   "email" : 3,
   "sex" : 4,
   "birthday" : 5,
   "profile_title" : 6,
   "profile_content" : 7,
   "profile_pic" : 8,
   "jokes_number" : 9,
   "comments_number" : 10,
   "likes_number" : 11,
   "dislikes_number" : 12,
   "last_udpated_by" : 'a',
   "updated" : 13,
   "created" : 14
},

'jokes' : {
   "_id" : 0,
   "author_id" : 1,
   "device_id" : 2,
   "language" : 3,
   "category" : 4,
   "title" : 5,
   "content" : 6,
   "likes_number" : 7,
   "dislikes_number" : 8,
   "comments_number" : 9,
   "shares_number" : 10,
   "last_udpated_by" : 'a',
   "updated" : 11,
   "created" : 12
},

'comments' : {
   "_id" : 0,
   "joke_id" : 1,
   "author_id" : 2,
   "device_id" : 3,
   "content" : 4,
   "last_udpated_by" : 'a',
   "updated" : 5,
   "created" : 6
},

'likes' : {
   "_id" : "d",
   "joke_id" : 0,
   "author_id" : 1,
   "device_id" : 2,
   "liked" : 3,
   "updated" : 4,
   "created" : 5
},

'categories' : {
   "_id" : "d",
   "short_name" : 0,
   "language" : 1,
   "name" : 2,
   "description" : 3,
   "count" : 4,
   "hidden" : 5
}
}
collection_name = 'categories'
input_file = '%s_06_01_2013.csv' % collection_name
output_file = '%s_json.txt' % collection_name
schema = schemas[collection_name] 

f = open(input_file, 'r')
j = open(output_file, 'w')


conn = Connection()
db = conn.funny_jokes
collection = db[collection_name]
linenum = 0
for line in f:
    if linenum == 0:
        linenum = linenum + 1
        continue
    entry = {} 
    line = line.strip()
    if line != '':
        items = line.split('|')
    for key in schema.keys():
        value = schema[key]
#getting raw value begins
        if isinstance(value, int):
            item = items[value]
        if value == 'd':
            item = str(linenum)
        if value == 'a':
            item = 'sunxin8086'
#getting raw value ends
#transform data begins
        if item == 'NULL':
            item = ''
        if 'number' in key or key in ('count'):
            item = int(item)
        if key in ('created', 'updated'):
            item = datetime.strptime(item, '%Y-%m-%d %H:%M:%S.%f') 
        if key in ('birthday'):
            item = datetime.strptime(item, '%Y-%m-%d') 
        if key in ('liked', 'hidden', 'sex'):
            if item == '1':
                item = True
            else:
                item = False
        if key == 'sex':
            if item == '1':
                item = True
            else:
                item = False
        entry[key] = item
#transform data ends
    linenum = linenum + 1
    print linenum
    collection.insert(entry)
    j.write(str(entry) + '\n')
    #if linenum > 50:
    #    break
f.close()
j.close()
