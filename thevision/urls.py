from django.urls import path
from . import views

app_name = 'thevision'

urlpatterns = [
    path('', views.support_create, name='support_create'),
    #path('', views.SupportView.as_view()),
    path('support_list/<int:support_id>/', views.detail, name='detail'),
    path('support_list/', views.index, name='index'),
    path('support_list/delete/<int:support_id>/', views.delete, name='delete'),
    path('support_list/insert/<int:support_id>/', views.insert, name='insert'),
    path('activity/', views.question_create, name='question_create'),
    path('activity_list/', views.question_list, name='question_list'),
    path('activity_list/<int:question_id>/', views.detail2, name='detail2'),
    path('activity_list/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('activity_list/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('test/fetch/', views.support_fetch, name='fetch'),
    path('save/', views.support_save, name='save'),
    path('json/', views.json_Data),
]