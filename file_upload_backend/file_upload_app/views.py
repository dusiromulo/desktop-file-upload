from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
import os
import errno
import json


dir_path = os.path.dirname(os.path.realpath(__file__))


def handle_uploaded_file(file, filename):
    path_to_upload = os.path.join(dir_path, '..', 'uploads', filename)
    if not os.path.exists(os.path.dirname(path_to_upload)):
        try:
            os.makedirs(os.path.dirname(path_to_upload))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    with open(path_to_upload, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()


@csrf_exempt
def upload_file(request):
    if request.method == 'POST':
        if 'file' in request.FILES and 'filename' in request.POST and 'username' in request.POST:
            handle_uploaded_file(request.FILES['file'], request.POST['username'] + '/' + request.POST['filename'])
            data = json.dumps({})
            return HttpResponse(data, status=200, content_type="application/json")
        return HttpResponse("", status=400, content_type="application/json")
    return HttpResponse("", status=404, content_type="application/json")


@csrf_exempt
def login(request):
    if request.method == 'POST':
        if 'username' in request.POST and 'password' in request.POST:
            users_qset = User.objects.filter(username=request.POST['username'])
            if len(users_qset) > 0:
                user = users_qset[0]
                if user.password == request.POST['password']:
                    return HttpResponse("", status=200, content_type="application/json")
                return HttpResponse("", status=401, content_type="application/json")
            return HttpResponse("", status=401, content_type="application/json")
        return HttpResponse("", status=400, content_type="application/json")
    return HttpResponse("", status=404, content_type="application/json")
