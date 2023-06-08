from django.shortcuts import render
from djagno.http import HttpResponse
from datetime import datetime,timedelta
# Create your views here.
def home(request):
    response = render(request,'home.html')
    response.set_cookie('name', 'rahim')
    response.set_cookie('name', 'karim',expires=datetime.utcnow()+timedelta(days=7))
    return response
def get_cookie(request):
    name = request.COOKIES.get('name')
    return render(request,'get_cookie.html',{'name':name})

def delete_cookie(request):
    response = render(request,'delete.html')
    response.delete_cookie('name')
    return response

def set_session(request):
    # data = {
    #     'name': 'rahim',
    #     'age': 23,
    #     'language': 'Bangla'
    # }
    # request.session.update(data)
    request.session['name'] = 'Karim'
    return render(request,'set_session.html')

def get_session(request):
    if 'name' in request.session:
        name = request.session.get('name','Guest')
        request.session.modified = True
        return render(request, 'get_session.html',{'name':name})
    else:
        return HttpResponse('Your session has been expired. Login again.')

def delete_session(request):
    request.session.flush()
    return render(request,'session_delete.html')