# -*- coding: utf8 -*-

import urllib2
import json

class JsonBasic():

    def __init__(self):
        self.url = "https://itunes.apple.com/cn/rss/topFreeApplications/limit=200/json"

    #抓取url返回的json字符串
    def craw(self):
        response = urllib2.urlopen(self.url)
        response_string = response.read()
        self.parse(response_string)

    def parse(self, json_string):
        try:
            res = json.loads(json_string)
        except BaseException, e:
            print e
        #获取json中的一个列表
        entryList = res['feed']['entry']
        for entry in entryList:
            #获取json中的一个值
            appName = entry['im:name']['label']
            print appName

if __name__ == '__main__':
    jb = JsonBasic()
    jb.craw()

