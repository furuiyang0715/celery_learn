from django.http import HttpResponse
from .tasks import my_task


def index(request):
    my_task.delay()
    return HttpResponse("<h1>服务器返回响应内容!</h1>")
