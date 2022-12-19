from django import forms
from thevision.models import Support, Activity

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

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['subject', 'content', 'member']
        labels = {
            'subject': '제목',
            'content': '내용',
            'member' : '참여자',
        }

class SupportForm2(forms.ModelForm):
    class Meta:
        model = Support
        fields = ['name', 'department', 'undergrad', 'password', 'phone_number', 'application_field']