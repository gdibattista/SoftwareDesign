# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 20:13:30 2014

@author: gianfranco
"""

from pattern.web import Facebook, NEWS, COMMENTS, LIKES

fb = Facebook(license='CAAEuAis8fUgBAIjddb5eck615kBpLhvmwaO9dh1ZBIv6YfsPGu0MhzdILYwAQX90qsmLTZCCeZCrwc0U07mzpE1grLUPAXfxyp6lbZCOD1xz1pzlplGbgM0gKWTKhR4nBYkwdJR9CZB0VDdS0f99IopQ7Uv6VZCyZAhMJnKz1yloCpwM4WNHoAG')
me = fb.profile(id=None) # user info dict
#This part of the code search for the last person that post in my wall that is not me
for post in fb.search(me['id'], type=NEWS, count=1000):
    if post.author[0]!=me['id']:
        amigo_id=post.author[0]
        break
#This part, is similar that the first part but in the friend wall that write my last post
for post in fb.search(amigo_id, type=NEWS, count=1000):
    if post.author[0]!=amigo_id:
        amigo1_id=post.author[0]
        break
#no that is defined the Facebook ID I will use google shortener URL API
#to give the link of the friend of my friend.


import requests
import urllib, urllib2
import json


def goo_shorten_url(url):
    post_url = 'https://www.googleapis.com/urlshortener/v1/url'
    postdata = {'longUrl':url}
    headers = {'Content-Type':'application/json'}
    req = urllib2.Request(
        post_url,
        json.dumps(postdata),
        headers
    )
    ret = urllib2.urlopen(req).read()
    print ret
    return json.loads(ret)['id']
    
print goo_shorten_url('http://www.facebook.com/'+ amigo1_id)#give me the shortener url of my friend



