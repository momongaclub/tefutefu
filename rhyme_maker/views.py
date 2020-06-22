from django.http import HttpResponse
from django.shortcuts import render

from .application import get_string2print
from .application import make_rhyme

# html側で呼ばれるメソッドをここに書く

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
        query_word = make_rhyme.get_query_word(req.GET.get('input_data'))
        rhymes = make_rhyme.main(req)
        dictionary = {'query_word': 'aaaa'}
        return render(req, 'index.html', dictionary)
        #return HttpResponse()

def exercise(request):
    text = 'テストです。'
    try:
        input_text = request.POST['input_text']
        print(input_text)
        text = input_text
    except:
        return render(request, 'make_rhymes.html')

    #now = datetime.now();
    rhymes = make_rhyme.main(request)
    input_text = request.POST['input_text']
    context = {
        'query_word': input_text,
        'text': rhymes,
    }
    return render(request, 'make_rhymes.html', context)
