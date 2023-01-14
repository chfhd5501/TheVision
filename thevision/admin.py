from django.contrib import admin
from .models import Support, Group, Question, Answer

class SupportAdmin(admin.ModelAdmin):
    search_fields = ['name','undergrad']

class GroupAdmin(admin.ModelAdmin):
    search_fields = ['name','undergrad']

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Support, SupportAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)