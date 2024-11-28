from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse
from chudyapp.models.PersonData import PersonData

def indexArticleJson(request):
    articles = PersonData.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type="applicaton/json")

def index(request):
    return HttpResponse("hello world")
# Create your views here.
