from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
from .models import Group
import requests
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def run_code(request):
    print("we got you\n\n\n\n")
    if request.method == 'POST':
        code = json.loads(request.body)['code']
        print(code)
        # Replace with your actual API URL and API key
        url = "https://online-code-compiler.p.rapidapi.com/v1/"

        payload = {
	        "language": "python3",
	        "version": "latest",
	        "code": code,
	        "input": None
        }
        headers = {
	        "content-type": "application/json",
	        "X-RapidAPI-Key": "d521d21373mshcd7151dc207daf1p139471jsn6c692100b8a5",
	        "X-RapidAPI-Host": "online-code-compiler.p.rapidapi.com"
        }
        
        response = requests.post(url, json=payload, headers=headers)
        data = response.json()
        print(data['output'])
        
        if response.status_code == 200:
            output = data['output']
        else:
            output = 'Compilation or execution error'
        
        return JsonResponse({'output': output})
    return JsonResponse({'error': 'Invalid request method'})


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
