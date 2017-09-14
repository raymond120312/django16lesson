# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Post
from django.template.loader import get_template
from datetime import datetime
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# Create your views here.

def homepage(req):
    posts = Post.objects.all()
    now = datetime.now()
    template = get_template('index.html')
    html = template.render(locals())
    return HttpResponse(html)

def showpost(req, slug):
    template = get_template('post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
