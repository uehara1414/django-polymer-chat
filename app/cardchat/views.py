from django.shortcuts import render
from django.http import JsonResponse

def hello_world(request):
    return JsonResponse({"status": "hello world"})