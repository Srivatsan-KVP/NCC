from django.shortcuts import render, redirect
from django.http.response import JsonResponse

import uuid
from utils import isLogged
from . import models

# Create your views here.
def login(req):
    if isLogged(req): return redirect(to='/master/')
    
    if req.method == 'POST':
        data = {'valid': req.POST['auth'] == '231bb39407658b596e860c5911ff7b1059d45879a6a740036457c1fc084502f5',
                 'message': 'Incorrect password'}

        res = JsonResponse(data)
        if data['valid']:
            res.set_cookie('logged_in', True, max_age=1800)
        
        return res

    return render(req, 'server/login.html')



def master(req):
    if not isLogged(req): return redirect(to='/login/')

    if req.method == 'POST':

        if req.POST['action'] == 'update':

            if req.POST['entity'] == 'batch':
                if req.POST['uid'] == "":
                    models.Batch(label=req.POST['label']).save()
                    return JsonResponse({ 'valid': True })
                
                models.Batch.objects.filter(uid=uuid.UUID(req.POST['uid'])).update(label=req.POST['label'])
                return JsonResponse({ 'valid': True })
                
            else:
                batch = models.Batch.objects.filter(uid=uuid.UUID(req.POST['buid']))
                if len(batch) == 0:
                    return JsonResponse({ 'valid': False, 'message': 'Batch not found' })
                
                batch = batch[0]
                if req.POST['uid'] == "":
                    cdt = models.Cadet(name=req.POST['name'].strip(), batch=batch)
                    cdt.save()
                    return JsonResponse({ 'valid': True, 'uid': cdt.uid.hex })
                
                models.Cadet.objects.filter(uid=uuid.UUID(req.POST['uid'])).update(name=req.POST['name'])
                return JsonResponse({ 'valid': True })
            
        else:
            model = models.Batch 
            if req.POST['entity'] != 'batch': model = models.Cadet

            model.objects.filter(uid=uuid.UUID(req.POST['uid'])).delete()
            return JsonResponse({ 'valid': True })
    
    
    data: dict[models.Batch, list[models.Cadet]] = {}
    for batch in models.Batch.objects.all(): data[batch] = []
    for cadet in models.Cadet.objects.all(): data[cadet.batch].append(cadet)

    return render(req, 'server/master.html', {
        'batches': models.Batch.objects.all(),
        'data': data
    })