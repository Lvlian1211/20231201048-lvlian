from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
    """简单的Hello World视图"""
    return HttpResponse("<h1>20231201048 吕莲</h1><p>欢迎来到Django世界！</p>")


def hello_template(request):
    """使用模板的Hello World视图"""
    context = {
        'message': '20231201048 吕莲',
        'welcome': '欢迎使用Django模板系统'
    }
    return render(request, 'hello/hello.html', context)