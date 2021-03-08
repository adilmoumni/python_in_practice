from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

import json

from .models import Idea


def index(request):
    idea = Idea.objects.all()
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')


def get_idea(request, idea_name):
    if request.method == "GET":
        try:
            idea = Idea.objects.get(title=idea_name)
            response = json.dumps(
                [{'idea': idea.title, 'description': idea.description}])
        except:
            response = json.dumps([{'Error': 'No idea with that name'}])
    return HttpResponse(response, content_type="text/json")


@csrf_exempt
def add_idea(request):
    if request.method == 'POST':
        payload = json.loads(request.body)
        title = payload['title']
        description = payload['description']
        idea = Idea(title=title, description=description)
        try:
            idea.save()
            response = json.dumps([{'Success': 'Idea added sucessfylly'}])
        except:
            response = json.dumps([{'Error': 'Idea not added sucessfylly'}])
        return HttpResponse(response, content_type='text/json')
    else:
        response = json.dumps([{}])
        return HttpResponse(response, content_type='text/json')
