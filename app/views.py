from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
from .models import Group
import requests
import json


def Output(request):
    number = [2,3,4,2,2]
    return JsonResponse({'number':number})


def home(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        group = Group.objects.filter(group_name=group_name).first()

        if not group:
            group = Group(group_name=group_name)
            group.save()

        return redirect('index', group_name=group_name)
    
    return render(request, 'app/home.html')


def index(request, group_name):
    group = Group.objects.get(group_name=group_name)
    
    # if request.method == 'POST':
    #     code = request.POST.get('code')
    #     output = compile_and_run(code)
    #     return JsonResponse({'output': output})
    
    return render(request, 'app/index.html', {'groupname': group_name, 'group': group})
