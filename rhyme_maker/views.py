from django.http import HttpResponse
from django.shortcuts import render

# from .application import get_string2print
from .application import get_string2print

def index(request):
    # string = '踏みたい言葉を入力してください'
    # name = request.GET.get('name')
    # return HttpResponse(string+name)
    return render(request, 'index.html')


def get_data(req):
    if req.method == 'GET':
        # print(req.GET.get('input_data')
        # get_string2print.load_datas('input_data')
        get_string2print.load_datas(req.GET.get('input_data'))
        return HttpResponse()
