from django.shortcuts import render
from django.shortcuts import render_to_response
import json
import django
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import time
from modles.models import *
# Create your views here.
@csrf_exempt
def login(request):
    if request.method=="POST":
        r = json.loads(request.body)

        print r
        user_id= r["user_id"]
        admin = Administor.objects.filter(id=user_id)
        response_data = {}
        if admin:
            if r['password']==admin[0].password:
                response_data['result'] = 0
                response_data['id'] = user_id
                response_data['auth'] = admin[0].authority
            else:
                response_data['result'] = 1
        else:
            response_data['result'] = 2
        return render_to_response('login.html',response_data)