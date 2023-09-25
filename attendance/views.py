from django.shortcuts import render, redirect
from django.http.response import JsonResponse

from server import models
from .models import Entry
from utils import isLogged
from datetime import datetime
import json, uuid

def home(req):
    if not isLogged(req): return redirect(to='/login/')

    if req.method == 'GET' and req.GET.get('date', False):
        return JsonResponse({
            'valid': True,
            'data': json.dumps([ entry.cadet.uid.hex for entry in Entry.objects.filter(date=datetime.strptime(req.GET['date'], '%Y-%m-%d').date()) ])
        })
    
    if req.method == 'POST':
        if req.POST['status']:
            Entry(
                cadet=models.Cadet.objects.get(uid=uuid.UUID(req.POST['uid'])),
                date=datetime.strptime(req.POST['date'], '%Y-%m-%d').date()
            ).save()
        else:
            Entry.objects.filter(
                cadet=models.Cadet.objects.get(uid=uuid.UUID(req.POST['uid'])),
                date=datetime.strptime(req.POST['date'], '%Y-%m-%d').date()
            ).delete()

        return JsonResponse({ 'valid': True })

    return render(req, 'attendance/post.html', {'cadets': models.Cadet.objects.all()})