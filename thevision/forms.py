from django import forms
from thevision.models import Support, Question, Answer

class SupportForm(forms.ModelForm):
    class Meta:
        model = Support
        fields = ['name', 'department', 'undergrad', 'password', 'phone_number', 'application_field']
        labels = {
            'name': '이름',
            'department': '학과',
            'undergrad': '학번(아이디)',
            'password': '비밀번호',
            'phone_number': '전화번호',
            'application_field': '분야',
        }

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }
        #widgets = {
            #'subject' : forms.TextInput(attrs={'class':'form-control'}),
            #'content' : forms.Textarea(attrs={'class':'form-control', 'rows':10}),
        #}

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변 내용',
        }

class SupportForm2(forms.ModelForm):
    class Meta:
        model = Support
        fields = ['name', 'department', 'undergrad', 'password', 'phone_number', 'application_field']