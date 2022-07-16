import json
import os
from django.shortcuts import render

# Create your views here.


def siuiah(request):
    context = {}
    siosiajson = os.path.join(
        os.path.dirname(__file__),
        'siosia.json'
    )
    with open(siosiajson, 'r') as tong:
        try:
            siosia = json.load(tong)
        except Exception:
            siosia = []
    # sorted(siosia)
    context['siosia'] = siosia
    return render(request, 'kpapp/index.html', context)
