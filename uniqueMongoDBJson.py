# -*- coding:utf-8 -*-
"""
Dec: 基于排序后的JSON文本去重
Created on: 2018.01.26
Author: Iflier
Modified on: 2018.01.30
一直删除到这个mmid对应的文档数只剩下一个为止
"""
import os.path
import json
from queue import Queue

import redis
from pymongo import MongoClient

cacheClient = redis.StrictRedis(decode_responses=True)
mongoClient = MongoClient()
db = mongoClient.fortest
que = Queue()

# 唯一id保存到队列
for i in cacheClient.lrange("idver4", 0, -1):
    que.put(i)
print("Toally, put {0} items.".format(que.qsize()))

while not que.empty():
    id = que.get()
    print("[INFO] Remaind {0} items.".format(que.qsize()))
    while db.DirtyJson.find({"xxx": id}).count() > 1:
        # 如果带有这个id的元素的个数大于1，就会一直删除到等于1为止
        db.DirtyJson.delete_one({"xxx": id})
        print("ID: {0}, remaind {1}".format(id, db.DirtyJson.find({"xxx": id}).count()))
print("Done.")
