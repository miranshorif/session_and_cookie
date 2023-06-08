from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name = 'home'),
    path('get/',views.get_cookie,name = 'get'),
    path('set/',views.set_session,name = 'set'),
    path('get_s/',views.get_session,name = 'get_s'),
    path('del_s/',views.delete_session,name = 'del_s'),
    path('del/',views.delete_cookie,name = 'del')
]
