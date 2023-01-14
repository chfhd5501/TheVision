import json
import traceback
from venv import logger
from rest_framework import status

from django.db.models.functions import datetime
from django.http import JsonResponse, HttpResponse, Http404
from django.template import loader
from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from .models import Support, Group, Question
from .forms import SupportForm, QuestionForm, SupportForm2, AnswerForm
from argon2 import PasswordHasher
from django.db.models import Q

def support_create(request):
    try:
        if request.method=='POST':
            form = SupportForm(request.POST)
            if form.is_valid():
                support = form.save(commit=False)
                support.save()
                id_data=support.id
                password_hash=Support.objects.get(id=id_data)
                password_hash.password=PasswordHasher().hash(password_hash.password)
                password_hash.save()
                data = {
                    'message': '',
                    'status': 'success'}
                return HttpResponse(json.dumps(data, ensure_ascii=False), "application/json")
                #return redirect('thevision:index')
        else:
            form = SupportForm()
        context = {'form' : form }
        return render(request, 'thevision/support_form.html', context) #프론트 url로 바꿔야함
    #except KeyError:
    except Exception as e:
        trace_back = traceback.format_exc()
        message = str(e) + "\n" + str(trace_back)
        return JsonResponse({"message": message}, status=status.HTTP_400_BAD_REQUEST)

class SupportView(View):
    model=Support
    def post(self, request):
        data = json.loads(request.body)
        try:
            Support.objects.create(
                name = data['name'],
                department = data['department'],
                undergrad = data['undergrad'],
                password = data['password'],
                phone_number = data['phone_number'],
                application_field = data['application_field']
            )
            return JsonResponse({"MESSAGE": "SUCCESS"}, status=201)
        except Exception as e:
            trace_back = traceback.format_exc()
            message = str(e) + "\n" + str(trace_back)
            return JsonResponse({"message": message}, status=status.HTTP_400_BAD_REQUEST)


def detail(request, support_id):
    try:
        #support = get_object_or_404(Support, pk=support_id)
        support = Support.objects.get(pk=support_id)
        context = {'support': support}
    except Support.DoesNotExist:
        raise Http404("member does not exist")
    return render(request, 'thevision/support_detail.html', context)

def index(request):
    try:
        support_list = Support.objects.all()
        context = {'support_list': support_list}
    except Support.DoesNotExist:
        return HttpResponse({"message" : "model error"}, status=status.HTTP_404_NOT_FOUND)
    return render(request, 'thevision/support_list.html', context)


def delete(request, support_id):
    try:
        support = get_object_or_404(Support, pk=support_id)
        support.delete()
        return redirect('thevision:index')
    except Support.DoesNotDelete:
        return HttpResponse({"message": "delete error"}, status=status.HTTP_406_NOT_ACCEPTABLE)

def insert(request, support_id):
    support = Support.objects.get(id=support_id)
    name=support.name
    department=support.department
    undergrad=support.undergrad
    password=support.password
    phone_number=support.phone_number
    application_field=support.application_field

    group_data = Group(name=name, department=department,
                  undergrad=undergrad, password=password,
                  phone_number=phone_number, application_field=application_field)
    group_data.save()
    support.delete()
    return redirect('thevision:index')


def question_create(request):
    try:
        if request.method == 'POST':
            form = QuestionForm(request.POST)
            if form.is_valid():
                question = form.save(commit=False)
                question.create_date = timezone.now()
                question.save()
                return redirect('thevision:question_list')
        else:
            form = QuestionForm()
        context = {'form': form}
        return render(request, 'thevision/activity_form.html', context)
    except Exception as e:
        trace_back = traceback.format_exc()
        message = str(e) + "\n" + str(trace_back)
        return JsonResponse({"message": message}, status=status.HTTP_400_BAD_REQUEST)


def question_list(request):
    try:
        question_list = Question.objects.order_by('-create_date')
        context = {'question_list': question_list}
    except Question.DoesNotExist:
        return HttpResponse({"message": "model error"}, status=status.HTTP_404_NOT_FOUND)
    return render(request, 'thevision/activity_list.html', context)

def detail2(request, question_id):
    try:
        question = Question.objects.get(id=question_id)
        context = {'question': question}
    except Support.DoesNotExist:
        raise Http404("member does not exist")
    return render(request, 'thevision/activity_detail.html', context)

def delete2(request, question_id):
    try:
        question = get_object_or_404(Question, pk=question_id)
        question.delete()
        return redirect('thevision:question_list')
    except Question.DoesNotDelete:
        return HttpResponse({"message": "delete error"}, status=status.HTTP_406_NOT_ACCEPTABLE)


def answer_create(request, question_id):
    try:
        question = get_object_or_404(Question, pk=question_id)
        if request.method == 'POST':
            form = AnswerForm(request.POST)
            if form.is_valid():
                answer = form.save(commit=False)
                answer.create_date = timezone.now()
                answer.question = question
                answer.save()
                return redirect('thevision:detail2', question_id=question_id)
        else:
            form = AnswerForm()
        context = {'question' : question, 'form' : form}
        return render(request, 'thevision/activity_detail.html', context)
    except Exception as e:
        trace_back = traceback.format_exc()
        message = str(e) + "\n" + str(trace_back)
        return JsonResponse({"message": message}, status=status.HTTP_400_BAD_REQUEST)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ front로 데이터 전송
@csrf_exempt
def json_Data(request):
    #json_data = {
        #'status' : 'success',
        #'error' : ['되려나','걍','해보기']
    #}
    #return JsonResponse(json_data)
    try:
        context={
        'message' : 'success',
        'error' : '없음'}
    except Exception as e:
        trace_back = traceback.format_exc()
        message = str(e) + "\n" + str(trace_back)
        logger.error('[FAIL] %s', message)
    return HttpResponse(json.dumps(context, ensure_ascii=False),"application/json")
    #return JsonResponse({'comment': serializer.data}, safe=False)
    #return JsonResponse(data={}, status=400)


def support_fetch(request):
    support_data = Support.objects.all()
    support_list = []
    for index, support in enumerate(support_data, start=1):
        support_list.append({
            'id': index,
            'name' : support.name,
            'department' : support.department,
            'undergrad' : support.undergrad,
            'password' : support.password,
            'phone_number' : support.phone_number,
            'application_field' : support.application_field
        })

    return JsonResponse(support_list, safe=False)


@csrf_exempt
def support_save(request):
    if request.body:
        data = json.loads(request.body)
        if 'support_data' in data:
            support_data = data['support_data']
            Support.objects.all().delete()
            for support in support_data:
                print('support', support)
                form = SupportForm2(support)
                if form.is_valid():
                    form.save()
    return JsonResponse({})


def test2(request):
    return JsonResponse({
            'type' : 'buttons',
            'buttons' : ['1','2','3','4']
    })


@csrf_exempt
def message(request):
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    name = received_json_data['content']

    return JsonResponse({
            'message': { name + '내용받기?'},
            'keyboard': {
                    'type': 'buttons',
                    'buttons':['1','2','3','4']
            }
    })
