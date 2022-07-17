import json
import os
from django.shortcuts import render

# Create your views here.


def khuijson(tongmia):
    ui = os.path.join(
        os.path.dirname(__file__),
        'jsons',
        tongmia
    )
    with open(ui, 'r') as tong:
        try:
            tsuliau = json.load(tong)
        except Exception:
            tsuliau = []
    return tsuliau


def siuiah(request):
    context = {}
    context['siosia'] = khuijson('siosia.json')
    context['tuasia'] = khuijson('tuasia.json')
    return render(request, 'kpapp/index.html', context)
