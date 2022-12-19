from django.urls import path
from . import views

app_name = 'thevision'

urlpatterns = [
    path('', views.support_create, name='support_create'),
    path('support_list/<int:support_id>/', views.detail, name='detail'),
    path('support_list/', views.index, name='index'),
    path('support_list/delete/<int:support_id>/', views.delete, name='delete'),
    path('support_list/insert/<int:support_id>/', views.insert, name='insert'),
    path('activity/', views.activity_create, name='activity_create'),
    path('activity_list/', views.activity_list, name='activity_list'),
    path('activity_list/<int:activity_id>/', views.detail2, name='detail2'),
    path('test/fetch/', views.support_fetch, name='fetch'),
    path('save/', views.support_save, name='save'),
    path('json/', views.json_Data),
    path('Time_Request/', views.Time_Request)
]